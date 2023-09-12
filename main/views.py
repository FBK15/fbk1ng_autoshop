from django.shortcuts import render

def stocks(request):
    context = {
        'name': 'Stargazer X',
        'manufacturer': 'Hyundai',
        'year': '2023',
        'price': '336.000.000',
        'amount': '2',
        'description': 'Bintang Baru Keluarga, Teman Terbaik Keluarga.',
    }

    return render(request, "main.html", context)
# Create your views here.
