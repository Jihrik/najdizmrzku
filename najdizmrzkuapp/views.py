from django.shortcuts import render, redirect
from .models import Store, Rating
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def home(request):
    stores = Store.objects.all()
    
    context = {'stores': stores}
    return render(request, 'najdizmrzkuapp/store_component.html', context)


def store_detail(request, pk):
    store = Store.objects.get(id=pk)
    ratings = store.ratings.all()
    rating_choices = range(1, 11)
    
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        rating_comment = request.POST.get('comment', '')
        
        if request.user.is_authenticated:
            existing_rating = Rating.objects.filter(
                store=store,
                user=request.user,
                rating=rating_value,
                comment=rating_comment.strip()
            ).exists()
            
            if not existing_rating:
                new_rating = Rating.objects.create(
                    store=store,
                    user=request.user,
                    rating=rating_value,
                    comment=rating_comment.strip()
                )
                new_rating.save()
            else:
                messages.error(request, 'You have already submitted the same rating.')
            
            return redirect('store-detail', pk=store.id)
        else:
            return redirect('login')    
    
    context = {
        'store': store,
        'ratings': ratings,
        "rating_choices": rating_choices,
    }
    return render(request, 'najdizmrzkuapp/store_detail.html', context)


def rating(request):
    ratings = Rating.objects.all()
    
    context = {
        "ratings": ratings,
    }
    return render(request, 'najdizmrzkuapp/ratings.html', context)


def profile(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user,
    }
    return render(request, 'najdizmrzkuapp/user_profile.html', context)


def login_page(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        # Correct authentication process
        user = authenticate(request, username=username, password=password)
        # authenticate() returns User object if username and password matches the DB otherwise -> None
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {'page': page}
    
    return render(request, 'najdizmrzkuapp/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Some error occured during registration')
    
    context = {'form': form}
    return render(request, 'najdizmrzkuapp/login_register.html', context)