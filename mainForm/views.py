from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from .models import PigEntry
from .models import Flow
from .forms import PigEntryForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import redirect
from django import forms
from django.forms import formset_factory
from django.contrib import messages


# Create your views here.
@login_required
def pig_form(request):
    user = request.user
    
    PigFormSet = formset_factory(PigEntryForm,  extra=14)
    if request.method == "POST" :
        
        entry_forms = PigFormSet(request.POST)

        if entry_forms.is_valid():
            new_entrys = []
            for entry_form in entry_forms:

                if entry_form.is_valid():
                    number_of_pigs = entry_form.cleaned_data.get('number_of_pigs')
                    date = entry_form.cleaned_data.get('entry_date')
                    print(date)
                    if number_of_pigs:
                        new_entrys.append(PigEntry(farm=user, entry_date = date, number_of_pigs=number_of_pigs))
                else:
                    print(entry_form.errors)
            try:
                with transaction.atomic():
                    #Replace the old with the new
                    for entry in new_entrys:
                        PigEntry.objects.filter(entry_date=entry.entry_date, farm = entry.farm).delete()

                    PigEntry.objects.bulk_create(new_entrys)

                    # And notify our users that it worked
                    messages.success(request, 'The pig entry was successful')

            except IntegrityError: #If the transaction failed
                messages.error(request, 'There was an error submitting the pig entry.')
                return redirect('index')
                
            
            return redirect('farm_submissions')
        else:
            print(entry_forms.errors)
            
    else:
        #form = PigEntryForm()
        formset = PigFormSet()
        #form.fields['entry_date'].widget = forms.HiddenInput()
    return render(request, 'mainForm/index.html', {'formset':PigFormSet, 'submission': request})

@login_required
def farm_submissions(request):
    entry_dates = []
    day = datetime.today()
    day_of_week = datetime.today().weekday()

    to_beginning_of_week = timedelta(days=day_of_week)
    beginning_of_week = day - to_beginning_of_week

    to_end_of_week = timedelta(days=13 - day_of_week)
    end_of_week = day + to_end_of_week

    delta = end_of_week - beginning_of_week         # timedelta
    print(delta.days)
    for i in range(delta.days + 1):
        entry_dates.append(datetime.date(beginning_of_week + timedelta(days=i)))

    print("Entry Dates:"+str(entry_dates))
    #Stored with the following structure: 
    # Submissions[
    #   [
    #       Flow, 
    #       [
    #           [Farm, FarmEntrys[]],
    #           [Farm, FarmEntyrs[]],
    #           ,...
    #       ]
    #   ],
    #   [Flow, []]]
    submissions = []
    for flow in Flow.objects.all():
        print(flow)
        
        flow_data = []

        all_farms = User.objects.all().select_related('profile')
        farm_in_flow = all_farms.filter(profile__flow = flow)

        for farm in farm_in_flow:
            farm_entrys = []
            for date in entry_dates:
                farm_entry = PigEntry.objects.filter(farm = farm, entry_date = date)      
                farm_entrys.append(farm_entry)
            farm_entry_pair = (farm, farm_entrys)
            flow_data.append(farm_entry_pair)
        
        
        submissions.append((flow,flow_data))
    print(submissions)      
        #submissions = PigEntry.objects.filter(farm = request.user).order_by('-entry_date')
    return render(request, 'mainForm/submissions.html', {'submissions':submissions, 'dates':entry_dates})
