from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request, 'input.html')

def result(request):
    input_image = request.GET.get('input')
    return render(request, 'result.html', {'input':input_image})

# def index(request):
#    return render(request, 'index.html')
