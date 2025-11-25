from django.shortcuts import render

# Create your views here.
def grade_calculator(request):
    return render(request, 'calculator/grade_calculator.html')