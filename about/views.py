from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import WorkWithUsForm


def about_us(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        work_with_us_form = WorkWithUsForm(data=request.POST)
        if work_with_us_form.is_valid():
            work_with_us_form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                "The request to work with us received! We'll be in touch within 2 working days.")
    
    about = About.objects.all().order_by('-updated_on').first()
    work_with_us_form = WorkWithUsForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "work_with_us_form": work_with_us_form
         },
    )

