from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreatUserForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from .models import Profile
from django.http import HttpResponse,HttpResponseRedirect

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def register(request):

    if request.method == 'POST':
        user_form = CreatUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request,'accounts/registration_done.html',{'new_user':new_user})
        else:
            return render(request,'accounts/registration.html', {'user_form':user_form})
    else:
        user_form = CreatUserForm()
        return render(request,'accounts/registration.html',{'user_form':user_form})

@login_required
def edit_profile(request):

    if request.method == 'POST':
        user_edit_form = UserEditForm(instance=request.user,data=request.POST)
        profile_edit_form = ProfileEditForm(instance=request.user.profile,data=request.POST)

        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            messages.add_message(request,messages.SUCCESS,'profile updated')
            return redirect('dashboard')
        else:
            return render(request,'accounts/edit_profile.html',{'user_edit_form':user_edit_form,
                                                                'profile_edit_form':profile_edit_form})
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)

        return render(request,'accounts/edit_profile.html',{'user_edit_form':user_edit_form,
                                                            'profile_edit_form':profile_edit_form})








