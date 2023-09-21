from django.db import models

class Describe(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

