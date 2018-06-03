from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'hello adi','number':200}
    return render(request,'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
