from django.shortcuts import render,redirect
from .models import Food,Consume
from django.contrib.auth.decorators import login_required
from . forms import RegisterForm
from django.contrib import messages
# Create your views here.
@login_required
def index(request):
    if request.method=="POST":
        food_consumed=request.POST['food_consumed']
        consume=Food.objects.get(name=food_consumed)
        user=request.user
        consume=Consume(user=user,food_consumed=consume)
        consume.save()
        foods=Food.objects.all()
    
    else:
        foods=Food.objects.all()
    consumed_foods=Consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':foods,'consumed_foods':consumed_foods})

@login_required
def delete_consume(request, id):
    consumed_food=Consume.objects.get(id=id)
    if request.method=="POST":
        consumed_food.delete()
        return redirect('/myapp')
    return render(request,'myapp/delete.html')

@login_required
def profilepage(request):
    return render(request,'myapp/profile.html')

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created :)')
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'myapp/register.html',{'form':form})