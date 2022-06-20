import imp
from sqlite3 import Cursor
from unittest import result
from xmlrpc.client import Server
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View

from properties.forms import PropertiesForm, SearchForm, contactMe_Form
# import model sang
from .models import LIKE_CHOICRS, District, House, ImageHouse, PropertiesEmail, Province, Search, Service, contactMe
from django.db import connection
# # Create your views here.

def getfavoritesList(request):
    # lấy từ form.
    CE = PropertiesForm
    SF =  SearchForm
    qs  = House.objects.all()
    
    # gọi connect.cursor () để lấy một đối tượng con trỏ
    cursor = connection.cursor()
    # gọi cursor.execute (sql) để thực thi truy vấn SQL 
    cursor.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  order by properties_house.Price DESC")
    # cursor.fetchall () để trả về các hàng kết quả và gán cho results
    results = cursor.fetchall()
    
    
    cursorSecond = connection.cursor();
    cursorSecond.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  order by properties_house.Price DESC LIMIT 1")
    resultsSecond = cursorSecond.fetchall()
    cursorThird = connection.cursor()
    cursorThird.execute("select DISTINCT properties_topprovince.FooterImage, properties_province.nameProvince, properties_house.Price from properties_topprovince LEFT join properties_province on properties_topprovince.nameProvince_id = properties_province.id left join properties_house on properties_province.id = properties_house.Province_id group by properties_province.nameProvince order by properties_house.Price DESC")
    resultsThird = cursorThird.fetchall()
    return render(request, 'properties/favoritesList.html',{'HouseList' : results , 'TopHouse':resultsSecond, 'TopProvince':resultsThird , 'CE':CE , 'SF':SF,'qs':qs})


def getProperty(request):
    CE = PropertiesForm
    SF =  SearchForm
    qs  = House.objects.all()
    cursor = connection.cursor()
    cursor.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  order by properties_house.Price DESC")

    results = cursor.fetchall()
    cursorSecond = connection.cursor();
    cursorSecond.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  order by properties_house.Price DESC LIMIT 1")
    resultsSecond = cursorSecond.fetchall()
    cursorThird = connection.cursor()
    cursorThird.execute("select DISTINCT properties_topprovince.FooterImage, properties_province.nameProvince, properties_house.Price from properties_topprovince LEFT join properties_province on properties_topprovince.nameProvince_id = properties_province.id left join properties_house on properties_province.id = properties_house.Province_id group by properties_province.nameProvince order by properties_house.Price DESC")
    resultsThird = cursorThird.fetchall()
    return render(request, 'properties/properties.html',{'HouseList' : results , 'TopHouse':resultsSecond, 'TopProvince':resultsThird , 'CE':CE ,'SF':SF,'qs':qs})

def postProperty(request):
    # nếu người dùng gửi có mothod là POST
    if request.method == "POST":
        # thì gán CE = 
        CE = PropertiesForm(request.POST)
        # nếu CF thỏa mãn các yêu cauafu bên model (độ dài,...) thì 
        if CE.is_valid():
            # thì lưu lại
            CE.save()
            return HttpResponse('Send Success')
    else:# nếu ko phải method POST 
        return HttpResponse('not Post')
        
        

def getSearchList(request):
    SF =  SearchForm
    qs  = House.objects.all()
    cursor = connection.cursor()
    cursor.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  order by properties_house.Price DESC")

    results = cursor.fetchall()
    cursorSecond = connection.cursor();
    cursorSecond.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  order by properties_house.Price DESC LIMIT 1")
    resultsSecond = cursorSecond.fetchall()
    cursorThird = connection.cursor()
    cursorThird.execute("select DISTINCT properties_topprovince.FooterImage, properties_province.nameProvince, properties_house.Price from properties_topprovince LEFT join properties_province on properties_topprovince.nameProvince_id = properties_province.id left join properties_house on properties_province.id = properties_house.Province_id group by properties_province.nameProvince order by properties_house.Price DESC")
    resultsThird = cursorThird.fetchall()
    return render(request, 'properties/searchList.html',{'HouseList' : results , 'TopHouse':resultsSecond, 'TopProvince':resultsThird ,'SF':SF,'qs':qs})

