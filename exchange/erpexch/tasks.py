from celery import shared_task
@shared_task
def test(test_str: str) -> None:
    print(f"Test string: {test_str}")    