from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in range(10000):
        print("from celery : {}".format(i))
    return "Done Processing In Celery"

@shared_task(bind=True)
def test_func1(self):
    for i in range(10000):
        print("from celery : {}".format("************"))
    return "Done Processing In Celery"