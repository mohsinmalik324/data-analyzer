from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

FILE_DESTINATION = 'app/uploaded/temp.csv'
FILE_RELATIVE = "uploaded/temp.csv"


# Handles an uploaded 
def handle_uploaded_file(file):
    with open(FILE_DESTINATION, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# instead of index.html -- include w/e you want
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        # print(request.FILES)
        # form = UploadFileForm(request.POST, request.FILES)
        handle_uploaded_file(request.FILES['test'])
        return render(request, "balls.html")


# def process_upload(request):
#     # Process the file
#     success = upload_file(request)
#     if (success):
#         # process the file
#     else:
#         return render(request, 'index.html')

# # This function handles an upload file request
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])

#             # This isn't necessary -- just indicates that it was successful
#             return True
#         else:
#             form = UploadFileForm()

#         return False;