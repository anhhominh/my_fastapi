from celery import Celery
from configs.envs import settings

celery_app = Celery('hello', broker=settings.CELERY_URL)

@celery_app.task(name='Hello task')
def hello():
    return 'Hello world!'