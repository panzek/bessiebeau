from django.db import models


class Contact(models.Model):
    """ 
    Contact model for customers to contact store owner 
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=150, null=False, blank=False)
    message = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
