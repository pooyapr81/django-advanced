from django.db import models

# Create your models here.
class Post(models.Model):
    '''
    This is a class to define posts for blog app
    '''
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True) #Because the category is defined after the post, we write it here as a string.

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name