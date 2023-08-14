from django.db import models

class Nameauthor(models.Model):
    author = models.CharField(max_length=255)
    def __str__(self):
        return self.author
    
class New(models.Model):
    headlines = models.CharField(max_length= 255)
    newscontent =models.TextField()
    author = models.ForeignKey(Nameauthor, on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Article."""

        verbose_name = 'new'
        verbose_name_plural = 'news'
        
    def __str__(self):
        return self.headlines
    
    def get_absolute_url(self):
        return reversed("New_detail", kwargs={"pk": self.pk})

