# chatbot/views.py
import time
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile
from .forms import RegistrationForm
from .chatbot import FinancialBot
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import random
import json

from .chatbot_util1 import *
from .chatbot_util2 import *
from .chatbot_util3 import *


def authentication_register(request):
    if request.method =='POST':
        fname = request.POST['fullName']
        username =request.POST['userName']
        email = request.POST['email']
        pass1 = request.POST['newPassword']
        pass2 = request.POST['conPassword']

        if User.objects.filter(username=username):
            messages.error(request,"Username already Exist! Please use another Username")
            return redirect('authentication-register')
        if User.objects.filter(email=email):
            messages.error(request,"email already Exist! Please use another email")
            return redirect('authentication-register')
        if pass1 != pass2:
            messages.error(request,"Your password didn't Match")
            return redirect('authentication-register')
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.save()
        
        messages.success(request,"Account created successfully")


        return redirect('authentication-login')


    return render(request,'registration/authentication-register.html')



def authentication_login(request):
    
    if request.method =='POST':
        uname =request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username=uname,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('chat')
        
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect('authentication-login')
        


    return render(request,'registration/authentication-login.html')



def authentication_signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('authentication-login',)



def chatbot_view(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')

        data = {
            "choice": "",
            "current_fun": "",
            "total_income": 0,
            "ent_expense": 0,
            "house_expense": 0,
            "total_expense": 0,
            "investment_term": ""
        }

        past_data = read_json()

        if choice:
            data['choice'] = choice
          # Retrieve message input

        if not choice:
            request_body_bytes = request.body
            request_body_string = request_body_bytes.decode('utf-8')
            json_data = json.loads(request_body_string)
            message = json_data.get('message')

            if message == 'Q':
                write_json(data)
                return JsonResponse({"response":"OK"})
            

        if choice == "1":
            data['current_fun'] = "ASK_INCOME"
            response = ask_total_income()
        
        if choice == "2":
            data['current_fun'] = "CHOICE_TWO"
            response = "Ask me a general financial Question..."

        if choice == "3":
            data['current_fun'] = "CHOICE_THREE"
            response = "For how long do you plan to invest (long term/short term)?"
        
        if past_data["investment_term"] == "" and past_data["choice"] == "3" and past_data["current_fun"] == "CHOICE_THREE" :
            data["investment_term"] = message
            data["current_fun"] = "ASK_RISK"
            response = "How comfortable are you with taking risks (low/high)?"
        
        if past_data["current_fun"] =="ASK_RISK":
            data = {
            "choice": "",
            "current_fun": "",
            "total_income": 0,
            "ent_expense": 0,
            "house_expense": 0,
            "total_expense": 0,
            "investment_term": ""
            }
            investment_term = past_data['investment_term']
            risk = message

            response = provide_investment_advice(investment_term, risk)


        if past_data["choice"] == "2" and past_data['current_fun'] == "CHOICE_TWO":
            if message != "Q":
                data['current_fun'] = "CHOICE_TWO"
                data["choice"] = '2'
                response = initiate_general_financial_questions(message) + "\n\n" + "Press Q to exit"
            else:
                response = "Wish you financially healthy future! bye."

        if past_data["current_fun"] == "ASK_INCOME":
            data['current_fun'] = "ASK_EXPENSES"
            data["total_income"] = int(message)
            response = ask_total_expenses()

        if past_data["current_fun"] == "ASK_EXPENSES":
            data['current_fun'] = "ASK_HOUSE_EXPENSES"
            data['total_income'] = past_data['total_income']
            data['house_expense'] = int(message)
            response = ask_house_expenses()

        if past_data["current_fun"] == "ASK_HOUSE_EXPENSES":
            data['current_fun'] = "ASK_ENTERTAINMENT_EXPENSES"
            data['total_income'] = past_data['total_income']
            data['house_expense'] = past_data['house_expense']
            data['ent_expense'] = int(message)
            response = ask_entertainment_expenses()
        
        if past_data["current_fun"] == "ASK_ENTERTAINMENT_EXPENSES":
            data['current_fun'] = "CHECK_EXPENSES"
            total_expense = past_data['house_expense'] +  past_data['ent_expense']
            ent_expense = past_data['ent_expense']
            findings = check_entertainment_expenses(ent_expense, total_expense)
            total_income = past_data['total_income']
            suggestions = calculate_suggested_expenditure(total_income)
            response = findings + suggestions


        if past_data["current_fun"] == "CHECK_EXPENSES" and past_data['choice'] != "2":
            data = {
            "choice": "",
            "current_fun": "",
            "total_income": 0,
            "ent_expense": 0,
            "house_expense": 0,
            "total_expense": 0,
            "investment_term": ""
        }

        write_json(data)

        # Return final JSON response
        return JsonResponse({'response': response})
    
    elif request.method == 'GET':
        # Handle GET requests if needed
        return render(request, 'chatbot/a_chat.html')





#NOTE: HELPER FUNCTIONS
FILE_PATH = 'chatbot/data.json'
def read_json():
    """
    Read JSON data from a file.
    
    Args:
        file_path (str): The path to the JSON file.
    
    Returns:
        dict: The JSON data read from the file.
    """
    with open(FILE_PATH, 'r') as file:
        data = json.load(file)
    return data



def write_json(data):
    """
    Write JSON data to a file.
    
    Args:
        data (dict): The JSON data to be written to the file.
        file_path (str): The path to the JSON file.
    """
    print(FILE_PATH)
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)
        