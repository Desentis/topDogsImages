from django.db import models


class Voted(models.Model):
    link = models.URLField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return ' '.join([self.link, str(self.votes)])
