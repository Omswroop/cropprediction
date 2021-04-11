from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from tablib import Dataset
from rapidconnect import RapidConnect    #to use a rapid api
import pprint       #pretty print a json
import requests     #access apis
import datetime     #get current date and time
import statistics   #calculate mean

count=0


# =======================================FOR WORK USING THE API OF WEATHER AND SOIL DETAILS=====================================


#to get the current temperature and weather information
def api_for_weather(place):
    
    result=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+place+'&appid=486d45a8672282f2149439e3fc7bfe40')
    data=result.json()
    return data

def api_for_weather_2(lat,longi):
    
    result=requests.get('http://api.openweathermap.org/data/2.5/weather?lat='+str(lat)+'&lon='+str(longi)+'&appid=486d45a8672282f2149439e3fc7bfe40')

    data=result.json()

    return data


def calculate_coord(data):
        try:

            coord=[data['coord']['lat'],data['coord']['lon']]
            return coord
        except Exception as e:
            print('coord returned method value',e)




#to get the information about the soil of the region or district

def get_soil_info(place, coord):
    def api_for_geocon(place):
        now = datetime.datetime.now()
        start_date = str(now.year) + '-' + str(now.month - 1) + '-' + str(now.day)
        end_date = str(now.year) + '-' + str(now.month + 1) + '-' + str(now.day)
        #    result=requests.get('https://api.weatherbit.io/v2.0/history/agweather?lat='+str(coord[0])+'&lon='+str(coord[1])+'&start_date='+start_date+'&end_date='+end_date+'&key=283a77fe5cbe46718430e4d5418be6c1')
        result = requests.get('https://api.weatherbit.io/v2.0/forecast/agweather?lat=' + str(coord[0]) + '&lon=' + str(
            coord[1]) + '&key=3d6dc8552cb74208866db831e6cc7724')
        data = result.json()
        return data

    def cal_mean(data):
        mean_vals = []
        summ_vals_dict = {}
        keywords = ['bulk_soil_density', 'skin_temp_avg', 'precip', 'specific_humidity', 'pres_avg', 'soilt_0_10cm',
                    'soilm_0_10cm', 'wind_10m_spd_avg']
        for k in keywords:
            summ = 0
            for i in range(0, 9):
                summ += data['data'][i][k]
            summ_vals_dict[k] = summ
        for key in summ_vals_dict:
            summ_vals_dict[key] = (summ_vals_dict[key]) / 9

        return summ_vals_dict

    #daaa = api_for_geocon(place)
    #return cal_mean(daaa)


def geocoding(place):
    coord=[]
    result=requests.get('https://api.opencagedata.com/geocode/v1/json?q='+place+'&key=217e890a4fed4cc780a83c8cce2abf14')
    data=result.json()
    coord.append(data['results'][0]['geometry']['lat'])
    coord.append(data['results'][0]['geometry']['lng'])
    return (coord,data)

def print_temp_details(data):
       
       temp=precise((data['main']['temp']-273.15),1)
       wind=precise((data['wind']['speed']*1.60934),2)
       dire=precise((data['wind']['deg']),2)

       values={
               'temperature':str(temp),
               'latitude':str(data['coord']['lat']),
               'longitude':str(data['coord']['lon']),
               'humidity':str(data['main']['humidity'])+'%',
               'pressure':str(data['main']['pressure'])+'hPa',
               'windspeed':str(wind)+'km/h',
               'winddirection':str(dire)
            #    'visibility':str(data['visibility'])+' metres',
               }
       
       return values



def precise(data,point):
    if type(data)==dict:
        a={}
        for i in data:
            if type(data[i])==float:
                data[i]=round(data[i],point)
                a[i]=data[i]
            else:
                a[i]=data[i]
        return a
    if type(data)==float:
        return round(data,point)
    
    if type(data)==list:
        a=[]
        for i in data:
            if type(i)==float:
                i=round(i,point)
                print(i)
                a.append(i)
            else:
                a.append(i)
        return a


def categorize(val1,val2):
    if val1>val2:
        pp=(val2/val1)
        return pp
    else:
        return 1


