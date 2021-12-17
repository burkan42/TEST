from django.shortcuts import render

def result(request):
    return render(request, "output/result.html")
    # 'desc':desc