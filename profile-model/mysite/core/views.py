from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User

from mysite.core.forms import SignUpForm
import os
import smtplib
import sqlite3

from mysite.core.src.convert import load
from mysite.core.src.table import TABLE
from mysite.core.src.submit import add_assignment
from mysite.core.src.test import test_Assignment
from mysite.core.src.save_pylint_score import pylint_result

@login_required
def home(request):
    return render(request, 'home.html')
    

def simple_upload(request):
    """USED_CASE_1"""
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        another_myfile = request.FILES['another_myfile']
        fs = FileSystemStorage(location='media/puzzle')
        fs.save(myfile.name, myfile)
        fs1 = FileSystemStorage(location='media/puzzle_sol')
        fs1.save(another_myfile.name, another_myfile)
        signature= request.POST.get('signature')
        class_name=another_myfile.name
        text_file = "/home/pallabeedey/Xtras/profile-model/media/puzzle_sol/"+class_name
        add_assignment(signature,text_file)
        return redirect('home')
    return render(request, 'simple_upload.html')
    
    
def signup(request):
    """USED_CASE_2"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            raw_id = form.cleaned_data.get('email')
            server.login("deypallabee@gmail.com", "mxfpjjvokodkvzcu")
            msg = ("Welcome to Kraysoft assignment tester site.\r\n\nYour registration is succesfully complete.\r\n Please save your password carefully: %s\r\n\r\n" % (raw_password))
            server.sendmail("deypallabee@gmail.com",raw_id, msg)
            server.quit()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def connect():
    conn = sqlite3.connect("\home\pallabeedey\Xtras\profile_model\db.sqlite3")
    cursor = conn.cursor()
    return cursor
    
       
def get_trainee_email_id(email_id,text):
    
    cursor = connect()
    query = """select exists(select * 
            from auth_user where email=?)
               ;"""

    cursor.execute(query,(email_id,))
    trainee_row = cursor.fetchall()
    print trainee_row

    if trainee_row == "1":
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        raw_id = form.cleaned_data.get('email')
        server.login("deypallabee@gmail.com", "mxfpjjvokodkvzcu")
        msg = ("Welcome to Kraysoft assignment tester site.\r\n\nYou are a registered candidate.\r\n Your result: %s\r\n\r\n" % (text))
        server.sendmail("deypallabee@gmail.com",email_id, msg)
        server.quit() 
            
    else:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        raw_id = form.cleaned_data.get('email')
        server.login("deypallabee@gmail.com", "mxfpjjvokodkvzcu")
        msg = ("Sorry,You are not a registered candidate .\r\n\nComplete your registration" )
        server.sendmail("deypallabee@gmail.com",email_id, msg)
        server.quit()            

  
def simple_form(request):
    """USED_CASE_3"""
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        signature = request.POST.get('signature','')
        puzzle = signature.split(".")[0]
        mail = request.POST.get('email','')
        file_saved_to="/home/pallabeedey/Xtras/profile-model/media/student_submission/"+puzzle+".py"
        if os.path.isfile(file_saved_to)==True:
            os.remove(file_saved_to)    
        fs = FileSystemStorage(location='media/student_submission')
        filename = fs.save(myfile.name, myfile)
        try:
            updated_pylint_out=pylint_result(file_saved_to)
            RESULT=test_Assignment(signature,file_saved_to,updated_pylint_out)
#            get_trainee_email_id(mail,RESULT)
            return render(request, 'result_through_mail.html',{'RESULT':RESULT})  
        except IndexError:
            RESULT ="""NO RESULT.
                    SUBMIT PROPER PYTHON FILE"""     
            return render(request, 'result_through_mail.html',{'RESULT':str(RESULT)})          
    return render(request, 'simple_form.html')
    

