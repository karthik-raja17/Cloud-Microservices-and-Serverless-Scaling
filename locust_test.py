from locust import HttpUser, task

class QuickstartUser(HttpUser):
    host = "https://gentle-river-97853206fcd24c989bed9f976f7f6174.azurewebsites.net" 

    @task
    def hello_world(self):
        self.client.get("/numericalintegralservice/0/3.14159")
