from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views import View

from .forms import IndexSendForm
from .models import IndexSendEmail
# Create your views here.

class homeIndex(View):
    def get(self , request):
        CE = IndexSendForm
        cursor = connection.cursor()
        cursor.execute("select * from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id order by properties_house.Price DESC")
        # trả về dữ liệu được lưu trữ bên trong bảng dưới dạng các hàng,có thể lặp lại kết quả để có được các hàng riêng lẻ.
        results = cursor.fetchall()
        cusorSecond = connection.cursor()
        cusorSecond.execute("select * from contact_feedback limit 3")
        resultSecond = cusorSecond.fetchall()
        return render(request, 'home/index.html',{'HouseList' : results , 'FeedBackLists' : resultSecond , 'CE': CE})

    def post(self,request):
        if request.method == "POST":
            CE = IndexSendForm(request.POST)
            if CE.is_valid():
                saveCE = IndexSendEmail ( Email = CE.cleaned_data['Email'])
                saveCE.save()
                return HttpResponse('Send Success')
        else:
            return HttpResponse('not Post')



def create(self,request):
    return HttpResponse('123')