from django.shortcuts import render
from django.views import View

class MainHomeView(View):
    
    def get(self, request):
        return render(request, 'main.html')