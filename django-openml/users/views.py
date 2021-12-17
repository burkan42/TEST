from django.shortcuts import render, redirect
import document
import requests
# from document import getElementById
from .forms import MyForm
def dashboard(request):

    if request.method == 'POST':
        form = MyForm(request.POST)
        
        if form.is_valid():
            print ("valid! from views.py")
            for fieldname in form.cleaned_data:
                field = form.cleaned_data[fieldname]
                print(fieldname)
                print(field)
            # suite_id = form.cleaned_data['suite_id']
            # flow1 = form.cleaned_data['flow1']
            # flow2 = form.cleaned_data['flow2']
            # print(suite_id)
            # desc = suite_id

            # query = {'lat':'45', 'lon':'180'}
            # response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
            # responseData =response.json()['response']
            # for d in responseData:
            #     time = d['risetime']
            #     print("p")
            return redirect("output")

    else:
        form = MyForm()
    return render(request, "users/dashboard.html",{'form':form,})
    # 'desc':desc

def resultpage(request):
    return render(request, 'output/result.html')