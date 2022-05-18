from distutils.command.upload import upload
from enum import unique
from operator import mod
from pyexpat import model
from django.db import models
from contact.models import contactEmail
import os
import datetime

from django.forms import FilePathField
# Create your models here.

# search
class Search(models.Model):
    UserSearch = models.TextField(null=False);
    
    
    def __str__(self):
        return f"{self.id},{self.UserSearch}"

# người cho thuê
class HouseLessor(models.Model):
    NameLessor = models.CharField(max_length=100,null=False)
    Sex = models.CharField(max_length=10,null=False)
    PhoneNumber = models.CharField(default='' , max_length=15)
    Address = models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return f"{self.id},{self.NameLessor}"
    
    
# Tỉnh
class Province(models.Model):

    nameProvince = models.CharField(max_length=100,null=False)
    def __str__(self):
        return f"{self.id},{self.nameProvince}"
    
    
    
# Huyện
class District(models.Model):

    nameDistrict = models.CharField(max_length=100,null=False)    
    def __str__(self):
        return f"{self.id},{self.nameDistrict}"
    
    
    
# Xã
class Commune(models.Model):
    nameCommune = models.CharField(max_length=100,null=False)    
    
    def __str__(self):
        return f"{self.id},{self.nameCommune}"
    
# Nhà
class House(models.Model):
    Color = models.CharField(max_length=100,null=False)
    Price = models.CharField(max_length=100,null=False)
    KindOfHouse = models.CharField(max_length=100,null=False)
    State = models.CharField(max_length=100,null=False)
    legalDocuments = models.CharField(max_length=100,null=False)
    Area = models.CharField(max_length=20,null=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    # foreignKey
    # nếu xóa người cho thuê thì nó cũng sẽ xóa
    HouseLessor = models.ForeignKey(HouseLessor , on_delete=models.CASCADE,null=True)
    Province = models.ForeignKey(Province, on_delete=models.CASCADE,null=True)
    District = models.ForeignKey(District , on_delete=models.CASCADE,null=True)
    Commune = models.ForeignKey(Commune , on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return f"{self.id},{self.HouseLessor}"


# ảnh nhà
class ImageHouse(models.Model):
    LinkImageFirst = models.ImageField(upload_to="images/", null=True, verbose_name="",unique=True)
    LinkImageSecond = models.ImageField(upload_to="images/", null=True, verbose_name="",unique=True)
    LinkImageThird = models.ImageField(upload_to="images/", null=True, verbose_name="",unique=True)
    LinkImageFourth = models.ImageField(upload_to="images/", null=True, verbose_name="",unique=True)
    LinkImageFifth = models.ImageField(upload_to="images/", null=True, verbose_name="",unique=True)
    NoteImage = models.CharField(max_length=100,null=False)
    House = models.ForeignKey(House , on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.id},{self.LinkImageFirst},{self.LinkImageSecond},{self.LinkImageThird},{self.LinkImageFourth},{self.LinkImageFifth}"
    

# # 3 dịch vụ 
# class ServiceBaths(models.Model):
#     NameService = models.CharField (max_length=100,null=True)
#     Quatity = models.IntegerField(null=False)
#     def __str__(self):
#         return f"{self.id},{self.NameService}"

# class ServiceRooms(models.Model):
#     NameService = models.CharField (max_length=100,null=True)
#     Quatity = models.IntegerField(null=False)
#     def __str__(self):
#         return f"{self.id},{self.NameService}"
# class ServiceBeds(models.Model):
#     NameService = models.CharField (max_length=100,null=True)
#     Quatity = models.IntegerField(null=False)
#     def __str__(self):
#         return f"{self.id},{self.NameService}"




# Dịch vụ
class Service(models.Model):
    # ServiceBaths = models.ForeignKey (ServiceBaths, on_delete=models.CASCADE,null=True)
    # ServiceRooms = models.ForeignKey (ServiceRooms, on_delete=models.CASCADE,null=True)
    # ServiceBeds = models.ForeignKey (ServiceBeds, on_delete=models.CASCADE,null=True)
    nameServiceFirst = models.CharField(max_length=100,null=True)
    QuatityFirst = models.IntegerField(null=False)
    nameServiceSecond = models.CharField(max_length=100,null=True)
    QuatitySecond = models.IntegerField(null=False)
    nameServiceThird = models.CharField(max_length=100,null=True)
    QuatityThird = models.IntegerField(null=False)
    def __str__(self):
        return f"{self.id},{self.nameServiceFirst},{self.QuatityFirst},{self.nameServiceSecond},{self.QuatitySecond},{self.nameServiceThird},{self.QuatityThird}"

# Dịch vụ của nhà
class ServiceHouse(models.Model):
    House = models.ForeignKey(House , on_delete=models.CASCADE,null=True)
    Service = models.ForeignKey (Service, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.id},{self.House},{self.Service}"
    

# top tỉnh của nhà có giá cao nhất
class TopProvince(models.Model):
    FooterImage = models.ImageField(upload_to="images/", null=False, verbose_name="")
    nameProvince = models.ForeignKey(Province, on_delete=models.CASCADE,null=False)

    def __str__(self):
        return f"{self.id},{self.FooterImage},{self.nameProvince}"


class PropertiesEmail(models.Model):
    Email = models.EmailField(null=False)
    # idUser = models.ForeignKey(HouseLessor, on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return f"{self.id},{self.Email}"

class UserLike(models.Model):
    idUserLike = models.ForeignKey(HouseLessor, on_delete=models.CASCADE,null=True)
    idHouseLike = models.ForeignKey(House, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.id},{self.idUserLike},{self.idHouseLike}"               