from django.shortcuts import render, redirect
from django.contrib import messages
from Accounts.models import Profile
from config import emailID, password
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pickle


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        message = MIMEMultipart()

        message['from'] = "Mental Health Support Team"
        message['to'] = str(request.user.email)
        message['subject'] = "Assistance Required !"
        message.attach(MIMEText(f'''
                                Hello, {request.user}, 

                                We will get back in touch with you!
                                name : {name} 
                                email : {email} 
                                msg : {msg} 

                                Query Submitted Successfully!                
                                ''')
                       )
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(emailID, password)
            smtp.send_message(message)

        messages.add_message(request, messages.SUCCESS,
                             'Query submitted successfully!')

    return render(request, 'contact.html')


def health_test(request):
    score = 0
    try:
        if request.method == "POST":
            age = request.POST.get('age')
            gender = request.POST.get('g')
            q1 = request.POST.get('q1')
            q2 = request.POST.get('q2')
            q3 = request.POST.get('q3')
            q4 = request.POST.get('q4')
            q5 = request.POST.get('q5')
            q6 = request.POST.get('q6')
            q7 = request.POST.get('q7')
            q8 = request.POST.get('q8')
            q9 = request.POST.get('q9')
            q10 = request.POST.get('q10')
            q11 = request.POST.get('q11')
            q12 = request.POST.get('q12')
            q13 = request.POST.get('q13')
            q14 = request.POST.get('q14')
            q15 = request.POST.get('q15')
            q16 = request.POST.get('q16')
            q17 = request.POST.get('q17')
            q18 = request.POST.get('q18')
            q19 = request.POST.get('q19')
            q20 = request.POST.get('q20')
            datapts = [age, gender, q1, q2, q3, q4, q5, q6, q7, q8, q9,
                       q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]
            data = [int(x) for x in datapts if x.isdigit()]
            score = data.count(1)
            score = score * 10

            if not data:
                messages.add_message(
                    request, messages.ERROR, 'Invalid input. Please enter numeric values.')
            else:
                model_loaded = pickle.load(open('./MHSModel.pkl', 'rb'))
                prediction = model_loaded.predict([data])

                if prediction[0] == 1 and score >= 70:
                    messages.add_message(
                        request, messages.ERROR, f'Your test results are positive! Score : {score}')

                    return redirect('dashboard')

                else:
                    messages.add_message(
                        request, messages.SUCCESS, f'Your test results are negative! Score : {score}')
                    return redirect('home')

        else:
            return render(request, 'health_test.html')

    except Exception as e:
        return redirect('health_test')

    return render(request, 'health_test.html')


def chatbot(request):
    return render(request, 'chatbot.html')


def video_conference(request):
    specialists = Profile.objects.filter(catagory="Specialist")
    spEmails = ', '.join([x.user.email for x in specialists])

    message = MIMEMultipart()

    message['from'] = "Mental Health Support Team"
    message['to'] = spEmails
    message['subject'] = "Assistance Required !"
    message.attach(MIMEText(f"""
                            Hello, {request.user}, 
                            \nKindly wait, the specialist is connecting... 
                            \nJoin here at, 
                            \nRoom Link : https://mhsupport.azurewebsites.net/video_conference/?roomID=100                 
                            """)
                   )
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(emailID, password)
        smtp.send_message(message)

    messages.add_message(request, messages.SUCCESS,
                         'Connecting with Specialists')
    return render(request, 'video_conferencing.html', {'name': request.user})
