from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here.

# This Class Will Add and Show Items
class UserAddShowView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        # context = super().get_context_data(*args,**kwargs)
        context = super(UserAddShowView,self).get_context_data(*args,**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stu':stud, 'form':fm}
        return context
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            messages.success(request,'Data insert successful')
        return HttpResponseRedirect('/')

# This Class Will Update/Edit
class UserUpdateView(View):
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
        return render (request, 'update.html',{'form':form})
    def post(self,request,id):
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        messages.warning(request,'Data update successful !')
        return render (request, 'update.html',{'form':form})
        # return HttpResponseRedirect('/')

# This Class Will Delete Student
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        # print(kwargs[id])
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

# def delete_data(request, id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         pi.delete()
#         messages.error(request,'User delete successful !')
#         return HttpResponseRedirect('/')
