from django.db import models


class Agent(models.Model):
    name = models.CharField('ФИО', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    city = models.CharField('Город', max_length=50)
    profession = models.CharField('Профессия', max_length=50)
    profession_description = models.CharField('Мини описание услуг', max_length=200, default='Описание услуг')
    services = models.TextField('Услуги (цена);')
    priority = models.IntegerField('Приоритет показа на странице')
    avatar = models.ImageField(upload_to='avatars', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return str(self.priority) + ' ' + str(self.name)
