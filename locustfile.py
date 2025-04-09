from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def load_dashboard(self):
        self.client.get("/employees")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)