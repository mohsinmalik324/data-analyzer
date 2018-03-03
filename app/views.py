from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

FILE_DESTINATION = 'uploaded/temp.csv'

# instead of index.html -- include w/e you want
def index(request):
    return render(request, 'index.html')

def process_upload(request):
    # Process the file
    success = upload_file(request)
    if (success):
        # process the file
    else:
        return render(request, 'index.html')

# Handles an uploaded 
def handle_uploaded_file(file):
    with open(FILE_DESTINATION, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# This function handles an upload file request
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])

            # This isn't necessary -- just indicates that it was successful
            return True
        else:
            form = UploadFileForm()

        return False;