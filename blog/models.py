from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  date = models.DateField()
  image = models.ImageField(blank =True, upload_to='blog/images/')
  def __str__(self):
    return self.title
