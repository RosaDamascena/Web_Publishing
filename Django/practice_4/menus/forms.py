from django import forms
from .models import Menu

# python에서 class의 이름을 정의하는 name convention은
# 파스칼 케이스다....ModelForm
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        