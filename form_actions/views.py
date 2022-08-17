from django.shortcuts import render
from django.http import HttpResponse
from cryptography.fernet import Fernet #requires pip install cryptography if this gives error
# Create your views here.
DB_HOST = "localhost"
DB_NAME = "database_for_personal_page"
DB_USER = "postgres"
DB_PASS = "Aditya@1729"

import psycopg2
import psycopg2.extras #for using dict instead of list
conn = psycopg2.connect(dbname = DB_NAME , user = DB_USER , password = DB_PASS , host = DB_HOST)
cur = conn.cursor()



# cur1 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# cur.execute(sql) # gives data in list format
# cur1.execute(sql) #gives data in dict format , values are linked with column id
# data = cur1.fetchall()

def register(request) :
    name_u = request.POST['name']
    pass_u = request.POST['password']
    first_name_u = request.POST['first_name']
    user_email = request.POST['user_email']
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypt_pass = fernet.encrypt(pass_u.encode())
    sql = "select user_pass from user_det where user_email = %s and first_name = ''"
    cur.execute(sql , (user_email ,))
    # conn.commit()
    # cur.execute(sql)
    data = cur.fetchall()
    conn.close()
    print(fernet.decrypt(data[0]).decode())
    return HttpResponse("Successs")
# def register(request) :
#     return render(request , 'test.html')
