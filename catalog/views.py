from django.shortcuts import render

# Create your views here.

from catalog.models import Tutor, Tutee

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tutors = Tutor.objects.all().count()
    num_tutees = Tutee.objects.all().count()
    
    context = {
        'num_tutors': num_tutors,
        'num_tutees': num_tutees,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)