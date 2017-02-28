from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import diveshops

def view_diveshops(request, id=None):
    if id:
        diveshops = get_object_or_404(diveshops, id=id)
        return render(request, 'dive_list.html', {'diveshops': diveshops})
    else:
        return render(request, 'dive_list.html')
