from django.shortcuts import render
# Create your views here.
def page1 (request):
    data='this is a semi dynamic web application'
    d={'output':data}
    return render(request,'page1.html',context=d)
