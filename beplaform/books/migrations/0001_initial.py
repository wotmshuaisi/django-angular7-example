# Generated by Django 2.1.3 on 2019-02-03 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('siteinfo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=384)),
            ],
        ),
        migrations.CreateModel(
            name='BooksInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wonder', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(blank=True, max_length=32, null=True)),
                ('press', models.CharField(blank=True, max_length=64, null=True)),
                ('isbn', models.CharField(blank=True, max_length=64, null=True)),
                ('month', models.DateField()),
                ('boughtdate', models.DateField()),
                ('price', models.FloatField(default=0.0)),
                ('page', models.IntegerField(default=0)),
                ('quality', models.IntegerField(default=3)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('img', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='siteinfo.BookCategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MarkedBook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.BooksInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('condition', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.BooksInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]