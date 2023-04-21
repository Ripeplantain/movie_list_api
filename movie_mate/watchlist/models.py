from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class StreamPlatform(models.Model):

    name = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WatchList(models.Model):

    title = models.CharField(max_length=100)
    storyline = models.TextField()
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist", default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    

class Review(models.Model):

    review_user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, null=True, related_name="review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title