from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        app_label = 'crudapp'

class Operator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        app_label = 'crudapp'
        
class Request(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('R', 'Rejected'),
    ]
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    client = models.ForeignKey(Client, related_name='requests', on_delete=models.CASCADE)
    processed_by = models.ForeignKey(Operator, related_name='processed_requests', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} - Status: {self.status}"
    
    class Meta:
        app_label = 'crudapp'