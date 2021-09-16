from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='Posts/%Y/%m/%d/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
