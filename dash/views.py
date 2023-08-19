from django.shortcuts import render, HttpResponseRedirect,HttpResponse,get_object_or_404,redirect
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile,ConfirmedUserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# def add_show(request):
#     pn="Add Customer"
#     if request.user.is_authenticated:
        
#         fm = UserForm()
#         user_id = request.user.id  # get the current user's ID
        
#         if request.method == 'POST':
#             fm = UserForm(request.POST)
#             if fm.is_valid():
#                 nm = fm.cleaned_data['name']
#                 em = fm.cleaned_data['email']
#                 ps = fm.cleaned_data['address']
#                 ans1 = fm.cleaned_data['ans_1']
#                 ans2 = fm.cleaned_data['ans_2']
#                 ans_choices=fm.cleaned_data['ans_choices']
#                 regi = UserProfile(name=nm, email=em, address=ps, ans_1=ans1, ans_2=ans2,ans_choices=ans_choices, user_id=user_id)
#                 regi.save()
#                 fm = UserForm()
#                 return HttpResponseRedirect("/dash/")
#             else:
#                 fm = UserForm()

    
#         stud = UserProfile.objects.filter(user_id=user_id)  # retrieve data of the current user only

#         return render(request, "dash/addandshow.html", {'form': fm, 'stu': stud , 'username': request.user.username,'page_name':pn})
#     else:
#         print("redirect")

