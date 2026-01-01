from django import forms
from .models import Donation
from datetime import date


class Registration(forms.Form):
    DonorName = forms.CharField()
    UserName = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput, max_length=100, label='Password')
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput, max_length=100, label='Confirm Password')
    DateOfBirth = forms.DateField(
        label="Date of Birth",
        widget=forms.TextInput(attrs={
            'placeholder': 'YYYY-MM-DD'
        }),
        input_formats=['%Y-%m-%d']
    )

    CHOICES1 = [('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]
    Gender = forms.ChoiceField(choices=CHOICES1, widget=forms.RadioSelect)
    OCCUPATION_CHOICES = [('--Select--','--Select--'),('accountant', 'Accountant'),('actor', 'Actor'),('architect', 'Architect'),('artist', 'Artist'),
        ('author', 'Author'),('barber', 'Barber'),('bartender', 'Bartender'),('chef', 'Chef'),('civil_engineer', 'Civil Engineer'),
        ('cleaner', 'Cleaner'),('clergy', 'Clergy'),('consultant', 'Consultant'),('construction_worker', 'Construction Worker'),
        ('dentist', 'Dentist'),('designer', 'Designer'),('developer', 'Developer'),('doctor', 'Doctor'),('electrician', 'Electrician'),
        ('engineer', 'Engineer'),('farmer', 'Farmer'),('fashion_designer', 'Fashion Designer'),('firefighter', 'Firefighter'),
        ('graphic_designer', 'Graphic Designer'),('hairdresser', 'Hairdresser'),('interior_designer', 'Interior Designer'),('journalist', 'Journalist'),
        ('lawyer', 'Lawyer'),('lecturer', 'Lecturer'),('librarian', 'Librarian'),('manager', 'Manager'),('mechanic', 'Mechanic'),('military', 'Military Personnel'),
        ('model', 'Model'),('musician', 'Musician'),('nurse', 'Nurse'),('painter', 'Painter'),('paramedic', 'Paramedic'),
        ('pharmacist', 'Pharmacist'),('photographer', 'Photographer'),('pilot', 'Pilot'),('plumber', 'Plumber'),('police_officer', 'Police Officer'),
        ('politician', 'Politician'),('programmer', 'Programmer'),('psychologist', 'Psychologist'),('real_estate_agent', 'Real Estate Agent'),
        ('receptionist', 'Receptionist'),('researcher', 'Researcher'),('scientist', 'Scientist'),('security_guard', 'Security Guard'),('software_engineer', 'Software Engineer'),
        ('student','Student'),('surgeon', 'Surgeon'),('teacher', 'Teacher'),('taxi_driver', 'Taxi Driver'),('translator', 'Translator'),
        ('truck_driver', 'Truck Driver'),('veterinarian', 'Veterinarian'),('waiter', 'Waiter/Waitress'),('web_developer', 'Web Developer'),
        ('writer', 'Writer'),('other', 'Other')]

    Profession=forms.ChoiceField(choices=OCCUPATION_CHOICES,widget=forms.Select)

    HABIT_CHOICES = [('None', "I don't have any of these habits"),('Smoking', 'Smoking'),('Alcohol', 'Alcohol'),
                     ('Drug Abuse', 'Drug Abuse'),('Chewing Tobacco', 'Chewing Tobacco'),('Vaping', 'Vaping'),
                     ('Recreational Drugs', 'Recreational Drugs'),('Excessive Caffeine', 'Excessive Caffeine'),
                     ('Overuse of Painkillers', 'Overuse of Painkillers')]

    BadHabits = forms.MultipleChoiceField(choices=HABIT_CHOICES,widget=forms.CheckboxSelectMultiple,required=True,label="Do you have any of the following bad habits?")

    CHOICES3 = [('--Select--', '--Select--'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
                ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')]
    BloodGroup = forms.ChoiceField(choices=CHOICES3, widget=forms.Select)
    DISEASE_CHOICES = [('HIV', 'HIV/AIDS'),('Hepatitis B', 'Hepatitis B'),('Hepatitis C', 'Hepatitis C'),
                       ('Syphilis', 'Syphilis'),('Malaria', 'Malaria (recent)'),('Dengue', 'Dengue (recent)'),
                       ('COVID-19', 'COVID-19 (recent)'),('None', 'None of the above'),('Other', 'Other')]

    Diseases = forms.MultipleChoiceField(choices=DISEASE_CHOICES,widget=forms.CheckboxSelectMultiple,
                required=True,label="Have you ever had any of the following diseases?")

    INFECTION_CHOICES = [('Malaria', 'Malaria'),('Dengue', 'Dengue'),('Typhoid', 'Typhoid'),('COVID-19', 'COVID-19'),('Jaundice', 'Jaundice')]

    HadRecentInfection = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')],widget=forms.RadioSelect,label="Have you had any infection in the past 6 months?")

    RecentInfections = forms.MultipleChoiceField(choices=INFECTION_CHOICES,widget=forms.CheckboxSelectMultiple,required=False,label="If yes, select which ones")

    Location = forms.CharField()

    CHOICES2 = [('--Select--', '--Select--'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'),
                ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'),
                ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'),
                ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'),
                ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'),
                ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'),
                ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'),
                ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'),
                ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')]
    State = forms.ChoiceField(choices=CHOICES2, widget=forms.Select)

    Mobile = forms.IntegerField()
    Email = forms.EmailField()


    def clean_Password(self):
        pwd = self.cleaned_data['Password']
        if len(pwd) < 8:
            raise forms.ValidationError('Password should be at least 8 characters long')
        return pwd

    def clean_ConfirmPassword(self):
        password = self.cleaned_data.get('Password')
        confirm = self.cleaned_data.get('ConfirmPassword')
        if password and confirm and password != confirm:
            raise forms.ValidationError('Password and Confirm Password must match')
        return confirm

    def clean_DateOfBirth(self):
        dob = self.cleaned_data['DateOfBirth']
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if age < 18 or age > 55:
            raise forms.ValidationError("Your age must be between 18 and 55 to register.")

        return dob

    def clean_Mobile(self):
        mobile = str(self.cleaned_data['Mobile'])
        if len(mobile) != 10:
            raise forms.ValidationError('Mobile number must be exactly 10 digits')
        return mobile

    def clean_UserName(self):
        username = self.cleaned_data['UserName']
        if Donation.objects.filter(UserName=username).exists():
            raise forms.ValidationError("This username already exists, try another one.")
        return username

    def clean_BadHabits(self):
        habits = self.cleaned_data.get('BadHabits')

        if not habits:
            raise forms.ValidationError("Please select one option.")

        if 'None' in habits:
            if len(habits) > 1:
                raise forms.ValidationError("Please select only 'I don't have any of these habits' if applicable.")
            return habits

        raise forms.ValidationError("Sorry, you are not eligible to register due to selected bad habits.")

    def clean(self):
        cleaned_data = super().clean()
        diseases = cleaned_data.get('Diseases')

        if diseases is None:
            return cleaned_data

        disqualifying_diseases = ['HIV', 'Hepatitis B', 'Hepatitis C', 'Syphilis']


        for disease in diseases:
            if disease in disqualifying_diseases:
                raise forms.ValidationError(
                    "Sorry, you are not eligible to donate blood due to your health condition."
                )


        if 'None' in diseases and len(diseases) > 1:
            raise forms.ValidationError(
                "Please select only 'None of the above' if you're healthy."
            )

        return cleaned_data