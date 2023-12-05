from django.db import models

# Create your models here.

class Main(models.Model):

    phone_number = models.CharField('Phone number', max_length=20)
    email = models.EmailField('Email')
    location = models.CharField('Location', max_length=70)
    logo = models.ImageField('Logo')
    main_name_first = models.CharField('Main name first', max_length=30)
    main_name_second = models.CharField('Main name second', max_length=30)
    name_first = models.CharField('Name first', max_length=30)
    name_second = models.CharField('Name second', max_length=30)
    button_name = models.CharField('Button name', max_length=20)


class About(models.Model):

    name = models.CharField('About name', max_length=20)
    description = models.TextField('About description')
    button_name = models.CharField('Button name', max_length=20)


class Class(models.Model):
     
    name = models.CharField('Class name', max_length=40)
    description = models.TextField('Class description')


class ClassImage(models.Model):

    name = models.CharField('Class name', max_length=40)
    button_name = models.CharField('Button name', max_length=20)
    image = models.ImageField('Class image')
    icon_image = models.ImageField('Icon image')


class Blog(models.Model):

    name = models.CharField('Blog name', max_length=40)
    description = models.TextField('Blog description')


class BlogImage(models.Model):

    name = models.CharField('Blog name', max_length=40)
    description = models.TextField('Blog description')
    date = models.DateField('Blog date')
    button_name = models.CharField('Button name', max_length=20)
    image = models.ImageField('Blog image')    

