## Flask SSE example

> Look ma, no dependencies!

This repository is an example of how to perform [server-sent events (SSE)](https://www.wikiwand.com/en/Server-sent_events) in Flask with no extra dependencies. Libraries such as [flask-sse](https://github.com/singingwolfboy/flask-sse) are great, but they require having to use Redis or some other sort of [pubsub](https://www.wikiwand.com/en/Publish%E2%80%93subscribe_pattern) backend. While this can be fine, I wanted to show that you can do SSE by only using Flask. The following instructions explain how to run the example. For more information on how this works, please see [Max's blog post](https://maxhalford.github.io/blog/flask-sse-no-deps).

### Install

In the first terminal, create a virtual environment, activate it, and install the necessary requirements.

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Run the server

```sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

or

```sh
python app.py
```

### Open browser

- Type into your browser localhost:8080, you should see new stock prices being updated every 2s.
- You can open multiple browsers, they'll show the same data being updated every 2s.

### My improvements

- More practical example using javascript SSE client instead of python SSE client. [See md_sse.html](templates/md_sse.html)
- Add json encode/decode on payload to support `\n` in payload
- Add [mydata.py](mydata.py) to simulate a data source.
  - Data is generated randomly every 2s
  - Data is in markdown and convert to HTML in client-side javascript
- And tidy up
