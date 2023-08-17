from django.db import models

class Call(models.Model):
    
    id = models.AutoField(primary_key=True)
    from_number = models.CharField(max_length=15)
    to_number = models.CharField(max_length=15)
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Call from {self.from_number} to {self.to_number} at {self.start_time}"
