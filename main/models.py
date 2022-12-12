from django.db import models


class Book(models.Model):
    title = models.CharField('Назва', max_length=50)
    author = models.CharField('Автор', max_length=50)
    text = models.TextField('Опис')
    # published = models.DateTimeField(auto_now=True, auto_now_add=False)
    published = models.CharField('Рік видання', max_length=4, default='2022')
    count = models.IntegerField('Кількість', default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Експонат'
        verbose_name_plural = 'Експонати'





