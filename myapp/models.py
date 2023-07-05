from django.db import models
from datetime import datetime
# Create your models here.
# CLASS = TABLE
# ATTRIBUTES = COLUMNS

class Enquiry(models.Model):
    name = models.CharField(max_length=30,verbose_name='Enter Name',help_text='Name should be within 30 letters')
    phone = models.IntegerField(verbose_name='Phone Number',help_text='Phone Number should contain 10 digits')
    email = models.EmailField(verbose_name='Email id')
    course = models.CharField(max_length=20,
                              choices=[('Python','Python3'),
                                       ('Java','Java 8'),
                                       ('Web Designing','Web Designing'),
                                       ('Django','Django'),
                                       ('Full Stack','Full Stack')])
    session = models.CharField(max_length=10,choices=[('Morning','Morning'),
                                                      ('Evening','Evening')],
                               default='Morning')
    date = models.DateTimeField(default=datetime.now())


class Student(models.Model):
    stdId = models.CharField(max_length=10,verbose_name='Student Id')
    stdName = models.CharField(max_length=30, verbose_name='Student Name')
    gender = models.CharField(max_length=15,choices=[('Male','Male'),
                                                     ('Female','Female'),
                                                     ("Transgender","Transgender")])
    email = models.EmailField()
    phone = models.BigIntegerField()
    course = models.CharField(max_length=25,choices=[('Python','Python'),
                                                     ('Java','Java'),
                                                     ('C','C'),
                                                     ('C++','C++'),
                                                     ('Django','Django'),
                                                     ('Full Stack','Full Stack')],
                              default='Python')
    joiningDate = models.DateField()
    fees = models.IntegerField()
    status = models.CharField(max_length=15,choices=[('Yet to Start','Yet to Start'),
                                                     ('Started','Started'),
                                                     ('Hold','Hold'),
                                                     ('Discontinued','Discontinued'),
                                                     ('Completed','Completed')])
    address = models.TextField()