import requests

from django.shortcuts import render
from django.views import View

class MainHomeView(View):
    
    def get(self, request):
        url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata'
        response = requests.get(url)

        if response.status_code == 200:

            dados = response.json()
            receita = dados['meals'][0]

            context = {
                'nome': receita['strMeal'],
                'categoria': receita['strCategory'],
                'instrucoes': receita['strInstructions'],
            }

        return render(request, 'main.html', context)