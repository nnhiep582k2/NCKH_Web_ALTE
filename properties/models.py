from distutils.command.upload import upload
from enum import unique
from operator import mod
from pyexpat import model
from django.db import models
from contact.models import contactEmail
from django.contrib.auth.models import User
import os
import datetime

from django.forms import FilePathField
# Create your models here.

# search
class Search(models.Model):
    UserSearch = models.TextField(null=False);
    
    # hàm trả về các trường trong bảng.
    def __str__(self):
        return f"{self.id},{self.UserSearch}"

# người cho thuê
class HouseLessor(models.Model):
    NameLessor = models.CharField(max_length=100,null=False)
    Sex = models.CharField(max_length=10,null=False)
    PhoneNumber = models.CharField(default='' , max_length=15)
    Image =  models.ImageField(upload_to="images/", null=False, verbose_name="")
    Address = models.CharField(max_length=100,null=False)
    Email = models.EmailField(null=False)
    Facebook = models.URLField(max_length=100,null=False)
    def __str__(self):
        return f"{self.id},{self.NameLessor}"
    
    
 # quốc gia
class Country(models.Model):
    nameCountry = models.CharField(max_length=100,null=False)    
    
    def __str__(self):
        return f"{self.id},{self.nameCountry}"
    
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
    
# các đặc trưng
class Features(models.Model):
    InteriorDetailsFirst = models.CharField(max_length=20,null=True)
    InteriorDetailsSecond = models.CharField(max_length=20,null=True)
    InteriorDetailsThird = models.CharField(max_length=20,null=True)
    OutdoorFirst = models.CharField(max_length=20,null=True)
    OutdoorSecond = models.CharField(max_length=20,null=True)
    OutdoorThird = models.CharField(max_length=20,null=True)
    UtilitiesFirst = models.CharField(max_length=20,null=True)
    UtilitiesSecond = models.CharField(max_length=20,null=True)
    UtilitiesThird= models.CharField(max_length=20,null=True)
    OtherFirst = models.CharField(max_length=20,null=True)
    OtherSecond = models.CharField(max_length=20,null=True)
    
 
    def __str__(self):
        return f"{self.id},{self.InteriorDetailsFirst},{self.InteriorDetailsSecond},{self.InteriorDetailsThird},{self. OutdoorFirst},{self. OutdoorSecond},{self. OutdoorThird},{self.UtilitiesFirst},{self.UtilitiesSecond},{self.UtilitiesThird},{self.OtherFirst},{self.OtherSecond}"

    
# Nhà
class House(models.Model):
    Color = models.CharField(max_length=100,null=False)
    Price = models.CharField(max_length=100,null=False)
    KindOfHouse = models.CharField(max_length=100,null=False)
    State = models.CharField(max_length=100,null=False)
    legalDocuments = models.CharField(max_length=100,null=False)
    LandArea = models.CharField(max_length=20,null=False)
    Size = models.CharField(max_length=20,null=False)
    link_map = models.URLField(max_length=100,null=False)
    urlFrame = models.URLField(max_length=10000,null=False)
    linkStreetView = models.URLField(max_length=1000,null=False)
    Description = models.CharField(max_length=1000,null=False)
    YearBuilt = models.CharField(max_length=10,null=False)
    liked = models.ManyToManyField(User, default= None, blank=True , related_name='liked')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', null=True)
    # foreignKey
    # nếu xóa người cho thuê thì nó cũng sẽ xóa
    HouseLessor = models.ForeignKey(HouseLessor , on_delete=models.CASCADE,null=True)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True)
    Province = models.ForeignKey(Province, on_delete=models.CASCADE,null=True)
    District = models.ForeignKey(District , on_delete=models.CASCADE,null=True)
    Commune = models.ForeignKey(Commune , on_delete=models.CASCADE,null=True)
    Features = models.ForeignKey(Features,on_delete=models.CASCADE,null=True)
    
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


# user email 
class PropertiesEmail(models.Model):
    Email = models.EmailField(null=False)
    # idUser = models.ForeignKey(HouseLessor, on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return f"{self.id},{self.Email}"

# user like
LIKE_CHOICRS = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class UserLike(models.Model):
    idUserLike = models.ForeignKey(User, on_delete=models.CASCADE)
    idHouseLike = models.ForeignKey(House, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICRS , default='Like',max_length=10)
    
    def __str__(self):
        return f"{self.id},{self.idUserLike},{self.idHouseLike}"               
    
    
    
    
# contact me details
class contactMe(models.Model):
    Name =  models.CharField(max_length=100,null=False)
    Email = models.EmailField(null=False)
    Number =  models.CharField(default='' , max_length=15)
    WriteMessage = models.TextField(max_length=100)
    
    
    def __str__(self):
        return f"{self.id},{self.Name},{self.Email}"
    
    
