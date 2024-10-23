from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Image
from django.db.models import Q
from .forms import ImageForm


# Create your views here.
def createaccount(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        if User.objects.filter(email=email).exists():
            return redirect('userexist.html')

        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname

        user.save()

        return redirect('acccreated')


    return render(request, 'create-account.html')

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from form input
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)  
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('invalidmessage')
       
    return render(request, 'index.html')


def forgotpassword(request):
    return render(request,'forgot-password.html')

def acccreated(request):
    return render(request,"acc-created.html")

def invalidmessage(request):
    return render(request,"invalid-message.html")

def userexist(request):
    return render(request,"userexist.html")

def home(request):
   objects = Image.objects.all()
   return render(request,"Home page.html",{'image':objects})

def detail_view(request,id):
    objects=get_object_or_404(Image,id=id)
    return render(request,"details.html",{'image':objects})

def search(request):
    query=None
    result=[]
    if request.method == 'GET':
        query=request.GET.get('search','')
        result=Image.objects.filter(Q(title__icontains=query))
    return render(request, 'search.html',{'query':query,'result':result})   

def upload(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.get('tags')
        image = request.FILES.get('image')

        if image:  # Check if the image was uploaded
            new_image = Image(title=title, description=description,tags=tags, image=image)
            new_image.save()
            valid_message = "New post plant added!"
            return render(request, 'upload.html', {'valid': valid_message})  # Redirect after successful upload
        else:
            # You can add an error message here to inform the user
            error_message = "Please upload a valid image."
            return render(request, 'upload.html', {'error': error_message})

    return render(request, 'upload.html') 

def editpost(request,id):
    post=get_object_or_404(Image,id=id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm(instance=post)
    return render(request, 'edit.html',{'form': form})


def deletepost(request,id):
    post=Image.objects.get(pk=id)
    post.delete()
    return redirect('home')




def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect("index")  # Redirect to login or homepage