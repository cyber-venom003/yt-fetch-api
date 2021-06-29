import os
from datetime import timedelta
from celery import Celery
from flask import Flask
from datetime import timedelta

celery_app = None

celery_app = Celery(
        backend="redis://redis/0",
        broker="redis://redis/1"
    )
