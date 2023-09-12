from django.shortcuts import render

# Create your views here.
def AboutMe(request):
    return render(request, 'result/AboutMe.html')

def Interests(request):
    return render(request, 'result/Interests.html')

def Projects(request):
    return render(request, 'result/Projects.html')

def Skills(request):
    return render(request, 'result/Skills.html')