#         return HttpResponseRedirect('/')
def add_show(request):
    pn = "Add Customer"
    if request.user.is_authenticated:
        fm = UserForm()
        user_id = request.user.id  # get the current user's ID

        if request.method == 'POST':
            fm = UserForm(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                ps = fm.cleaned_data['address']
                ans1 = fm.cleaned_data['ans_1']
                ans2 = fm.cleaned_data['ans_2']
                ans3 = fm.cleaned_data['ans_3']
                ans4 = fm.cleaned_data['ans_4']
                ans5 = fm.cleaned_data['ans_5']
                ans6 = fm.cleaned_data['ans_6']
                ans7 = fm.cleaned_data['ans_7']
                ans8 = fm.cleaned_data['ans_8']
                ans9 = fm.cleaned_data['ans_9']
                ans_choices = fm.cleaned_data['ans_choices']
                ans_question1 = fm.cleaned_data['ans_question1']
                ans_question2 = fm.cleaned_data['ans_question2']
                dead_line=fm.cleaned_data['date']
                business=fm.cleaned_data['business_name']
                phone=fm.cleaned_data['phone_number']
                regi = UserProfile(name=nm, email=em, address=ps, ans_1=ans1, ans_2=ans2, ans_choices=ans_choices , ans_question1=ans_question1 , ans_question2=ans_question2,user_id=user_id,date=dead_line,ans_3=ans3,ans_4=ans4,ans_5=ans5,ans_6=ans6,ans_7=ans7,ans_8=ans8,ans_9=ans9,phone_number=phone,business_name=business)
                regi.save()
                fm = UserForm()
                return HttpResponseRedirect("/dash/")
            else:
                fm = UserForm(request.POST)

        stud = UserProfile.objects.filter(user_id=user_id)  # retrieve data of the current user only

        return render(request, "dash/addandshow.html", {'form': fm, 'stu': stud, 'username': request.user.username, 'page_name': pn})
    else:
        print("redirect")
        return HttpResponseRedirect('/')




@login_required
def delete_fun(request, id):
    if request.method == 'POST':
        pi = get_object_or_404(UserProfile, pk=id, user=request.user)
        pi.delete()
    return redirect('show')


def update_data(request, id):
    pn="Update Information"
    pi=None
    if request.user.is_authenticated:
        # profile = ConfirmedUserProfile.objects.get(pk=id)
        user_id = request.user.id
        
        try:
            pi = UserProfile.objects.get(pk=id, user_id=user_id)
        except UserProfile.DoesNotExist:
            messages.error(request, 'Sorry, the requested data does not exist or does not belong to you.')
            # return redirect('/dash/')

        if request.method == 'POST':
            fm = UserForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Data updated successfully!')
                # return redirect('/dash/')
        else:
            if pi==None:
                return render(request, 'enroll/exc.html')
            fm = UserForm(instance=pi)
        return render(request, 'dash/update.html', {'form': fm,'page_name':pn})
    else:
        return redirect('/')

    


def show(request):
    pn="Your Submissions"
    if request.user.is_authenticated:
        user = request.user
        stud = UserProfile.objects.filter(user=user)
        return render(request, 'dash/show.html', {'stu': stud,'page_name':pn})
    else:
        print("redirect")
        return HttpResponseRedirect('/')


     
def admin_all_show(request):
         pn="All Responses"
         if request.user.is_superuser:
            stud = UserProfile.objects.all()
            return render(request,'dash/show.html',{'stu':stud,'page_nam':pn})
         else:
            print("redirect")
            return HttpResponseRedirect('/')


def admin_update(request, id):
    pn="Confirmation Form"
    value="Confirm"
    if request.user.is_superuser:
        
        
        if request.method == 'POST':
            pi = UserProfile.objects.get(pk=id)
            fm = UserForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()

                # Save the confirmed data to ConfirmedUserProfile model
                confirmed_data = ConfirmedUserProfile.objects.create(
                    name=pi.name,
                    email=pi.email,
                    address=pi.address,
                    ans_1=pi.ans_1,
                    ans_2=pi.ans_2,
                    ans_3=pi.ans_3,
                    ans_4=pi.ans_4,
                    ans_5=pi.ans_5,
                    ans_6=pi.ans_6,
                    ans_7=pi.ans_7,
                    ans_8=pi.ans_8,
                    ans_9=pi.ans_9,
                    ans_choices=pi.ans_choices,
                    business_name=pi.business_name,
                    ans_question1=pi.ans_question1,
                    ans_question2=pi.ans_question2,
                    date=pi.date,
                    user=pi.user
                )
                pi.delete()

                messages.success(request, 'Data updated successfully and confirmed!')
                return redirect('/show/')
        else:
            pi = UserProfile.objects.get(pk=id)
            fm = UserForm(instance=pi)

        return render(request, 'dash/update.html', {'form': fm,'value':value,'page_name':pn})
    else:
        return redirect('/')



def follow_up(request):
    pn="Follow Up Records"
    if request.user.is_superuser:
        stud = UserProfile.objects.filter(ans_choices='Follow up').order_by('-id')
        return render(request, 'dash/show.html', {'stu': stud,'page_name':pn})
    else:
        return HttpResponseRedirect('/')

def user_follow_up(request):
    pn = "Follow Up clients"
    if request.user.is_authenticated:
        user = request.user
        stud = UserProfile.objects.filter(user=user, ans_choices='Follow up')
        print(stud)
        return render(request, 'dash/show.html', {'stu': stud, 'page_name': pn})
    else:
        print("redirect")
        return HttpResponseRedirect('/')





#show the data of confirmed user

def confirm_admin_obj(request):
          pn="Confirmed Clients"
          if request.user.is_authenticated and not request.user.is_superuser:          
                    user = request.user
                    stud = ConfirmedUserProfile.objects.filter(user=user)
                    return render(request, 'dash/show.html', {'stu': stud,'page_name':pn})
          elif request.user.is_superuser:
            stud = ConfirmedUserProfile.objects.all()
            return render(request,'dash/show.html',{'stu':stud,'page_name':pn})
          else:
            return HttpResponseRedirect('/')





def confirm_update(request, id):
   
    if request.user.is_superuser:
        profile = ConfirmedUserProfile.objects.get(pk=id)
        pn="Confirmed Data"
        value="Update"
        show_generate_receipt = True
        if request.method == 'POST':
            pi = ConfirmedUserProfile.objects.get(pk=id)
            fm = UserForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()

                messages.success(request, 'Data updated successfully and confirmed!',{'value':value})
                return redirect('/sub/')
        else:
            pi = ConfirmedUserProfile.objects.get(pk=id)
            fm = UserForm(instance=pi)

        return render(request, 'dash/update.html', {'form': fm,'value':value,'page_name':pn,'profile':profile,'pk':id, 'show_generate_receipt': show_generate_receipt})
    else:
        return redirect('/')



def confirm_delete(request,id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi=ConfirmedUserProfile.objects.get(pk=id)
            pi.delete()
        return redirect('/confirm_obj/')
    else:
        return redirect('/')
    
