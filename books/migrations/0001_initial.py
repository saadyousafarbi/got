# Generated by Django 2.2.5 on 2019-09-25 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('isbn', models.CharField(max_length=20)),
                ('number_of_pages', models.IntegerField()),
                ('released_date', models.DateTimeField()),
                ('authors', models.ManyToManyField(related_name='authors', to='books.Author')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='books.Country')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='books.Publisher')),
            ],
        ),
    ]
