from django.shortcuts import render, redirect
from crupapp.forms import UserForm
from django.http import HttpResponse
from crupapp.models import User

# Insert the data 💥💥💥💥
def insert(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                # return HttpResponse("<h1>Data Successfully Saved</h1>")
                return redirect('/show')
            except:
                pass
    form=UserForm()
    return render(request,'index.html',{'form':form})


# Get the Data in a Table 💥💥💥💥
def show(request):
    users=User.objects.all()
    return render(request,'show.html', {'users':users})


# Delete the Data from the table 💥💥💥💥
def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('/show')


# Update the data 💥💥💥💥
def update(request,id):
    user=User.objects.get(id=id)
    return render(request,'update.html',{'user':user})