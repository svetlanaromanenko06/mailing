from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    '''Создание модели блога в таблице БД'''

    title = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', default='blog/no_image.jpg', verbose_name='изображение', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='дата публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}, {self.description}, {self.views_count}'

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"