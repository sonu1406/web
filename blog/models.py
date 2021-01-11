from django.db import models

class Blog(models.Model):
    Title=models.CharField(max_length=300)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
