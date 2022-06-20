from msilib.schema import Feature
from django.contrib import admin

# add các bảng bên model vào trang admin
from .models import Commune, Country, District, Features, House, HouseLessor, ImageHouse, PropertiesEmail, Province, Search, Service, ServiceHouse, TopProvince, UserLike, contactMe

# Register your models here.



class UserSearchAdmin(admin.ModelAdmin):
    # hiển thị tiêu đề bảng admin là các cột 
    list_display = ["UserSearch"]
    # thêm thanh công cụ tìm kiếm
    search_fields = ['UserSearch']
    # thêm cột filter
    list_filter =["UserSearch"]
admin.site.register(Search,UserSearchAdmin)


class HouseLessorAdmin(admin.ModelAdmin):
    list_display = ["NameLessor","Sex", "PhoneNumber","Image","Address","Email","Facebook"]
    search_fields = ['NameLessor']
    list_filter =["NameLessor","Sex", "PhoneNumber","Image","Address","Email","Facebook"]
admin.site.register(HouseLessor,HouseLessorAdmin)


class  CountryAdmin(admin.ModelAdmin):
    list_display = ["nameCountry"]
    search_fields = ['nameCountry']
    list_filter =["nameCountry"]
admin.site.register(Country, CountryAdmin)


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ["nameProvince"]
    search_fields = ['nameProvince']
    list_filter =["nameProvince"]
admin.site.register(Province,ProvinceAdmin)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ["nameDistrict"]
    search_fields = ['nameDistrict']
    list_filter =["nameDistrict"]
admin.site.register(District,DistrictAdmin)

class CommuneAdmin(admin.ModelAdmin):
    list_display = ["nameCommune"]
    search_fields = ['nameCommune']
    list_filter =["nameCommune"]
admin.site.register(Commune,CommuneAdmin)

class HouseAdmin(admin.ModelAdmin):
    list_display = ["Color","Price", "KindOfHouse","State","legalDocuments","Size","LandArea","link_map","urlFrame","YearBuilt","Description","author","HouseLessor","Country","Province","District","Commune"]
    search_fields = ['KindOfHouse']
    list_filter =["Color","Price", "KindOfHouse","State","legalDocuments","Size","LandArea","link_map","urlFrame","YearBuilt","Description","author","HouseLessor","Country","Province","District","Commune"]
admin.site.register(House,HouseAdmin)

class ImageHouseAdmin(admin.ModelAdmin):
    list_display = ["LinkImageFirst","LinkImageSecond","LinkImageThird","LinkImageFourth","LinkImageFifth","NoteImage", "House"]
    search_fields = ['NoteImage']
    list_filter =('LinkImageFirst',"LinkImageSecond","LinkImageThird","LinkImageFourth","LinkImageFifth",'NoteImage', 'House')
admin.site.register(ImageHouse,ImageHouseAdmin)

# class ServiceBathsAdmin(admin.ModelAdmin):
#     list_display = ["NameService","Quatity"]
#     search_fields = ['NameService',"Quatity"]
#     list_filter =["NameService","Quatity"]
# admin.site.register(ServiceBaths,ServiceBathsAdmin)

# class ServiceRoomsAdmin(admin.ModelAdmin):
#     list_display = ["NameService","Quatity"]
#     search_fields = ['NameService',"Quatity"]
#     list_filter =["NameService","Quatity"]
# admin.site.register(ServiceRooms,ServiceRoomsAdmin)

# class ServiceBedsAdmin(admin.ModelAdmin):
#     list_display = ["NameService","Quatity"]
#     search_fields = ['NameService',"Quatity"]
#     list_filter =["NameService","Quatity"]
# admin.site.register(ServiceBeds,ServiceBedsAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["nameServiceFirst","QuatityFirst","nameServiceSecond","QuatitySecond","nameServiceThird","QuatityThird"]
    search_fields = ["nameServiceFirst","QuatityFirst","nameServiceSecond","QuatitySecond","nameServiceThird","QuatityThird"]
    list_filter =["nameServiceFirst","QuatityFirst","nameServiceSecond","QuatitySecond","nameServiceThird","QuatityThird"]
admin.site.register(Service,ServiceAdmin)


class ServiceHouseAdmin(admin.ModelAdmin):
    list_display = ["Service","House"]
    search_fields = ["Service","House"]
    list_filter =["Service","House"]
admin.site.register(ServiceHouse,ServiceHouseAdmin)



class TopProvinceAdmin(admin.ModelAdmin):
    list_display = ["FooterImage","nameProvince"]
    search_fields = ["FooterImage","nameProvince"]
    list_filter =["FooterImage","nameProvince"]
admin.site.register(TopProvince,TopProvinceAdmin)


# footer
class PropertiesEmailAdmin(admin.ModelAdmin):
    list_display = ["id","Email"]
    search_fields =["id","Email"]
    list_filter = ["id","Email"]
admin.site.register(PropertiesEmail,PropertiesEmailAdmin)

class UserLikeAdmin(admin.ModelAdmin):
    list_display = ["id","idUserLike","idHouseLike","value"]
    search_fields =["id","idUserLike","idHouseLike","value"]
    list_filter = ["id","idUserLike","idHouseLike","value"]
admin.site.register(UserLike,UserLikeAdmin)


# details
class DetailsAdmin(admin.ModelAdmin):
    list_display = ["Name","Email","Number","WriteMessage"]
    search_fields = ['Name']
    list_filter = ["Name","Email","Number","WriteMessage"]
admin.site.register(contactMe,DetailsAdmin)

# Features Details
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ["InteriorDetailsFirst","InteriorDetailsSecond","InteriorDetailsThird","OutdoorFirst","OutdoorSecond","OutdoorThird","UtilitiesFirst","UtilitiesSecond","UtilitiesThird","OtherFirst","OtherSecond"]
    search_fields = ["InteriorDetailsFirst","InteriorDetailsSecond","InteriorDetailsThird","OutdoorFirst","OutdoorSecond","OutdoorThird","UtilitiesFirst","UtilitiesSecond","UtilitiesThird","OtherFirst","OtherSecond"]
    list_filter = ["InteriorDetailsFirst","InteriorDetailsSecond","InteriorDetailsThird","OutdoorFirst","OutdoorSecond","OutdoorThird","UtilitiesFirst","UtilitiesSecond","UtilitiesThird","OtherFirst","OtherSecond"]
admin.site.register(Features,FeaturesAdmin)