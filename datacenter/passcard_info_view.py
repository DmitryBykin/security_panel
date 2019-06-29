from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.storage_information_view import get_duration, format_duration, is_visit_long

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    # Программируем здесь  
              
    visits = Visit.objects.filter(passcard=passcard)    
    this_passcard_visits = []
    for visit in visits:
      this_passcard_visits.append(
          {
              "entered_at": visit.entered_at,
              "duration": format_duration(visit),
              "is_strange": is_visit_long(visit)
          }
      )
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
