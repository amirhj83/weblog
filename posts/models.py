from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    publish_date = models.DateField(null=True)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField()
    def __str__(self):
         return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)




