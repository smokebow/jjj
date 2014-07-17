from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    bio = models.TextField()
    mail = models.EmailField()

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)




