from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import timedelta, datetime

def is_visit_long(visit, minutes = 60):
  return get_duration(visit) / 60 > minutes

def get_duration(visit):
  if visit.leaved_at:
    amount_seconds = (visit.leaved_at - visit.entered_at).seconds  
  else:    
    amount_seconds = (datetime.now() - visit.entered_at).seconds
  return amount_seconds

def format_duration(visit):
  return str(timedelta(seconds=get_duration(visit)))

def storage_information_view(request):
    # Программируем здесь   
    
    visits = Visit.objects.filter(leaved_at = None)
    non_closed_visits = []

    for visit in visits:    
      non_closed_visits.append(
          {
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": format_duration(visit),
            "is_strange": is_visit_long(visit)            
        }        
      )
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
