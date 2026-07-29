from django.db import models

# Create your models here.





class Project(models.Model):
    image = models.ImageField(upload_to="projects/")
    image_alt = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    title_project_name = models.CharField(max_length=200)
    client = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    role = models.CharField(max_length=100)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.project_name