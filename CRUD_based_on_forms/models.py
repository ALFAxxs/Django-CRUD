from django.db import models


# Create your models here.
class Orders(models.Model):
    # picture = models.ImageField(upload_to='test_picture', height_field=None, width_field=None, max_length=100)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='test_picture/', null=True, blank=True)  # Upload to 'media/images/'
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    price = models.FloatField()
    mail = models.EmailField()
    addr = models.CharField(max_length=50)

    def __str__(self):
        return self.fname