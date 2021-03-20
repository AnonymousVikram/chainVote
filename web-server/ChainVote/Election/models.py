from django.db import models

# Create your models here.
class Election(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()


class Candidates(models.Model):
    election = models.ForeignKey(Election, null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length=1000)
    vote_count = models.IntegerField(default=0)

