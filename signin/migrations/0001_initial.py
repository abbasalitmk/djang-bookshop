# Generated by Django 4.1.7 on 2023-02-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booktable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200)),
                ('bookprice', models.IntegerField()),
                ('bookdesc', models.CharField(max_length=1000)),
            ],
        ),
    ]