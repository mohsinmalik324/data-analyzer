from django.shortcuts import render

# instead of index.html -- include w/e you want
def index(request):
    return render(request, 'index.html')