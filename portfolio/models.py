from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to='portfolio/images/')
  sourceUrl = models.URLField()
  liveUrl = models.URLField(max_length=300)

  def __str__(self):
    return self.title