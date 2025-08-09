from locust import HttpUser, task, between
from random import randint

dev = "127.0.0.1:5000"
prod = "http://msse640-project3-env.eba-2r38qkuh.us-east-1.elasticbeanstalk.com"


class LocustUser(HttpUser):
    abstract = True
    host = prod

    def on_start(self):
        self.client.headers.update({"User-Agent": "LocustTestClient/1.0"})


class BasicWebUser(LocustUser):
    wait_time = between(1, 3)

    @task(3)
    def load_homepage(self):
        self.client.get("/")


class BurstWebUser(LocustUser):
    wait_time = between(5, 10)

    @task
    def hit_main_page(self):
        self.client.get("/", name="SpikeUserMainPage")


class ExpensiveUser(LocustUser):
    wait_time = between(5, 10)

    @task
    def hit_expensive_page(self):
        size = randint(0, 510)
        self.client.get(f'/expensive/{size}')