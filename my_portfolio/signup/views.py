from django.shortcuts import render

from signup.models import users
import mysql.connector as sql
fn=''
ln=''
gen=''
em=''
pswd=''

# Create your views here.
def signaction(request):
    global fn,ln,gen,em,pswd
    if request.method=='POST':
        m=sql.connect(host='localhost',user='root',password='12345',database='my_portfolio')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="gender":
                gen=value
            if key=="email":
                em=value
            if key=="password":
                pswd=value

        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,gen,em,pswd)
        cursor.execute(c)
        m.commit()

        about = users(First_Name=fn,Last_Name=ln,Gender=gen,Email=em,Password=pswd)
        about.save()
        
        

        

        

    return render(request,'signup.html')    