def finding_subs(p,crop1):
    d={}
    for i in p.values():
        crop=i['crop']
        area=i['district']

        first_datset=pred_one.objects.filter(crop=crop)
        sec_datset=prod_area.objects.filter(crop=crop,district=area)
        third_datset=pred_three.objects.filter(crop=crop)
        
        if first_datset.count()!=0 and sec_datset.count()!=0 and third_datset.count()!=0:

            sec_val=list(sec_datset.values())[0] 
            val1=sec_val['org_val']
            val2=sec_val['pred_val']

            p1=categorize(val1,val2)

    #handing the  Gross_Production_Value_current_million_US_dollar factor
            
            fir1=list(first_datset.values())[0]['Gross_Production_Value_constant_2004_2006_million_US_dollar']
            fir2=list(first_datset.values())[0]['org_mean_Gross_Production_Value_constant_2004_2006_million_US_dollar']

            p2=categorize(fir1,fir2)
            
    # handling the imports exports and production factors
            firr1=list(third_datset.values())[0]

            val1_1=firr1['exports']
            val2_2=firr1['imports']
            val3_3=firr1['production']

            val1_1_p=firr1['exports_mean']
            val2_2_p=firr1['imports_mean']
            val3_3_p=firr1['production_mean']

            p3=categorize(val1_1,val1_1_p)
            p4=categorize(val2_2,val2_2_p)
            p5=categorize(val3_3,val3_3_p)

            mean_final=(p1+p2+p3+p4+p5)/5

            d[crop]=mean_final
    
    else:
        d[crop]='no db exist for the crop'

    
    e={}
    for i in d:
        if type(d[i])!=str and i!=crop1:
            e[i]=d[i]
    return e


# ==========================================MAIN DJANGO VIEWS=============================================



class TemplateView(generic.TemplateView):
    template_name='cultivo_main/login.html'

class TemplateView2(generic.TemplateView):
    template_name='cultivo_main/contact.html'

class TemplateView3(generic.TemplateView):
    template_name='cultivo_main/story.html'

class TemplateView4(generic.TemplateView):
    template_name='cultivo_main/services.html'




def work(request):
    
    if request.method=='POST':
        area=request.POST['area'].upper()   # here we are taken area
        crop=request.POST['crop'].capitalize() # and perticuler crop

        if (prod_area.objects.filter(crop=crop,district=area)).count()>=1: ###if the crop and area fond 
            #getting the atmosphere information
            data=api_for_weather(area)    ###gettting the weather details of the area
            print('api weather data is',data)
            #getting the json details of the atmosphere
            coord,data=geocoding(area)
            print("geocoding area",coord)
            ##getting the same weather info

            if data['status']['code']==200 and data['status']['message']=='OK':
                    data=api_for_weather_2(coord[0],coord[1])  ###here we are taking langitude and latitude
            else:
                    return render(request,'cultivo_main/error.html')
            
            
            coord=calculate_coord(data) ###
            print('coord',coord)
            #extracting the coordinates
            #soil_info=get_soil_info(area,coord)
            #dictionary cointaining soil info
           # print("Soil info",soil_info)
            temp_det=print_temp_details(data)
            print('tempo',temp_det)
            #converting all the details into proper units for printing
            #print('temp',temp_det)
            #soil_info=precise(soil_info,2)
            # temp_det_2=precise(temp_det,1)
            #print('soil',soil_info)
            # filtering the objects

            first_datset=pred_one.objects.filter(crop=crop) ###second datasetoutput values
            sec_datset=prod_area.objects.filter(crop=crop,district=area)
            ####first dataset values
            third_datset=pred_three.objects.filter(crop=crop)
            ###third dataset values


            # #gettting dictionaries out of the returned values

            fir=list(first_datset.values())[0]['Gross_Production_Value_constant_2004_2006_million_US_dollar']
            print('fir',fir)
            first_value={'Gross_Production_Value_constant_2004_2006_million_US_dollar':round(fir,2)}
            print('first_value',first_value)
            #making round figure

            sec_values=list(sec_datset.values())[0]
            del sec_values['id']
            del sec_values['org_val']

            third_values=list(third_datset.values())[0]
            del third_values['id']
            del third_values['crop']
            print('third_values',third_values)


            final_dict={**sec_values,**third_values,**first_value}
            
            # finding the final % success and failure

    # handling prod_area factor
            sec_val=list(sec_datset.values())[0]
            val1=sec_val['org_val']
            val2=sec_val['pred_val']

            p1=categorize(val1,val2)
            print('p1',p1)

    #handing the  Gross_Production_Value_current_million_US_dollar factor
            
            fir1=list(first_datset.values())[0]['Gross_Production_Value_constant_2004_2006_million_US_dollar']
            fir2=list(first_datset.values())[0]['org_mean_Gross_Production_Value_constant_2004_2006_million_US_dollar']

            p2=categorize(fir1,fir2)
            
    # handling the imports exports and production factors
            firr1=list(third_datset.values())[0]

            val1_1=firr1['exports']
            val2_2=firr1['imports']
            val3_3=firr1['production']

            val1_1_p=firr1['exports_mean']
            val2_2_p=firr1['imports_mean']
            val3_3_p=firr1['production_mean']

            p3=categorize(val1_1,val1_1_p)
            p4=categorize(val2_2,val2_2_p)
            p5=categorize(val3_3,val3_3_p)

            mean_final=(p1+p2+p3+p4+p5)/5
            print('mean final',mean_final)
            # final_outcome=mean_final
            # final_outcome=round(mean_final,)
            final_outcome=(round(mean_final,5))*100
            final_outcome = float("{0:.3f}".format(final_outcome))
            final_main=str(final_outcome).split('.')[0]
            final_dec=str(final_outcome).split('.')[1]


            obj=prod_area.objects.filter(district=area)
            d=finding_subs(obj,crop) 
            dd=list(d[i] for i in d)
            dd=list(map(float,dd))
            dd.sort(reverse=True)
            fin_dict={}
            for i in dd:
                for j in d:
                    if float(d[j])==i:
                        fin_dict[j]=i

            for i in fin_dict:
                fin_dict[i]=round(fin_dict[i],5)*100
                fin_dict[i]=float("{0:.3f}".format(fin_dict[i]))
               
            


            return render(request,'cultivo_main/parallax.html',{'first':first_value,'second':sec_values,'third':third_values, 'temp_det':temp_det,'final':final_dict,'soil':788.9,'finalout_main':final_main,'finalout_dec':final_dec,'ff':fin_dict})
        else:
            return render(request,'cultivo_main/new.html',{'crop':crop})


            
    else:
        raise Http404("You are unauthorised to access this page")
        
        # =====================================================for making the final prediction====================================
        


