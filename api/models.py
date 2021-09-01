from django.db import models

# Create your models here.

#models created
class Book(models.Model):
   book_title = models.CharField(max_length=200, null=False, blank=False)
   book_category = models.CharField(max_length=100,null=False, blank=False)
   book_price = models.CharField(max_length=200, null=False, blank=False)#models.DecimalField(max_digits=4,decimal_places=2)
   book_description = models.TextField()
   stars = models.IntegerField()


   def __str__(self):
        return self.book_title