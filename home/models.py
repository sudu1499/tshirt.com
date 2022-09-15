from django.db import models

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='home/images/') 

    def __str__(self):
        return self.category_name+str(self.id)