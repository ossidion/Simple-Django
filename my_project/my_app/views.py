from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main.html')

def welcome(request):
    name = request.GET.get("name")
    surname = request.GET.get("surname")
    favourite_colour = request.GET.get("favourite_colour")
    favourite_number = request.GET.get("favourite_number")
    return render(request, 'welcome.html', {"name" : name,
                                            "surname" : surname,
                                            "favourite_colour" : favourite_colour,
                                            "favourite_number" : favourite_number})