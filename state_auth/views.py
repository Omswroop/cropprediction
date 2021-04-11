from django.shortcuts import render,redirect

from .forms import  Auth_Form
from .forms import Second_Form
from .forms import Auth_LoginForm
from .models import  Database2
from .models import  FirstDB1
from cultivo_main.models import prod_area
from cultivo_main.models import pred_one
from cultivo_main.models import pred_three
from .forms import First_Form
from .forms import Third_Form

# Create your views here.
def index(request):
    if request.method == 'POST':
         form1 = Auth_Form(request.POST)
         if form1.is_valid():
           new_data = Database2( email=request.POST['email'],password=request.POST['password'],
                             username=request.POST['username'],
                            department=request.POST['department'], Pancard=request.POST['Pancard'],
                            crop=request.POST['crop'], Address=request.POST['Address'],
                            Gender=request.POST['Gender'], phone=request.POST['phone']
                            )
           new_data.save()
           return redirect('login')
         else:
             return render(request, 'state_auth/register.html',
                           {'form1': form1})
    else:
          form1 = Auth_Form()
          context = {'form1': form1}
          return render(request, 'state_auth/register.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("email is", email)
        print("pass is", password)
        d = Database2()
        userdetails = d.validteuser(email=email,password=password)
        #print(userdetails.Email)
        print(userdetails)
        if userdetails =='yes':
            print('Successfull Login')
            return render(request, 'state_auth/home.html')
        else:
            print('Failure Login')
            return render(request, 'state_auth/Failurelogin.html')

    form2=Auth_LoginForm()
    context={'form2':form2}
    return  render(request,'state_auth/index.html',context)


def first(request):
    if request.method == 'POST':
        regform = First_Form(request.POST)
        if regform.is_valid():
            new_data = prod_area(state=request.POST['State'],
                               district=request.POST['District'],
                               crop=request.POST['Crop'],
                                 org_val=request.POST['Org'],
                                 pred_val=request.POST['Pred'],

                                 )
            new_data.save()
            return redirect('second')

    else:

          form3=First_Form()
          context={'form3':form3}
          return render(request, 'state_auth/first.html',context)




def second(request):
    if request.method == 'POST':
        regform = Second_Form(request.POST)
        if regform.is_valid():
            new_data = pred_one(
                                 crop=request.POST['Crop'],
                Gross_Production_Value_constant_2004_2006_1000_dollar=request.POST['Gross_Production_Value_constant_2004_2006_1000_dollar'],
                Net_Production_Value_constant_2004_2006_1000_dollar=request.POST['Net_Production_Value_constant_2004_2006_1000_dollar'],
                Gross_Production_Value_current_million_SLC=request.POST[
                    'Gross_Production_Value_current_million_SLC'],
                Gross_Production_Value_constant_2004_2006_million_SLC=request.POST[
                    'Gross_Production_Value_constant_2004_2006_million_SLC'],
                Gross_Production_Value_current_million_US_dollar=request.POST[
                    'Gross_Production_Value_current_million_US_dollar'],
                Gross_Production_Value_constant_2004_2006_million_US_dollar=request.POST[
                    'Gross_Production_Value_constant_2004_2006_million_US_dollar'],
                org_mean_Gross_Production_Value_constant_2004_2006_million_US_dollar=request.POST[
                    'org_mean_Gross_Production_Value_constant_2004_2006_million_US_dollar']


            )
            new_data.save()
            return redirect('third')

    else:
       form4=Second_Form()
       context={'form4':form4}
       return render(request,'state_auth/second.html',context)




def third(request):
    if request.method == 'POST':
        regform = Third_Form(request.POST)
        if regform.is_valid():
            new_data = pred_three(
                crop=request.POST['crop'],
                                 imports=request.POST['imports'],
                                 exports=request.POST['exports'],
                production=request.POST['production'],
                imports_mean=request.POST['imports_mean'],
                exports_mean=request.POST['exports_mean'],
                production_mean=request.POST['production_mean']

                                 )
            new_data.save()
            return render(request, 'state_auth/success.html')


    else:

       forms5=Third_Form()
       context={'forms5':forms5}
       return render(request,'state_auth/third.html',context)