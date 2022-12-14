# Generated by Django 4.0.6 on 2022-08-05 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Заведение',
                'verbose_name_plural': 'Заведения',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image_restaurant/', verbose_name='Изображения')),
                ('phone_number_1', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('phone_number_2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('phone_number_3', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Местоположение')),
                ('openning_times', models.TextField(verbose_name='Время работы')),
                ('menu_image', models.ImageField(upload_to='menu_restaurant/', verbose_name='Меню')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='Ссылка')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=255, verbose_name='Афиша')),
                ('image', models.ImageField(upload_to='sale_image/', verbose_name='Фото')),
                ('text', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='selections_image/', verbose_name='Фото')),
                ('url', models.SlugField(max_length=160, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Подборка',
                'verbose_name_plural': 'Подборки',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest.review', verbose_name='Родитель')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ресторан', to='rest.restaurant')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Отзыв', to='rest.review', verbose_name='Отзыв'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest.sale', verbose_name='Акция'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='selections',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest.selection', verbose_name='Подборка'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.restaurant', verbose_name='ресторан')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
    ]
