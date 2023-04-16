from django.db import models


class reed_solomon(models.Model):
    position = models.IntegerField(help_text='позиция на странице относительно начала', default=0, blank=True)
    paragraf_name = models.CharField(max_length=100, help_text='название блока')
    paragraf_content = models.TextField(help_text='текст блока')
    def __str__(self):
        return self.paragraf_name