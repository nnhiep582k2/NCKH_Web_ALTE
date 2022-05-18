import imp
from sqlite3 import Cursor
from unittest import result
from xmlrpc.client import Server
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from properties.forms import PropertiesForm, SearchForm
from .models import District, ImageHouse, PropertiesEmail, Province, Search, Service
from django.db import connection
# # Create your views here.

def getfavoritesList(request):
    CE = PropertiesForm
    SF =  SearchForm
    cursor = connection.cursor()
    cursor.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id order by properties_house.Price DESC")
    # trả về dữ liệu được lưu trữ bên trong bảng dưới dạng các hàng,có thể lặp lại kết quả để có được các hàng riêng lẻ.
    results = cursor.fetchall()
    cursorSecond = connection.cursor()
    cursorSecond.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id order by properties_house.Price DESC LIMIT 1")
    resultsSecond = cursorSecond.fetchall()
    cursorThird = connection.cursor()
    cursorThird.execute("select DISTINCT properties_topprovince.FooterImage, properties_province.nameProvince, properties_house.Price from properties_topprovince LEFT join properties_province on properties_topprovince.nameProvince_id = properties_province.id left join properties_house on properties_province.id = properties_house.Province_id group by properties_province.nameProvince order by properties_house.Price DESC")
    resultsThird = cursorThird.fetchall()
    return render(request, 'properties/favoritesList.html',{'HouseList' : results , 'TopHouse':resultsSecond, 'TopProvince':resultsThird , 'CE':CE , 'SF':SF})


def getProperty(request):
    CE = PropertiesForm
    SF =  SearchForm
    cursor = connection.cursor()
    cursor.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id order by properties_house.Price DESC")
    # trả về dữ liệu được lưu trữ bên trong bảng dưới dạng các hàng,có thể lặp lại kết quả để có được các hàng riêng lẻ.
    results = cursor.fetchall()
    cursorSecond = connection.cursor();
    cursorSecond.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id order by properties_house.Price DESC LIMIT 1")
    resultsSecond = cursorSecond.fetchall()
    cursorThird = connection.cursor()
    cursorThird.execute("select DISTINCT properties_topprovince.FooterImage, properties_province.nameProvince, properties_house.Price from properties_topprovince LEFT join properties_province on properties_topprovince.nameProvince_id = properties_province.id left join properties_house on properties_province.id = properties_house.Province_id group by properties_province.nameProvince order by properties_house.Price DESC")
    resultsThird = cursorThird.fetchall()
    return render(request, 'properties/properties.html',{'HouseList' : results , 'TopHouse':resultsSecond, 'TopProvince':resultsThird , 'CE':CE ,'SF':SF})

def postProperty(request):
    if request.method == "POST":
        CE = PropertiesForm(request.POST)
        if CE.is_valid():
            CE.save()
            return HttpResponse('Send Success')
    else:
        return HttpResponse('not Post')
        
        

def getSearchList(request):
    SF =  SearchForm
    cursor = connection.cursor()
    cursor.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id order by properties_house.Price DESC")
    # trả về dữ liệu được lưu trữ bên trong bảng dưới dạng các hàng,có thể lặp lại kết quả để có được các hàng riêng lẻ.
    results = cursor.fetchall()
    cursorSecond = connection.cursor()
    cursorSecond.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id order by properties_house.Price DESC LIMIT 1")
    resultsSecond = cursorSecond.fetchall()
    cursorThird = connection.cursor()
    cursorThird.execute("select DISTINCT properties_topprovince.FooterImage, properties_province.nameProvince, properties_house.Price from properties_topprovince LEFT join properties_province on properties_topprovince.nameProvince_id = properties_province.id left join properties_house on properties_province.id = properties_house.Province_id group by properties_province.nameProvince order by properties_house.Price DESC")
    resultsThird = cursorThird.fetchall()
    return render(request, 'properties/searchList.html',{'HouseList' : results , 'TopHouse':resultsSecond, 'TopProvince':resultsThird ,'SF':SF})

def postSearchList(request):
    if request.method == "POST":
        CE = PropertiesForm
        SF = SearchForm(request.POST)
        if SF.is_valid():
            saveSF = Search (UserSearch = SF.cleaned_data['UserSearch'])
            saveSF.save()
            # để hiển thị ra trang search
            SF =  SearchForm
            cursor = connection.cursor()
            cursor.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id where properties_district.nameDistrict in ( SELECT properties_search.UserSearch FROM `properties_search` WHERE properties_search.id IN ( SELECT COUNT(properties_search.id) FROM `properties_search` ) ) LIMIT 1 ")
            # trả về dữ liệu được lưu trữ bên trong bảng dưới dạng các hàng,có thể lặp lại kết quả để có được các hàng riêng lẻ.
            results = cursor.fetchall()
            cursorSecond = connection.cursor()
            cursorSecond.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id order by properties_house.Price DESC LIMIT 1")
            resultsSecond = cursorSecond.fetchall()
            cursorThird = connection.cursor()
            cursorThird.execute("select DISTINCT properties_topprovince.FooterImage, properties_province.nameProvince, properties_house.Price from properties_topprovince LEFT join properties_province on properties_topprovince.nameProvince_id = properties_province.id left join properties_house on properties_province.id = properties_house.Province_id group by properties_province.nameProvince order by properties_house.Price DESC")
            resultsThird = cursorThird.fetchall()
            return render(request, 'properties/searchList.html',{'HouseList' : results , 'TopHouse':resultsSecond, 'TopProvince':resultsThird ,'SF':SF , 'CE':CE})
    else:
        return HttpResponse('not Post')


