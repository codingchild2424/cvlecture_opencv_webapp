from django.shortcuts import render, redirect

from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})

def uimage(request):
    #글을 쓸 때 여기 분기
    if request.method == 'POST': 
        form = UploadImageForm(request.POST, request.FILES) #업로드
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage() #저장
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'opencv_webapp/uimage.html',
    {'form': form, 'uploaded_file_url': uploaded_file_url})
    #글을 안 쓸 때 여기 분기
    else: 
        form = UploadImageForm()
        return render(request, 'opencv_webapp/uimage.html',
    {'form': form})