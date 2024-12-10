import requests

from django.shortcuts import render
from django.views import View

class MainHomeView(View):
    
    def get(self, request):
        url = 'https://www.themealdb.com/api/json/v1/1/random.php'
        receitas = []

        for i in range(10):
            response = requests.get(url)

            if response.status_code == 200:

                dados = response.json()
                
                if dados.get('meals'):
                    receitas.append(dados['meals'][0])

        context = {'receitas': receitas}
        return render(request, 'main.html', context)