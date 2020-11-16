import flask
from urllib.parse import urljoin

from msg_announcer import announcer
import mydata


app = flask.Flask(__name__)


@app.route('/')
def root():
    mydata.runDataPollingLoop()
    return flask.render_template('md_sse.html', mdStr=mydata.getContent(), base_url=urljoin(flask.request.base_url, 'listen'))


@app.route('/ping')
def ping():
    # manually sending data to SSE client
    content = mydata.getContent()
    announcer.announceSse(content)
    return content, 200


@app.route('/listen', methods=['GET'])
def listen():

    def stream():
        messages = announcer.listen()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg

    return flask.Response(stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)
