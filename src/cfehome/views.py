from django.http import HttpResponse
import pathlib
# rendering out template folder html documents.->
from django.shortcuts import render

# importing the models file that we created:-
from visits.models import PageVisit

this_dir= pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    # print(this_dir)
    # html_= ""
    # html_file_path=this_dir / "home.html"
    # html_= html_file_path.read_text()

    # counting the number of page visits:-
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    try:
        percent=(page_qs.count() * 100.0) /qs.count()
    except:
        percent=0
    my_title="My Name is"
    html_template="home.html"
    my_context={
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)

def my_old_home_page_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello world</h1>")