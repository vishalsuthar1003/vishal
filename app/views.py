from django.shortcuts import render
def registration(request):
    return render(request,"app/registration.html")
def form(request):
    return render(request,"app/form.html")
def form(request):
    return render(request,"app/registration1.html")
def registerUser(request):
    fname= request.POST['fname']
    lname= request.POST['lname']
    email= request.POST['email']
    password= request.POST['password']

    newuser = user.objects.create(fname=fname,lname=lname,email=email,password=password)
    return render(request,"app/success.html ")