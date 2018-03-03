from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from .sample_object import sample_object
from .render_tools import render_table

FILE_DESTINATION = 'app/uploaded/temp.csv'

# Handles uploading a file for our use later
def handle_uploaded_file(file):
    with open(FILE_DESTINATION, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# Handles rendering the html page
def index(request):
    # Determine what type of a request  it is
    if request.method == 'GET':
        return render(request, 'index.html')

    elif request.method == 'POST':
        # Upload the file 
        handle_uploaded_file(request.FILES['data-file'])

        # Declare all of the varialbes we are going to display
        mean = median = mode = variance = first_quartile = third_quartile = std_dev = 0

        # Get the sample data and enter the info into an html table
        data = sample_object(FILE_DESTINATION)
        data.generate_list()
        table = data.point_list

        mean = data.get_mean_column1()

        return render(
            request, 
            "balls.html",       # FIXME: Change this 
            context={'mean': mean, 'median': median, 'mode': mode, 
            'variance': variance, 'first_quartile': first_quartile,
            'third_quartile': third_quartile, 'std_dev': std_dev,
            'data_table': table})