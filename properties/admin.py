from django.contrib import admin

from .models import Commune, District, House, HouseLessor, ImageHouse, PropertiesEmail, Province, Search, Service, ServiceHouse, TopProvince, UserLike

# Register your models here.


# class TopViewPhotoSecondAdmin(admin.ModelAdmin):
#     list_display = ["TopViewPhotoSecond"]
#     search_fields = ['TopViewPhotoSecond']
#     list_filter =["TopViewPhotoSecond"]
# admin.site.register(TopViewPhotoSecond,TopViewPhotoSecondAdmin)

# class TopViewPhotoThirdAdmin(admin.ModelAdmin):
#     list_display = ["TopViewPhotoThird"]
#     search_fields = ['TopViewPhotoThird']
#     list_filter =["TopViewPhotoThird"]
# admin.site.register(TopViewPhotoThird,TopViewPhotoThirdAdmin)


# class TopViewPhotoFourthAdmin(admin.ModelAdmin):
#     list_display = ["TopViewPhotoFourth"]
#     search_fields = ['TopViewPhotoFourth']
#     list_filter =["TopViewPhotoFourth"]
# admin.site.register(TopViewPhotoFourth,TopViewPhotoFourthAdmin)


# class TopViewPhotoFifthAdmin(admin.ModelAdmin):
#     list_display = ["TopViewPhotoFifth"]
#     search_fields = ['TopViewPhotoFifth']
#     list_filter =["TopViewPhotoFifth"]
# admin.site.register(TopViewPhotoFifth,TopViewPhotoFifthAdmin)



# class TopHouseAdmin(admin.ModelAdmin):
#     list_display = ["TopViewPhotoSecond","TopViewPhotoThird","TopViewPhotoFourth","TopViewPhotoFifth","TopHouseOne","TopImageOne"]
#     search_fields = ['TopHouseOne']
#     list_filter = ["TopViewPhotoSecond","TopViewPhotoThird","TopViewPhotoFourth","TopViewPhotoFifth","TopHouseOne","TopImageOne"]
# admin.site.register(TopHouse,TopHouseAdmin)

class UserSearchAdmin(admin.ModelAdmin):
    list_display = ["UserSearch"]
    search_fields = ['UserSearch']
    list_filter =["UserSearch"]
admin.site.register(Search,UserSearchAdmin)


class HouseLessorAdmin(admin.ModelAdmin):
    list_display = ["NameLessor","Sex", "PhoneNumber","Address"]
    search_fields = ['NameLessor']
    list_filter =["NameLessor","Sex", "PhoneNumber","Address"]
admin.site.register(HouseLessor,HouseLessorAdmin)



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
    list_display = ["Color","Price", "KindOfHouse","State","legalDocuments","Area","created_date","updated_date","HouseLessor","Province","District","Commune"]
    search_fields = ['KindOfHouse']
    list_filter =["Color","Price", "KindOfHouse","State","legalDocuments","Area","created_date","updated_date","HouseLessor","Province","District","Commune"]
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
    list_display = ["id","idUserLike","idHouseLike"]
    search_fields =["id","idUserLike","idHouseLike"]
    list_filter = ["id","idUserLike","idHouseLike"]
admin.site.register(UserLike,UserLikeAdmin)