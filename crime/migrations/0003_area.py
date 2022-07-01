# Generated by Django 3.0.3 on 2020-02-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0002_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('doorno', models.CharField(max_length=10)),
                ('stname', models.CharField(max_length=200)),
                ('villcit', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=20)),
                ('contactnumber', models.CharField(max_length=50)),
            ],
        ),
    ]
