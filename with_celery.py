from celery import Celery
import requests
import json

CELERY_RESULT_BACKEND = 'db+postgresql://sanket:sanket@localhost/postgres'
# backend='db+postgresql://user:password@localhost/db_name',

app = Celery('with_celery', broker='redis://localhost:6379/0', backend=CELERY_RESULT_BACKEND)



@app.task
def fetch_url(url,name):
    data={}
    data=json.dumps(data)
    with open(f"{name}.json", "w") as outfile:
        outfile.write(data)
    resp = requests.get(url)
    print(resp.status_code)


def func(urls):
    print("hellloo")
    for url in range(len(urls)):
        celeryTask = fetch_url.delay(urls[url], url)
        print(celeryTask.id)


if __name__ == "__main__":
	func(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])