# ===================================================FOR IMPORTING CSV FILES TO DJANGO DBS============================================


def simple_upload(request):
    if request.method == 'POST':
        value=True

        res = predone()
        value=vv(res)

        if value==False:
            res = prodarea()
            value=vv(res)
        
        if value==False:
            res = one()
            value=vv(res)

        if value==False:
            res = two()
            value=vv(res)

        if value==False:
            res = three()
            value=vv(res)
        
        if value==False:
            res = pred_three()
            value=vv(res)
       
    return render(request, 'core/simple_upload.html')


def vv(request,res):
    dataset = Dataset()
    new = request.FILES['myfile']

    imported_data = dataset.load(new.read())
    result = res.import_data(dataset, dry_run=True)  # Test the data import

    if not result.has_errors():
        value=True
        res.import_data(dataset, dry_run=False)  # Actually import now
    
    else:
        value=False
    return value


def input(request):
    return  render(request,'cultivo_main/footer.html')

def login1(request):
    global loginFlag, loginUser
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)
        message = ""

        if len(Users.objects.filter(emp_id=username)) == 0:
            message = message + "No Matching Accounts Found"
        else:
            pass_hash = str(Users.objects.filter(emp_id=username)[0]).split(";")[4]
            decrypt_text = pass_hash
            if password == decrypt_text:
                message = message + "Welcome to the Home Page"
                loginFlag = True
                loginUser = username
                print(loginUser)
                return render(request, 'cultivo_main/footer.html')
            else:
                message = message + "Wrong Password Entered"

        print(message)
        context = {"message": message}
        return render(request, 'cultivo_main/UserFailure.html', context)



    return render(request,'cultivo_main/login.html')


def register(request):
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()

        emp_id = request.POST['emp_id']
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']

        ques_1_id = request.POST['ques_1_id']
        ans_1 = request.POST['ans_1']
        ques_2_id = request.POST['ques_2_id']
        ans_2 = request.POST['ans_2']
        gender = request.POST['gender']
        phone = request.POST['phone']
        repeat_password = request.POST['repeat_password']
        print(emp_id, name, password, email, ques_1_id, ans_1, ques_2_id, ans_2, gender, phone, repeat_password)
        count = 0
        message = ""
        searchObject = Users.objects.all()
        flag = 1
        for i in range(len(searchObject)):
            lst = str(searchObject[i]).split(";")
            print(lst[0], emp_id)
            if lst[0] == emp_id:
                message = message + "Employee already exists.\n"
                flag = 0
                break
        if flag == 1:
            count = count + 1

        if password == repeat_password:
            if len(password) > 6:
                flag1, flag2, flag3 = 0, 0, 0
                for i in range(len(password)):
                    ele = ord(password[i])
                    if ele > 96 and ele < 123:
                        flag1 = 1
                    elif ele > 47 and ele < 58:
                        flag2 = 1
                    elif ele > 64 and ele < 91:
                        flag3 = 1
                if flag1 == 1 and flag2 == 1 and flag3 == 1:
                    count = count + 1
                else:
                    message = message + "Re-enter the Password.\n"
        else:
            message = message + "Passwords does not match.\n"

        print(count)
        if count == 2:
            raw_text = password
            encrypt_text = raw_text
            Users(emp_id=emp_id,
                     name=name,
                     password=encrypt_text,
                     email=email,
                     ques_1_id=ques_1_id,
                     ans_1=ans_1,
                     ques_2_id=ques_2_id,
                     ans_2=ans_2,
                     gender=gender,
                     phone=phone).save()

            message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}
        return render(request, 'cultivo_main/register.html', context)

    else:
        message = "Welcome To Registration Page"
        context = {"message": message}
        return render(request, 'cultivo_main/register.html', context)