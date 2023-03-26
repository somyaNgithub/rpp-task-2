from django.shortcuts import render
from portfolio.models import visitor_note

def portfolio(request):
    if request.method == "POST":
        fn = request.POST.get('full_name')
        em = request.POST.get('email')
        mn = request.POST.get('mob_number')
        emsb = request.POST.get('email_subject')
        m = request.POST.get('message')
    
        temp = visitor_note(full_name=fn,email=em,mob_number=mn,email_subject=emsb,message=m)
        temp.save()
    return render(request, 'index.html')
