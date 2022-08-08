from django.db import models

from custom_auth.models import MyUser


class Category(models.Model):
    """Категории"""
    name = models.CharField('Название', max_length=255)
    url = models.SlugField('Ссылка', max_length=160, unique=True)

    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Selection(models.Model):
    """Подборки"""
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Фото', upload_to="selections_image/")
    url = models.SlugField('Ссылка', max_length=160, unique=True)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Sale(models.Model):
    """Акции"""
    time_create = models.DateTimeField('Дата добавления', auto_now_add=True)
    time_update = models.DateTimeField('Дата обновления', auto_now=True)
    name = models.CharField('Афиша', max_length=255)
    image = models.ImageField('Фото', upload_to="sale_image/")
    text = models.TextField('Описание')
    url = models.SlugField('Ссылка', max_length=160, unique=True)

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class Restaurant(models.Model):
    """Все заведения"""
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    # image = models.ImageField('Изображения', upload_to='image_restaurant/')
    phone_number_1 = models.CharField('Номер телефона', max_length=15)
    phone_number_2 = models.CharField('Номер телефона', max_length=15, blank=True, null=True)
    phone_number_3 = models.CharField('Номер телефона', max_length=15, blank=True, null=True)
    address = models.CharField('Местоположение', max_length=255)
    openning_times = models.CharField('Время работы', max_length=255)
    # menu_image = models.ImageField('Меню', upload_to='menu_restaurant/')
    selections = models.ForeignKey(Selection, verbose_name='Подборка', on_delete=models.SET_NULL,
                                   blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL,
                                 null=True)
    sale = models.ForeignKey(Sale, verbose_name='Акция', on_delete=models.SET_NULL,
                             blank=True, null=True)
    review = models.ForeignKey('Review', related_name='Отзыв', verbose_name='Отзыв',
                               on_delete=models.SET_NULL, blank=True, null=True)
    url = models.SlugField('Ссылка', max_length=160, unique=True)

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'


class Image(models.Model):
    image = models.ImageField('Изображения', upload_to='image_restaurant/')
    restaurant = models.ForeignKey(Restaurant, related_name='image', verbose_name='Фото',
                                   on_delete=models.SET_NULL, null=True)


class Review(models.Model):
    """Отзывы"""
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    text = models.TextField('Сообщение')
    restaurant = models.ForeignKey(Restaurant, related_name='Ресторан', on_delete=models.CASCADE)

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='ресторан')

    def __str__(self):
        return f'{self.star} - {self.restaurant}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
