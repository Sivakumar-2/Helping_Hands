from django.shortcuts import render,redirect
from .models import Donation
from . import forms

def home(req):
        if req.method == 'POST':
            return render(req, 'home.html')
        else:

            return render(req, 'home.html')


def Register(req):
    if req.method == 'POST':
        form = forms.Registration(req.POST)
        if form.is_valid():
            data = form.cleaned_data


            if ('None' not in data['Diseases'] and data['Diseases']) or \
               ('None' not in data['BadHabits'] and data['BadHabits']):
                error_msg = "Registration denied: donors with disqualifying health or habits are not eligible."
                return render(req, 'Register.html', {'form': form, 'error': error_msg})

            s1 = Donation(
                DonorName=data['DonorName'],
                UserName=data['UserName'],
                Password=data['Password'],
                DateOfBirth=data['DateOfBirth'],
                Gender=data['Gender'],
                Profession=data['Profession'],
                BadHabits=", ".join(data['BadHabits']),
                BloodGroup=data['BloodGroup'],
                Diseases=", ".join(data['Diseases']),
                HadRecentInfection=data['HadRecentInfection'],
                RecentInfections=data['RecentInfections'],
                Location=data['Location'],
                State=data['State'],
                Mobile=data['Mobile'],
                Email=data['Email']
            )
            s1.save()

            msg = "You have successfully registered."
            return render(req,'Register.html', {'form': forms.Registration(), 'success': msg})
    else:
        form = forms.Registration()

    return render(req, 'Register.html', {'form': form})

def login(req):
    if req.method == 'POST':
        username = req.POST.get('uname')
        password = req.POST.get('pwd')

        try:
            user = Donation.objects.get(UserName=username)
            if password == user.Password:
                req.session['username'] = username
                if username == 'admin':
                    req.session['is_admin'] = True
                else:
                    req.session['is_admin'] = False
                return redirect('welcome')
            else:
                return render(req, 'Login.html', {'msg': 'Invalid Username or Password'})
        except Donation.DoesNotExist:
            return render(req, 'Login.html', {'msg': 'Invalid Username or Password'})
    else:
        return render(req, 'Login.html')




# def welcome(req):
#     username = req.session.get('username')
#     admin = req.session.get('admin', False)
#
#     if not username:
#         return redirect('login')
#
#     if admin:
#         data = Donation.objects.all()
#     else:
#         data = Donation.objects.filter(UserName=username)
#
#     return render(req, 'welcome.html', {'data': data, 'admin': admin})

def welcome(req):
    username = req.session.get('username')
    # is_admin = req.session.get('is_admin', False)

    if not username:
        return redirect('login')
    else:

        data = Donation.objects.filter(UserName=username)

    return render(req, 'welcome.html', {'data': data})




def display(req):
    res=Donation.objects.all()
    return render(req,'Display.html',{'help':res})


def group(req):
    if req.method == 'GET':
        s = req.GET.get('group')

        if s :
            donate = Donation.objects.filter(BloodGroup=s)
        else:
            donate = Donation.objects.all()

        return render(req, 'search.html', {'donate': donate })


def update(req):
    blood = Donation.objects.all()
    return render(req, 'Update.html', {'blood': blood})


def update1(request, DonorID):
    if request.method == "POST":
        b = request.POST.get('dname')
        c = request.POST.get('uname')
        d = request.POST.get('pwd')
        e = request.POST.get('dob')
        f = request.POST.get('gender')
        m = request.POST.get('Profession')
        g = request.POST.get('hobbies')
        h = request.POST.get('group')
        i = request.POST.get('location')
        j = request.POST.get('state')
        k = request.POST.get('mobile')
        l = request.POST.get('email')

        res = Donation.objects.get(DonorID=DonorID)

        res.DonorName = b
        res.UserName = c
        res.Password = d
        res.DateOfBirth = e
        res.Gender = f
        res.Profession = m
        res.Hobbies = g
        res.BloodGroup = h
        res.Location = i
        res.State = j
        res.Mobile = k
        res.Email = l
        res.save()

        return redirect('welcome')

    else:
        donation = Donation.objects.get(DonorID=DonorID)
        return render(request, 'Update1.html', {'Donate': donation})

def delete(req):
    mobile = req.GET.get('mobile')
    if mobile:
        blood = Donation.objects.filter(Mobile=mobile)
    else:
        blood = Donation.objects.filter()
    return render(req, 'Welcome.html', {'blood': blood})


def delrec(req, UserName):
    username = req.session.get('username')


    try:
        donor = Donation.objects.get(UserName=UserName)
        if  donor.UserName == username:
            donor.delete()
            return redirect('logout')
        else:
            return HttpResponse("Something went wrong Please try again later")
    except Donation.DoesNotExist:
        return redirect('welcome')


def logout(req):
   return render(req, 'Logout.html')

def aboutus(req):
   return render(req, 'Aboutus.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        if username == 'admin' and password == 'admin123':
            request.session['username'] = username
            request.session['is_admin'] = True
            return redirect('admin_welcome')

        else:
            return render(request, 'Admin-login.html', {'msg': 'Invalid Admin Credentials'})
    return render(request, 'Admin-login.html')

def admin_welcome(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')  # custom admin login page
    data = Donation.objects.all()
    return render(request, 'welcome.html', {'data': data})



def update2(request,DonorID):
    Donor=Donation.objects.get(DonorID=DonorID)
    if request.method == "POST":
        b = request.POST.get('dname')
        c = request.POST.get('uname')
        d = request.POST.get('pwd')
        e = request.POST.get('dob')
        f = request.POST.get('gender')
        m = request.POST.get('Profession')
        g = request.POST.get('hobbies')
        h = request.POST.get('group')
        i = request.POST.get('location')
        j = request.POST.get('state')
        k = request.POST.get('mobile')
        l = request.POST.get('email')

        res = Donation.objects.get(DonorID=DonorID)

        res.DonorName = b
        res.UserName = c
        res.Password = d
        res.DateOfBirth = e
        res.Gender = f
        res.Profession = m
        res.Hobbies = g
        res.BloodGroup = h
        res.Location = i
        res.State = j
        res.Mobile = k
        res.Email = l
        res.save()

        return redirect('welcome')

    return render(request,'Update1.html',{'Donate':Donor})