from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    '''Testimonial model
    ---
    Attributes:
        name: Name of the reviewer
        body: Customer comments
        created_on: Date and time created
        approved: Approval status
    '''

    user = models.ForeignKey(
        User,
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        )
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    body = models.TextField(max_length=250, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Testimonial {self.body} by {self.name}"
