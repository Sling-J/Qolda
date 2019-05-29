from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect

def index(request):
    return render(request, 'professions/index.html')

def all(request):
   users = User.objects.all()
   if request.method == 'POST':
      user_id = request.POST.get('user_id')
      person = User.objects.get(id=user_id)
      person.star.add_star(request.user)
      return redirect('professions:all')

   return render(request, 'professions/all.html',{'users': users})

