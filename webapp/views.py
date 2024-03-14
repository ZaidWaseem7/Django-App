from django.shortcuts import render ,redirect 

from .forms import CreateForm,LoginForm,CreateRecordForm,UpdateRecordForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Record


# Starting Page


def home(request):

    return render(request,"webapp/home.html")



# Register a User

def register(request):
    form=CreateForm()

    if request.method == "POST":

        form=CreateForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Account Created Successfully")

            return redirect("login")

    context={"form":form}

    return render(request,"webapp/register.html",context)


#Login User


def login(request):
    form=LoginForm()

    if request.method == "POST":

        form=LoginForm(request, data=request.POST )

        if form.is_valid():
            username= request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context={"form":form}

    return render(request,"webapp/login.html",context)



# DashBoard


@login_required(login_url="login")
def dashboard(request):
    
    my_record=Record.objects.all()

    context={"records": my_record}

    return render(request, "webapp/dashboard.html",context)




#create record

@login_required(login_url="login")
def create_record(request):
    
    form=CreateRecordForm()

    if request.method == "POST":

        form=CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Reacord was Created ")

            return redirect("dashboard")

    context={"form":form}

    return render(request,"webapp/create_record.html",context)

# Update Record

@login_required(login_url="login")
def update_record(request,pk):
    my_record=Record.objects.get(id=pk)

    form=UpdateRecordForm(instance=my_record)

    if request.method == "POST":

        form=UpdateRecordForm(request.POST,instance=my_record)

        if form.is_valid():

            form.save()

            messages.success(request, "Record Updated Successfully")

            return redirect("dashboard")
    
    
    context={"form":form,
             "record":my_record}

    return render(request, "webapp/update_record.html", context)


# Read Single Record

@login_required(login_url="login")
def View_record(request,pk):
   
    all_records=Record.objects.get(id=pk)

    return render(request,"webapp/view.html",{
        "record":all_records
    })

# Delete a Record

@login_required(login_url="login")
def delete_record(request,pk):
    record=Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Record Deleted!")

    return redirect("dashboard")




def logout(request):

    auth.logout(request)

    messages.success(request, "Logout Succeed!")

    return redirect("login")






