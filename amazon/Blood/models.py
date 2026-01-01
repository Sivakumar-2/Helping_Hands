from django.db import models


class Donation(models.Model):
    DonorID = models.AutoField(primary_key=True)
    DonorName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=128)
    DateOfBirth = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=10)
    Profession = models.CharField(max_length=100)
    BadHabits = models.TextField()
    BloodGroup = models.CharField(max_length=5)
    Diseases = models.CharField(max_length=300, null=True, blank=True)
    HadRecentInfection = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    RecentInfections = models.CharField(max_length=300, blank=True)
    Location = models.TextField()
    State = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=10)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.DonorName} - {self.BloodGroup}"


from django.db import models

# Create your models here.
