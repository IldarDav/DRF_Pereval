from django.db import models


class Users(models.Model):
    email = models.EmailField()
    phone = models.TextField(max_length=255, verbose_name='Контактный телефон')
    first_name = models.TextField(max_length=255, verbose_name='Имя')
    last_name = models.TextField(max_length=255, verbose_name='Фамилия')
    surname = models.TextField(max_length=255, verbose_name='Отчество')


class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f"Широта: {self.latitude}, Долгота: {self.longitude}, Высота: {self.height}"


class Level(models.Model):
    winter = models.TextField(null=True, blank=True, verbose_name='Зима')
    spring = models.TextField(null=True, blank=True, verbose_name='Весна')
    summer = models.TextField(null=True, blank=True, verbose_name='Лето')
    autumn = models.TextField(null=True, blank=True, verbose_name='Осень')


class Images(models.Model):
    pereval = models.ForeignKey('Pereval', related_name='images', on_delete=models.CASCADE, default='1')
    data = models.URLField(verbose_name='Изображение', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')
    add_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} {self.title}'


class Pereval(models.Model):
    STATUS_CHOICES = [
        ("new", "новый"),
        ("pending", "в работе"),
        ("accepted", "принят"),
        ("rejected", "отклонен"),
    ]
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.TextField(choices=STATUS_CHOICES, default='new')
    beauty_title = models.TextField(blank=True, verbose_name='Основное название вершины', null=True)
    title = models.TextField(blank=True, null=True, verbose_name='Название вершины')
    other_titles = models.TextField(blank=True, null=True, verbose_name='Другое название')
    connect = models.TextField(blank=True, null=True)
    add_time = models.TimeField(auto_now_add=True)