def postSearchList(request):
    # nếu là method POST thì
    if request.method == "POST":
        # lấy CE
        CE = PropertiesForm
        SF = SearchForm(request.POST)
        qs  = House.objects.all()
        # hỏi xem nó có đúng các điều kiện như là độ dài,... thì 
        if SF.is_valid():
            SF.save()
            # để hiển thị ra trang search
            SF =  SearchForm
            cursor = connection.cursor()
            cursor.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond,properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id join properties_country on properties_house.Country_id = properties_country.id join properties_features on properties_features.id = properties_house.Features_id  where properties_district.nameDistrict in ( SELECT properties_search.UserSearch FROM `properties_search` WHERE properties_search.id IN ( SELECT COUNT(properties_search.id) FROM `properties_search` ) ) LIMIT 1 ")
        
            results = cursor.fetchall()
            cursorSecond = connection.cursor()
            cursorSecond.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  order by properties_house.Price DESC LIMIT 1")
            resultsSecond = cursorSecond.fetchall()
            cursorThird = connection.cursor()
            cursorThird.execute("select DISTINCT properties_topprovince.FooterImage, properties_province.nameProvince, properties_house.Price from properties_topprovince LEFT join properties_province on properties_topprovince.nameProvince_id = properties_province.id left join properties_house on properties_province.id = properties_house.Province_id group by properties_province.nameProvince order by properties_house.Price DESC")
            resultsThird = cursorThird.fetchall()
            return render(request, 'properties/searchList.html',{'HouseList' : results , 'TopHouse':resultsSecond, 'TopProvince':resultsThird ,'SF':SF , 'CE':CE,'qs':qs})
    else:
        return HttpResponse('not Post')

def like_user(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = House.objects.get(id = post_id)
        
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created =LIKE_CHOICRS.object.get_or_create(user = user, post_id = post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
    return redirect('properties:getProperties')


def Details_house(request, id):
    CE = PropertiesForm
    SF =  SearchForm
    CTM = contactMe_Form
    # user = request.user
    pD = House.objects.get(id = id)
    DT = House.objects.all()
    cursor = connection.cursor()
    cursor.execute("select properties_house.id,properties_house.linkStreetView,properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id ")
    results = cursor.fetchall()
    
    
    cursorThird = connection.cursor()
    cursorThird.execute("select properties_houselessor.id,properties_houselessor.NameLessor,COUNT(properties_house.id),properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook from properties_houselessor join properties_house on properties_houselessor.id = properties_house.HouseLessor_id GROUP by properties_houselessor.id ORDER by COUNT(properties_house.id) ASC LIMIT 3")

    resultsThird = cursorThird.fetchall()
    
    cursorFourth = connection.cursor()
    cursorFourth.execute("select properties_house.KindOfHouse,COUNT(properties_house.KindOfHouse) from properties_house GROUP by properties_house.KindOfHouse")

    resultsFourth = cursorFourth.fetchall()
    
    cursorFifth = connection.cursor()
    cursorFifth.execute("select properties_house.id,properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  LIMIT 4")

    resultsFifth = cursorFifth.fetchall()
    
    return render(request, 'properties/detail.html',{'HouseList' : results , 'TopAgents':resultsThird,'KindOfHouse':resultsFourth,'FourHouse':resultsFifth ,'SF':SF , 'CE':CE,'CTM':CTM,'pD':pD,'DT':DT})


def PostDetails_house(request):
    if request.method == "POST":
        CTM = contactMe_Form(request.POST)
        if CTM.is_valid():
            CTM.save()
            return HttpResponse('FeedBack Success')
        else:
            return HttpResponse('not Post')
        
        
def SubDetails_house(request, id):
    CE = PropertiesForm
    SF =  SearchForm
    CTM = contactMe_Form
    # user = request.user
    DT = House.objects.get(id = id)
    cursor = connection.cursor()
    cursor.execute("select properties_house.id,properties_house.linkStreetView,properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id ")
    results = cursor.fetchall()
    
    
    cursorThird = connection.cursor()
    cursorThird.execute("select properties_houselessor.id,properties_houselessor.NameLessor,COUNT(properties_house.id),properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook from properties_houselessor join properties_house on properties_houselessor.id = properties_house.HouseLessor_id GROUP by properties_houselessor.id ORDER by COUNT(properties_house.id) ASC LIMIT 3")

    resultsThird = cursorThird.fetchall()
    
    cursorFourth = connection.cursor()
    cursorFourth.execute("select properties_house.KindOfHouse,COUNT(properties_house.KindOfHouse) from properties_house GROUP by properties_house.KindOfHouse")

    resultsFourth = cursorFourth.fetchall()
    
    cursorFifth = connection.cursor()
    cursorFifth.execute("select properties_house.id,properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond, properties_house.id from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_features.id = properties_house.Features_id  LIMIT 4")

    resultsFifth = cursorFifth.fetchall()
    
    return render(request, 'properties/detailItem.html',{'HouseList' : results , 'TopAgents':resultsThird,'KindOfHouse':resultsFourth,'FourHouse':resultsFifth ,'SF':SF , 'CE':CE,'CTM':CTM,'DT':DT})
