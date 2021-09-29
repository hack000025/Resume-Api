from django.db import models
import uuid, datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class TimeStampModel(models.Model):
    id = models.IntegerField (primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Education(models.Model):
    college_name = models.CharField(primary_key=True , max_length=90)
    stream =models.CharField(max_length=50,blank=True)
    percentage = models.CharField(max_length=50,blank=True)
    subject = models.CharField(max_length=50 , blank=True)
    Passout_Date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.college_name

    class Meta:
        db_table='Education'


class Projects(models.Model):

    live_projects = models.BooleanField()
    personal = models.BooleanField()
    project_name = models.CharField(primary_key=True,max_length=256)
    duration = models.CharField(max_length=250 , blank = True)
    langauges = models.CharField(max_length=50 ,blank = True)
    role = models.CharField(max_length=250)
    description = models.CharField(max_length=550 , blank = True)
    project_url =  models.URLField(max_length=200 , blank= True)

    def __str__(self):
        return self.project_name

    class Meta:
        db_table ='user_Projects'
        verbose_name_plural="Projects"


class Experience(models.Model):
    company_name = models.CharField(primary_key=True ,max_length=50)
    ex_year_or_month = models.CharField(max_length=64)


    def __str__(self):
        return self.ex_year_or_month
    class Meta:
        db_table='user_Experience'
        verbose_name_plural="Experience"


class Skills(models.Model):
    Programming_lang=models.CharField(primary_key=True,max_length=50)
    def __str__(self):
        return self.Programming_lang
    class Meta:
        db_table='Skill'
        verbose_name_plural="Skills"


class Certification(models.Model):
    certificate_name = models.CharField(primary_key=True, max_length=50)
    Certificate_url = models.URLField(max_length=200 , blank=True)

    class Meta:
        db_table='user_Certification'
        verbose_name_plural="Certification"

    def __str__(self):
        return self.certificate_name


class Profile(TimeStampModel):
    Name = models.CharField(max_length=64)
    user_sex = (('MALE', 'Male'), ('FEMALE', 'Female'))
    sex = models.CharField(max_length=6, default='Male', choices= user_sex)
    phone = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    Project = models.ManyToManyField(Projects,related_name='Project')
    Experinces = models.ManyToManyField(Experience,related_name='Experience')
    Certification = models.ManyToManyField(Certification,related_name='Certification')
    skills = models.ManyToManyField(Skills,related_name='Skills')
    def __str__(self):
        return self.Name

    @staticmethod
    def exists(**kwargs):
        if Profile.objects.filter(**kwargs).exists():
            return True
        return False

    class Meta:
        db_table = 'Profile'
