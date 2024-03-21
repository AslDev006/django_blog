# Generated by Django 5.0.3 on 2024-03-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUTH', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('erkak', 'Male'), ('ayol', 'Female')], default='erkak', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='anywhere', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='static/static_images/none.png', upload_to='users/avatar/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
