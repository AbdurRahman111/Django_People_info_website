from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import random
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404
from .models import EmailConfirmed, contact_table, person_information
from .forms import add_person_info
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def search_person(request):
    Name = request.GET.get('Name')
    State_of_origin = request.GET.get('State_of_origin')
    Complexion = request.GET.get('Complexion')
    print(Name, State_of_origin, Complexion)
    print('okok')

    if Name!='' and State_of_origin!='' and Complexion=='All_Type':
        search_person = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name) | Q(State_of_Origin__icontains=State_of_origin)).order_by('-id')
        search_person_count = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name) | Q(State_of_Origin__icontains=State_of_origin)).count()

    elif Name != '' and State_of_origin != '':
        search_person = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name) | Q(State_of_Origin__icontains=State_of_origin)).filter(Complexion=Complexion).order_by('-id')
        search_person_count = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name) | Q(State_of_Origin__icontains=State_of_origin)).filter(Complexion=Complexion).count()

    elif Name!='' and State_of_origin=='' and Complexion=='All_Type':
        search_person = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name)).order_by('-id')
        search_person_count = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name)).count()

    elif Name == '' and State_of_origin != '' and Complexion == 'All_Type':
        search_person = person_information.objects.filter(Q(State_of_Origin__icontains=State_of_origin)).order_by('-id')
        search_person_count = person_information.objects.filter(Q(State_of_Origin__icontains=State_of_origin)).count()


    elif Name!='' and State_of_origin=='':
        search_person = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name)).filter(Complexion=Complexion).order_by('-id')
        search_person_count = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name)).filter(Complexion=Complexion).count()

    elif Name == '' and State_of_origin != '':
        search_person = person_information.objects.filter(Q(State_of_Origin__icontains=State_of_origin)).filter(Complexion=Complexion).order_by('-id')
        search_person_count = person_information.objects.filter(Q(State_of_Origin__icontains=State_of_origin)).filter(Complexion=Complexion).count()

    elif Name=='' and State_of_origin=='' and Complexion=='All_Type':
        search_person = person_information.objects.all().order_by('-id')
        search_person_count = person_information.objects.all().count()

    elif Name=='' and State_of_origin=='':
        search_person = person_information.objects.filter(Complexion=Complexion).order_by('-id')
        search_person_count = person_information.objects.filter(Complexion=Complexion).count()

    else:
        search_person = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name) | Q(State_of_Origin__icontains=State_of_origin))
        search_person_count = person_information.objects.filter(Q(First_name__icontains=Name) | Q(Last_name__icontains=Name) | Q(Other_name__icontains=Name) | Q(State_of_Origin__icontains=State_of_origin)).count()

    # search_jobs_form = posted_jobs.objects.filter(Q(job_title__icontains=job_title) | Q(job_details__icontains=job_title) | Q(job_location__icontains=job_location) | Q(job_type__icontains=job_type)).order_by('-id')

    # search_jobs_form = posted_jobs.objects.filter(
    #     Q(job_title__icontains=job_title) | Q(job_details__icontains=job_title)).filter(job_post_status='2').order_by(
    #     '-id')
    #
    # search_jobs_count = posted_jobs.objects.filter(
    #     Q(job_title__icontains=job_title) | Q(job_details__icontains=job_title)).filter(job_post_status='2').order_by(
    #     '-id').count()

    p = Paginator(search_person, 10)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)


    context13 = {'search_person': search_person, 'Name': Name, 'State_of_origin': State_of_origin,
                 'Complexion': Complexion, 'search_person_count': search_person_count, 'myseaech': page, 'list': list}

    return render(request, 'search_person.html', context13)


def add_a_person(request):
    if request.user.is_authenticated:
        form1=add_person_info()
        if request.method == 'POST':
            form1 = add_person_info(request.POST, request.FILES)
            if form1.is_valid():
                abc=form1.save(commit=False)
                abc.user=request.user
                abc.save()
                messages.success(request, 'Successfully Added !!')
                return redirect('add_a_person')
        context={'form1':form1}
        return render(request, 'add_a_person.html', context)
    else:
        messages.info(request, "You Have to Login First")
        return redirect('account')



