from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Menu
from .forms import MenuForm

def index(request): # 메인 페이지
    menus = Menu.objects.all()
    context = {
        'menus':menus,
    }
    return render(request, 'menus/index.html', context)

def new(request):   # 생성 페이지
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menus:index')
    else:
        form = MenuForm()

    context = {
        'form': form,
    }
    return render(request, 'menus/new.html', context)

@require_POST
def delete(request, menu_pk):   # 삭제 페이지
    menu = Menu.objects.get(pk=menu_pk)
    menu.delete()
    return redirect('menus:index')