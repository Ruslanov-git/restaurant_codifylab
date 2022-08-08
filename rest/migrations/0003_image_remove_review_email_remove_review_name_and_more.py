# Generated by Django 4.0.6 on 2022-08-08 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest', '0002_remove_restaurant_image_remove_restaurant_menu_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_restaurant/', verbose_name='Изображения')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image', to='rest.restaurant', verbose_name='Фото')),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='RestaurantImage',
        ),
    ]