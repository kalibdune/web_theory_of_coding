from django.db import models

class Block_hamming(models.Model):
    position = models.IntegerField(help_text='позиция на странице относительно начала', default=0, blank=True)
    paragraf_name = models.CharField(max_length=100, help_text='название блока')
    paragraf_content = models.TextField(help_text='текст блока')
    def __str__(self):
        return self.paragraf_name

class Task(models.Model):
    text = models.TextField(help_text='содержимое задания')
    answer = models.CharField(max_length=50, help_text='ответ на задание')
    level = models.IntegerField(default=0, help_text='уровень сложности')
    def __str__(self):
        return str(self.id)
