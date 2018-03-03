from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .sample_object import sample_object

FILE_DESTINATION = 'app/uploaded/temp.csv'

# Handles uploading a file for our use later
def handle_uploaded_file(file):
    with open(FILE_DESTINATION, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# Handles rendering the html page
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        # Upload the file
        handle_uploaded_file(request.FILES['test'])

        # TODO: Process the file using the statistics library
        # Declare all of the variables we will display
        mean = median = mode = variance = first_quartile = third_quartile = std_dev = 0

        # Get the sample data
        data = sample_object(FILE_DESTINATION)

        return render(
            request, 
            "balls.html",
            context={'mean': mean, 'median': median, 'mode': mode, 
            'variance': variance, 'first_quartile': first_quartile,
            'third_quartile': third_quartile, 'std_dev': std_dev})