from celery_worker import app


class CeleryTasksHandler:

    def __init__(self):
        pass

    @app.task()
    def time_consuming_function(self):
        for _ in range(10 ** 8):
            # Simulate some computation by performing a simple operation
            _ = 2 + 2
        return True