def see_my_adds(request):
    if request.user.is_authenticated:
        user = request.user
        mypost = person_information.objects.filter(user=user).order_by('-id')
        # pagination
        p = Paginator(mypost, 10)
        # print(p.num_pages)
        number_of_pages = p.num_pages

        # show list of pages
        number_of_pages_1 = p.num_pages + 1
        list = []
        for i in range(1, number_of_pages_1):
            list.append(i)

        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)

        context11 = {'mypost': page, 'list': list}
        return render(request, 'see_my_adds.html', context11)
    else:
        messages.info(request, "You Have to Login First")
        return redirect('account')


def person_details(request, id):
    get_person_information = person_information.objects.get(id=id)
    context11 = {'get_person_information':get_person_information}
    return render(request, 'person_details.html', context11)


def about(request):
    return render(request, 'about.html')


def contact(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')

    save_contact_table=contact_table(name=name, email=email, message=message)
    save_contact_table.save()

    messages.success(request, name+' Your Message Successfully Deliver to Manager. Our manager will get back to you soon. Thank You !!')
    return redirect('/')




def account(request):
    if request.method=='POST':

        #check the post peramiters
        sign_email=request.POST['sign_email']
        sign_password=request.POST['sign_password']
        confirm_sign_password=request.POST['confirm_sign_password']
        sign_first_name=request.POST['sign_first_name']
        sign_last_name=request.POST['sign_last_name']




        #chech the error inputs

        user_email_info = User.objects.filter(email=sign_email)

        erorr_message= ""

        if user_email_info:
            # messages.error(request, "Email Already Exist")
            erorr_message = "Email Already Exist"

        elif sign_password != confirm_sign_password:
            # messages.error(request, "Passwords are not match")
            erorr_message = "Passwords are not match"

        elif len(sign_password)<7:
            # messages.error(request, "Passwords Must be Al least 7 Digits")
            erorr_message = "Passwords Must be Al least 7 Digits"

        if not erorr_message:

            # create user
            myuser = User.objects.create_user(sign_email, sign_email, sign_password)
            myuser.first_name=sign_first_name
            myuser.last_name=sign_last_name
            myuser.is_active = False
            myuser.save()


            # send mail
            user = EmailConfirmed.objects.get(user=myuser)
            site = get_current_site(request)
            email = myuser.email
            first_name = myuser.first_name
            last_name = myuser.last_name

            sub_of_email = "Activation Email From Medicify."
            email_body = render_to_string(
                'verify_email.html',
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'domain': site.domain,
                    'activation_key': user.activation_key
                }
            )

            send_mail(
                sub_of_email,  # Subject of message
                email_body,  # Message
                '',  # From Email
                [email],  # To Email

                fail_silently=True
            )

            messages.success(request, 'Check Your Email for Activate Your Account !!!')

            return redirect('/')

        else:
            value_dic = {'sign_email': sign_email, 'sign_first_name': sign_first_name,
                         'sign_last_name': sign_last_name, 'erorr_message':erorr_message}
            return render(request, 'account.html', value_dic)
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'account.html')



def login_func(request):
    if request.method == 'POST':
        log_username = request.POST['log_username']
        log_password = request.POST['log_password']
        # this is for authenticate username and password for login
        user = authenticate(username=log_username, password=log_password)

        erorr_message_2 = ""

        if user is not None:
            login(request, user)
            # messages.success(request, "Successfully Logged In !!")
            return redirect('index')
        else:
            erorr_message_2 ="Invalid Credentials, Please Try Again !!"



            value_func2 = {'erorr_message_2':erorr_message_2, 'log_username':log_username}
            # messages.error(request, "Invalid Credentials, Please Try Again !!")
            return render(request, 'account.html', value_func2)


def func_logout(request):
    # this is for logout from user id
    logout(request)
    return redirect('index')


def email_confirm(request, activation_key):
    user= get_object_or_404(EmailConfirmed, activation_key=activation_key)
    if user is not None:
        user.email_confirmed=True
        user.save()

        myuser=User.objects.get(email=user)
        myuser.is_active=True
        myuser.save()


        return render(request, 'registration_complete.html')
