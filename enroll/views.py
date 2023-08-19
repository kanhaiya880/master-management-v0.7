from django.shortcuts import render, HttpResponseRedirect ,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CustomAuthenticationForm
from django.db.models import Count
from dash.models import UserProfile,ConfirmedUserProfile
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import datetime

# Create your views here.
def user_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            fm=CustomAuthenticationForm(data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Login in successful')
                    return HttpResponseRedirect('/dash/')
        else:
            fm=CustomAuthenticationForm()
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dash/')



# def user_dash(request):
#     if request.user.is_authenticated:

#         return render(request,'dash/dashboard.html',{'name':request.user})
#     else:
#         return HttpResponseRedirect('/')




def user_dash(request):
    if request.user.is_authenticated:
        user = request.user
        
        if not user.is_superuser:

            user_data = UserProfile.objects.filter(user=user)
            con_data = ConfirmedUserProfile.objects.filter(user=user)
            folow_data=UserProfile.objects.filter(user=user,ans_choices='Follow up')
            num_data = user_data.count()
            con_num=con_data.count()
            f_data=folow_data.count()
            data_counts = user_data.values('name').annotate(count=Count('name'))
            return render(request,'dash/dashboard.html',{'name': user.username, 'num_data': num_data, 'data_counts': data_counts,'con_data':con_num,'f_data':f_data})
        else:
              
              num_data = UserProfile.objects.count()
              con_num = ConfirmedUserProfile.objects.count()
              f_data=UserProfile.objects.filter(ans_choices='Follow up').count()
              data_counts = UserProfile.objects.values('name').annotate(count=Count('name'))
             
              return render(request,'dash/dashboard.html',{'name': user.username, 'num_data': num_data, 'data_counts': data_counts,'con_data':con_num,'f_data':f_data})     
    else:
        return redirect('/')



def user_logout(request):
    logout(request)
    return redirect('/')

def exception_handaling(request):
    return render(request,'enroll/exc.html')




def generate_receipt(request, pk):
    # Get the ConfirmedUserProfile instance
    profile = get_object_or_404(ConfirmedUserProfile, pk=pk)

    # Create the HttpResponse object with PDF headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="receipt.pdf"'

    # Create the PDF object, using the response object as its "file."
    doc = SimpleDocTemplate(response, pagesize=letter, topMargin=1*inch, bottomMargin=1*inch)

    # Set up the styles
    styles = getSampleStyleSheet()

    # Create the story elements for the PDF
    story = []

    # Add a custom header
    header_text = "<b>VI Mark Tech </b>"
    header = Paragraph(header_text, styles['Heading1'])
    story.append(header)

    # Draw the fields with numbering
    field_number = 1

    def draw_field(field_name, field_value):
        nonlocal field_number
        field_text = f"<b>{field_number}. {field_name}:</b> {field_value}"
        field_paragraph = Paragraph(field_text, styles['Normal'])
        story.append(Spacer(1, 0.2*inch))
        story.append(field_paragraph)
        field_number += 1

    phone = str(profile.phone_number)

    draw_field("Name", profile.name)
    draw_field("Business Name", profile.business_name)
    draw_field("Email", profile.email)
    draw_field("Address", profile.address)
    draw_field("Phone Number", phone)
    draw_field("What are the key messages or content that you want to convey through your website?", profile.ans_1)
    draw_field("What are the key messages or content that you want to convey through your website?", profile.ans_2)
    draw_field("Who is your target audience?", profile.ans_3)
    draw_field("Do you have a specific design style or branding guidelines that you would like us to follow for the website?", profile.ans_4)
    draw_field("Do you have the content (text, images, videos, etc.) ready for the website, or would you like us to help with content creation?", profile.ans_5)
    draw_field("Do you have any specific requirements for website functionality or features?", profile.ans_6)
    draw_field("What are the specific functionalities or features that you want to include on your website?", profile.ans_7)
    draw_field("Do you have any additional requirements or comments that you would like to share with us regarding your website development project?", profile.ans_8)
    draw_field("What is your budget for the website development project?", profile.ans_9)
    draw_field("Do you have any specific timeline or deadline for the website development project?", str(profile.date))
    draw_field("What are the main pages or sections that you want to include on your website?", ", ".join(profile.ans_question1))
    draw_field("What are the main goals and objectives of your website?", ", ".join(profile.ans_question2))
    draw_field("Status:", profile.ans_choices)

    # Create the brand title and signature line
    brand_title = "<b>Brand Title</b>"
    brand_paragraph = Paragraph(brand_title, styles['Normal'])
    signature_line = "Signature: ____________________"
    signature_paragraph = Paragraph(signature_line, styles['Normal'])

    # Add the brand title and signature line to the story
    story.append(Spacer(1, 0.4*inch))
    story.append(brand_paragraph)
    story.append(Spacer(1, 0.2*inch))
    story.append(signature_paragraph)

    # Add printing date and time to the footer
    footer_text = f"Printed on: {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}"
    footer = Paragraph(footer_text, styles['Normal'])
    story.append(Spacer(1, 0.2*inch))
    story.append(footer)

    # Build the PDF document
    doc.build(story)

    return response



