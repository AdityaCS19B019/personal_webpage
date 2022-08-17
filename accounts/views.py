import email
from pyexpat.errors import messages
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User_Details
import psycopg2
from django.contrib.auth.models import User , auth
DB_NAME = "database_for_personal_page"
DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASS = "Aditya@1729"
conn = psycopg2.connect(dbname = DB_NAME , user = DB_USER , password = DB_PASS , host = DB_HOST)
# Create your views here.

def login(request) :
    data = User_Details.objects.all()
    # return HttpResponse(data[0].first_name)
    return render(request , 'login.html')

def signup(request) :
    return render(request , 'signup.html')

def register_account(request) :
    user_email = request.POST['username']
    user_pass = request.POST['pass']
    user_org = request.POST['org_name']
    first_name = request.POST['name']
    # with conn.cursor() as cur :
    #     sql = "select * from user_det where user_email = %s"
    #     cur.execute(sql , (user_email,))
    #     data = cur.fetchall()
    # if(len(data) > 0) :
    #     return redirect('..')
    # else :
    #     with conn.cursor() as cur :
    #         sql = "insert into user_det values(%s , %s , %s , %s)"
    #         cur.execute(sql , (user_email , user_pass , first_name , user_org))
    #         conn.commit()
    #     return redirect('/page')
    if User.objects.filter(email = user_email).exists() :
        messages.info(request , 'Email already exists')
        return redirect('/')
    else :
        user_new = User.objects.create_user(username = user_email , email = user_email , first_name = first_name , password = user_pass)
        user_new.save()
        new_obj = User_Details(first_name = first_name , email_address = user_email , password = user_pass , Org = user_org)
        new_obj.save()
        return redirect('../skills')
        

def Authenticate(request) :
    user_name = request.POST['user_name']
    user_pass = request.POST['user_pass']
    # with conn.cursor() as cur :
    #     sql = "select * from user_det where user_email = %s and user_pass = %s"
    #     cur.execute(sql , (user_name , user_pass))
    #     data = cur.fetchall()
    # if(len(data) > 0) :
    #     res = redirect('../page')
    #     res.set_cookie('user' , data[0][2])
    #     return res
    # else :
    #     return render(request , 'login.html' , {"invalid_cred" : "Yes"})
    user = auth.authenticate(username = user_name , password = user_pass)
    if user is not None :
        return redirect('../view/skills')
    else :
        messages.info(request , 'invalid credentials')
        return redirect('/')

def logout(request) :
    auth.logout(request)
    return redirect('')

