from celery import Celery


class CeleryUtil:
    __code_dir_to_monitor = None
    __celery_working_dir = None

    def __init__(self):
        pass

    @classmethod
    def create_celery_app(cls, name, redis_config=None):
        # cls.__code_dir_to_monitor = get_root_dir()
        # cls.__celery_working_dir = working_dir


        redis_host = 'localhost'
        redis_port = 6379

        # Redis broker URL
        broker_url = f'redis://{redis_host}:{redis_port}/0'

        # Process result
        backend_url = f'redis://{redis_host}:{redis_port}/0'

        app = Celery(name, broker=broker_url, backend=backend_url, task_track_started=True,
                     task_acks_late=True, worker_prefetch_multiplier=1, broker_connection_retry_on_startup=True)

        return app
