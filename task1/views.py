from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game

def index(request):
    user_name = request.session.get('user_name', 'Гость')
    return render(request, 'fourth_task/index.html',
                  {'user_name': user_name})

def shop(request):
    items = Game.objects.all()
    return render(request, 'fourth_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'fourth_task/cart.html')

def games_view(request):
        games = Game.objects.all()
        context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']}
        return render(request, 'fourth_task/games.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.values_list('name', flat=True)
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                # Сохраняем нового пользователя в базу данных
                new_user = Buyer(name=username, balance=0.00, age=age)
                new_user.save()
                request.session['user_name'] = username
                return render(request, 'fourth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fourth_task/registration_page.html', info)


