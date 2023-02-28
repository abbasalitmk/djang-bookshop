from django.db import models


class Booktable(models.Model):
    bookname = models.CharField(max_length=200)
    bookprice = models.IntegerField()
    bookdesc = models.CharField(max_length=1000)
    bookimage = models.CharField(max_length=1000)
