from django.db import models

class nameauthor(models.Model):
    author = models.CharField(max_length=255)
    def __str__(self):
        return self.author
    
class news(models.Model):
    headlines = models.CharField(max_length= 255)
    newscontent =models.TextField()
    author = models.ForeignKey(nameauthor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.headlines

