from django.shortcuts import render

# Create your views here.

def print_hello(request):
    return render(request,'index.html')

def greet(request):
    return render(request,'two.html')

def demo(request):
    student={
        'name':"Alan",
        'age':22,
        'place':"Kollam"
    }
    movies={
        'm_name':"Lokah",
        'm_year':2025,
        'm_summary':"Story of Neeli"
    }
    return render(request,'demo.html',student)
    # return render(request,'demo.html',movies)
    
def tags(request):
    subjects=["English","Science","Maths","Chemistry","GK"]
    fruits=["Grapes","Orange","Apple"]
    return render(request,'tags.html',{'subjects':subjects,'fruits':fruits,'marks':65})

def t_filter(request):
     return render(request,'filter.html',{'name':"Alan"})
    
    