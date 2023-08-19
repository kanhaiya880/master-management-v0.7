from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import UserProfile
from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.ModelForm):
    ans_1 = forms.CharField(
        label='Who is your target audience?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_2 = forms.CharField(
        label='What are the key messages or content that you want to convey through your website?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_3 = forms.CharField(
        label='Do you have a specific design style or branding guidelines that you would like us to follow for the website?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_4 = forms.CharField(
        label='Do you have the content (text, images, videos, etc.) ready for the website, or would you like us to help with content creation?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_5 = forms.CharField(
        label='Do you have any specific requirements for website functionality or features?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_6 = forms.CharField(
        label='What are the specific functionalities or features that you want to include on your website?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_7 = forms.CharField(
        label='Do you have any additional requirements or comments that you would like to share with us regarding your website development project?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_8 = forms.CharField(
        label='What is your budget for the website development project?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_9 = forms.CharField(
        label='Do you have any specific timeline or deadline for the website development project?',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3 mt-2', 'style': 'height: 100px'})
    )
    ans_question1 = forms.MultipleChoiceField(
        label='What are the main pages or sections that you want to include on your website?',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),
        choices=[('Home', 'Home'), ('About us', 'About us'), ('Products', 'Products'), ('Services', 'Services'), ('Contact us', 'Contact us')],
        required=True
    )
    ans_question2 = forms.MultipleChoiceField(
        label='What are the main goals and objectives of your website?',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),
        choices=[('increase online sales', 'increase online sales'), ('promote brand awareness', 'promote brand awareness'), ('provide information', 'provide information'), ('generate leads', 'generate leads')],
        required=True
    )
    ans_choices = forms.ChoiceField(
        label='Select one of the following options:',
        widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}),
        choices=[('Follow up', 'Follow up'), ('Hold up', 'Hold up'), ('Canceled', 'Canceled')],
        required=True
    )
    date = forms.DateField(
        label='Project timeline or deadline',
        widget=forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'})
    )
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EX: +91 8805406514'}),
        validators=[RegexValidator(r'^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$', message="Please enter a valid phone number.")],
    )
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        try:
            phone_number = PhoneNumberField().clean(phone_number)
        except ValidationError:
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone_number

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'phone_number', 'address', 'business_name', 'ans_1', 'ans_2', 'ans_3', 'ans_4', 'ans_5', 'ans_6', 'ans_7', 'ans_8', 'ans_9', 'ans_question1', 'ans_question2', 'ans_choices', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of your organization or business:'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EX: +91 8805406514'}),
            'ans_1': forms.Textarea(attrs={'class': 'form-control mb-3', 'style': 'height: 100px'}),
            'ans_2': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}),
            'ans_3': forms.Textarea(attrs={'class': 'form-control mb-3', 'style': 'height: 100px'}),
            'ans_4': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}),
            'ans_5': forms.Textarea(attrs={'class': 'form-control mb-3', 'style': 'height: 100px'}),
            'ans_6': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}),
            'ans_7': forms.Textarea(attrs={'class': 'form-control mb-3', 'style': 'height: 100px'}),
            'ans_8': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}),
            'ans_9': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px'}),
        }
