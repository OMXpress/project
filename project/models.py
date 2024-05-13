from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    speed = models.CharField(max_length=200)
    POP_name = models.CharField(max_length=400)
    DSLAM_hostname = models.CharField(max_length=200)
    frame = models.CharField(max_length=200)
    


    def __str__(self):
            return self.name + ' ' + "Customer" 