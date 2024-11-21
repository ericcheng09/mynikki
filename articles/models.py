from django.db import models 
from django.utils.timezone import now
import time

def ts_now():
    return int(time.time())

# Create your models here.
class Article(models.Model):
    date = models.DateField(default=now)
    content = models.TextField(blank=True)
    create_at = models.IntegerField(default=ts_now)
    update_at = models.IntegerField(default=ts_now)
    