# Generated by Django 2.1.3 on 2018-12-03 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListPostPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listId', models.IntegerField()),
                ('postId', models.IntegerField()),
                ('imageId', models.TextField()),
            ],
            options={
                'db_table': 'ListPostPhoto',
            },
        ),
        migrations.CreateModel(
            name='PathsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialID', models.IntegerField()),
                ('pathID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PostFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('urlStatic', models.TextField()),
                ('authId', models.IntegerField()),
                ('localsIds', models.TextField()),
            ],
            options={
                'db_table': 'PostFeed',
            },
        ),
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('cookie', models.TextField()),
                ('image', models.TextField()),
            ],
            options={
                'db_table': 'UserAuth',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userauth',
            unique_together={('userId',)},
        ),
        migrations.AlterUniqueTogether(
            name='postfeed',
            unique_together={('userId', 'authId')},
        ),
        migrations.AlterUniqueTogether(
            name='listpostphoto',
            unique_together={('listId', 'postId', 'imageId')},
        ),
    ]
