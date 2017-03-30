from django.shortcuts import render
from django.utils import timezone
from .models import PigEntry
from .forms import PigEntryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django import forms

# Create your views here.
@login_required
def pig_form(request):
    if request.method =="POST":
        form = PigEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            week = entry.entry_date.isocalendar()[1]
            
            if PigEntry.objects.filter(farm = request.user, week_of_year = week, room_number=entry.room_number).exists():
                exisiting = PigEntry.objects.get(farm = request.user, week_of_year = week, room_number=entry.room_number)
                exisiting.number_of_pigs += entry.number_of_pigs
                exisiting.save()
            else: 
                entry.farm = request.user
                entry.week_of_year = week
                entry.save()
            #entry.entry_date = request.entry_date
           # entry.farm = request.user
            #entry.number_pigs = request.number_pigs
            #print("request")
            #print(entry)
            #Other form saving stuff here
            return redirect('farm_submissions')
    else:
        form = PigEntryForm()
        form.fields['entry_date'].widget = forms.HiddenInput()
    return render(request, 'mainForm/index.html', {'form': form, 'submission': request})

@login_required
def farm_submissions(request):
    submissions = PigEntry.objects.filter(farm = request.user).order_by('-week_of_year', 'room_number')
    return render(request, 'mainForm/submissions.html', {'submissions':submissions})

"""def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

    else:
        form = PostForm()
    return render(request, 'mainForm/post_edit.html', {'form': form})
   """ 