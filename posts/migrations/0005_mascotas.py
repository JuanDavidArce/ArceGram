# Generated by Django 3.2.7 on 2021-09-10 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
    ]
