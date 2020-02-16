# Generated by Django 2.2.10 on 2020-02-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('vote_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
