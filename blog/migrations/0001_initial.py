# Generated by Django 2.1.5 on 2019-01-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('draft', models.BooleanField(default=True, verbose_name='Is Draft')),
                ('thumb', models.ImageField(upload_to='thumbs/', verbose_name='Thumbnail')),
                ('keywords', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Keywords')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Publish Date')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-date'],
            },
        ),
    ]
