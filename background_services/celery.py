from celery import Celery
from configs.envs import Env

celery_app = Celery('hello', broker=Env.CELERY_URL)

@celery_app.task(name='Hello task')
def hello():
    return 'Hello world!'