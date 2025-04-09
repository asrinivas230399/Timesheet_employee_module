from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def load_dashboard(self):
        self.client.get("/employees")

    @task
    def submit_feedback(self):
        self.client.post("/feedback", data={"name": "Test User", "feedback": "Great dashboard!"})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
