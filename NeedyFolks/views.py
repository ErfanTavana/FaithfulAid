from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Needy
from django.shortcuts import render, redirect


def register_needy(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    if request.method == 'POST':
        data = request.POST
        name = data.get('name').strip()
        last_name = data.get('last_name').strip()
        father_name = data.get('father_name').strip()
        national_code = data.get('national_code').strip()
        gender = data.get('gender').strip()
        family_members_count = data.get('family_members_count').strip()
        phone_number = data.get('phone_number').strip()
        referrer_name = data.get('referrer_name').strip()
        marital_status = data.get('marital_status').strip()
        religion = data.get('religion').strip()
        job = data.get('job').strip()
        coverage = data.get('coverage').strip()
        street_name = data.get('street_name').strip()
        address = data.get('address').strip()
        needy = Needy.objects.create(name=name, last_name=last_name, father_name=father_name,
                                     national_code=national_code, gender=gender,
                                     family_members_count=family_members_count, phone_number=phone_number,
                                     referrer_name=referrer_name, marital_status=marital_status, religion=religion,
                                     job=job, coverage=coverage, street_name=street_name, address=address)
        needy.save()
        return render(request, 'form.html')
    else:
        return render(request, 'form.html')
