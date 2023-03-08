from django.shortcuts import render
from django.views import View
from .models import Student

# Create your views here.


class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html', {'studata':stu_data})
