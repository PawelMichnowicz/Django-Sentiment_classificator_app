from django.db import models

# Create your models here.
class Sentence(models.Model):
    text = models.TextField()
    result = models.IntegerField()
    result2 = models.IntegerField()
    result3 = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']

    def __str__(self) :
        return self.text[:10] + "__" + str(self.result)

    