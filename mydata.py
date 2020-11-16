import random
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from msg_announcer import announcer


executor = ThreadPoolExecutor(1)


def getContent():
    # markdown
    return f'''## Stock price

|      | Price |
|-----:|:------|
| TSLA | {random.randint(400, 500)} |
| AAPL | {random.randint(100, 140)} |
'''


def loop():
    print('- Data loop started')
    while True:
        announcer.announceSse(getContent())
        sleep(2)
    print('- Data loop ended')


def runDataPollingLoop():
    executor.submit(loop)
