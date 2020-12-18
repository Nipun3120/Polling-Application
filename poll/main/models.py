from django.db import models

# Create your models here.

class Questions(models.Model):
    content = models.CharField(max_length = 1024)

    def __str__(self):
        return self.content

class Choice(models.Model):
    question = models.ForeignKey('Questions', on_delete = models.CASCADE)
    content = models.CharField(max_length = 256)

    def __str__(self):
        return "{} - {}".format(self.question.content[:50], self.content) 
