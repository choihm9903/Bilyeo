# Generated by Django 3.1.1 on 2020-09-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=11)),
                ('rev_star', models.IntegerField()),
            ],
        ),
    ]