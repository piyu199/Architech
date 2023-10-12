from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='photos',blank=True)
    body = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_by=models.DateTimeField(auto_now_add=True,editable=False) 

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name="BlogPost"
        verbose_name_plural="BlogPosts"
    