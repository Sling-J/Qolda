from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Star(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   count = models.IntegerField(default=0)
   liked = models.ManyToManyField(User, related_name='liked', blank=True)

   def __str__(self):
      return f'{self.user.username}'

   def add_star(self, ura):
      if ura in self.liked.all():
         self.count -= 1
         self.liked.remove(ura)
         self.save()
      else:
         self.count += 1
         self.liked.add(ura)
         self.save()



class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   position = models.CharField(max_length=100, blank=True)
   information = models.TextField(blank=True)
   img = models.ImageField(default='default.jpg', upload_to='user_images', blank=True)
   date_birth = models.DateField(null=True, blank=True)
   phone = models.IntegerField(null=True,blank=True)
   country = models.CharField(max_length=100, blank=True)
   city = models.CharField(max_length=100, blank=True)
   job = models.CharField(max_length=100, blank=True)
   star = models.IntegerField(default=0, null=True)

   def __str__(self):
      return f'Профиль пользователя {self.user.username}'


   # def get_absolute_url(self):
   #    return reverse('staff_detail_url', kwargs={'pk': self.pk})