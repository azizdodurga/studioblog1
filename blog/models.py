from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "auth.user",
        on_delete=models.CASCADE
    )
    image_1 = models.ImageField(upload_to="media/", height_field=None, null=True, width_field=None, max_length=100)
    image_2 = models.ImageField(upload_to="media/", height_field=None, null=True, width_field=None, max_length=100)
    image_3 = models.ImageField(upload_to="media/", height_field=None, null=True, width_field=None, max_length=100)
    image_4 = models.ImageField(upload_to="media/", height_field=None, null=True, width_field=None, max_length=100)

    class Meta():
        ordering = ['-date']

    def __str__(self):
        return self.title

        
    

    
