from django.shortcuts import render, redirect
from phone.forms import PhoneForm as PF
from phone.models import Phone
from django.db.models import F

def add_phone(request):
    if request.method == 'POST':
        form = PF.phoneform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PF.phoneform()
    return render(request, '../templates/add_phone.html', {'form': form})
def success(request):
    return render(request, '../templates/success.html')

def phone_search_results(request):
    search_query = request.GET.get('search_query')
    if search_query:
        phones = Phone.objects.filter(brand_name__icontains=search_query)
    else:
        phones = Phone.objects.all()
    return render(request, 'phone_search_results.html', {'phones': phones})
def phone_search_results2(request):
    brand_name = request.GET.get('brand_name')
    brand_nationality = request.GET.get('brand_nationality')
    country_of_manufacture = request.GET.get('country_of_manufacture')
    flag = request.GET.get('flag')
    phones = Phone.objects.all()

    if brand_name:
        phones = phones.filter(brand_name__icontains=brand_name)
    if brand_nationality:
        phones = phones.filter(brand_nationality__icontains=brand_nationality)
    if country_of_manufacture:
        phones = phones.filter(country_of_manufacture__icontains=country_of_manufacture)
    if not brand_name and not brand_nationality and not country_of_manufacture:
        phones = Phone.objects.all()
    if flag:
        phones = phones.filter(brand_nationality__icontains=F('country_of_manufacture'))

    return render(request, 'phone_search_results.html', {'phones': phones})

def search(request):
    form = PF.SearchForm()
    phones = None

    if request.method == 'POST':
        form = PF.SearchForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            if brand:
                phones = Phone.objects.filter(brand_name=brand)

    return render(request, 'phone_search.html', {'form': form, 'phones': phones})

def advanced_search(request):
    form = PF.SearchForm2()
    if request.method == 'POST':
        form = PF.SearchForm2(request.POST)
    return render(request, 'advanced_search.html', {'form': form})