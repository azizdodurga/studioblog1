from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "auth.user",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="media/", height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.title

        
    

    
