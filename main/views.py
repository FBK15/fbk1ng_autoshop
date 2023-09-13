from django.shortcuts import render

def stocks(request):
    car_data = {
        'name': 'Stargazer X',
        'manufacturer': 'Hyundai',
        'year': '2023',
        'price': '336.000.000',
        'amount': '2',
        'description': 'Bintang Baru Keluarga, Teman Terbaik Keluarga.',
    }

    return render(request, "main.html", car_data)

def developer(request):
    self_identity = {
        'developer_name': 'Asadilhaq Elqudsi Prabowo',
        'Class': 'PBP B',
    }

    return render(request, "developer.html", self_identity)