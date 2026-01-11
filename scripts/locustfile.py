from locust import HttpUser, task


class HealthcheckUser(HttpUser):
    @task
    def healthcheck(self) -> None:
        self.client.get("/healthcheck")
