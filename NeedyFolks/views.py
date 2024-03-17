from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Needy
from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    if request.method == 'GET':
        data = request.GET
        street_name = data.get('street_name', None)
        route_code = data.get('route_code', None)
        if route_code == None and street_name == None:
            needy = Needy.objects.all()
        elif street_name != None:
            needy = Needy.objects.filter(street_name=street_name)
        elif route_code != None:
            needy = Needy.objects.filter(route_code=route_code)
        else:
            needy = Needy.objects.all()
        # تعداد خانواده
        familyCount = needy.count()
        # تعداد افراد
        personCount = 0
        for family in needy:
            personCount += family.family_members_count
        # تعداد سرپرست زن
        numberOfFemaleGuardians = needy.filter(gender='زن').count()
        # تعداد سرپرست مرد
        numberOfMaleGuardians = needy.filter(gender='مرد').count()
        # تعداد تشیع
        ShiaCount = needy.filter(religion='تشیع').count()
        # تعداد تسنن
        SunniCount = needy.filter(religion='تسنن').count()
        # تعداد متاهل
        MarriedCount = needy.filter(marital_status='متاهل').count()
        # تعداد مجرد
        SingleCount = needy.filter(marital_status='مجرد').count()
        # تعداد بیوه
        WidowCount = needy.filter(marital_status='بیوه').count()
        # تعداد مطلقه
        numberOfDivorcedWomen = needy.filter(marital_status='مطلقه').count()
        statistics = {
            'needy': needy,
            'familyCount': familyCount,
            'personCount': personCount,
            'numberOfFemaleGuardians': numberOfFemaleGuardians,
            'numberOfMaleGuardians': numberOfMaleGuardians,
            'ShiaCount': ShiaCount,
            'SunniCount': SunniCount,
            'MarriedCount': MarriedCount,
            'SingleCount': SingleCount,
            'WidowCount': WidowCount,
            'numberOfDivorcedWomen': numberOfDivorcedWomen,

        }
        return render(request, 'index.html', statistics)


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


def details(request, id):
    if request.user.is_authenticated == False:
        return redirect('login')
    if request.method == 'GET':
        data = request.GET
        needy_id = id
        try:
            needy = Needy.objects.get(id=needy_id)
            statistics = {
                'needy': needy,
            }
            return render(request, 'details.html', statistics)
        except:
            return redirect('home_name')


def edit_needy(request):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        if request.method == 'POST':
            data = request.POST
            id = data.get('id')
            print(id)
            # دریافت نیازمند با استفاده از شناسه
            needy = Needy.objects.get(id=id)
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
            needy.name = name
            needy.last_name = last_name
            needy.father_name = father_name
            needy.national_code = national_code
            needy.gender = gender
            needy.family_members_count = family_members_count
            needy.phone_number = phone_number
            needy.referrer_name = referrer_name
            needy.marital_status = marital_status
            needy.religion = religion
            needy.job = job
            needy.coverage = coverage
            needy.street_name = street_name
            needy.address = address
            needy.save()
            # هدایت کاربر به صفحه دیگر (مثلاً به صفحه جزئیات نیازمند)
            return redirect('details_name', id=id)
    except Exception as e:
        print(e)
        return redirect('home_name')
