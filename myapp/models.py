from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.degree

class Name(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"