from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
    wait_time = between(1, 2.5)
    host = "https://numericalintfunc.azurewebsites.net"  # Base URL of your Function App

    @task
    def calculate_integral(self):
        self.client.get("/api/numericalintegralfunction?lower=0&upper=3.14&n=1000")