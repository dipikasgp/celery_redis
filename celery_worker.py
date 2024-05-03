from celery_util import CeleryUtil

app_name = 'celery_task_handler'

app = CeleryUtil.create_celery_app(app_name)
app.autodiscover_tasks(related_name=app_name)


if __name__ == '__main__':

    print('Celery starting!')
    # solo worker
    app.start(argv=['-A', app_name, 'worker', '--pool=solo', '--loglevel=info'])
    # app.start(argv=['-A', app_name, 'worker', '--pool=solo', '--loglevel=info',
    #                 f'--logfile={__logger.handlers[0].baseFilename}'])
