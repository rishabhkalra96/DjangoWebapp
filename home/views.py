# from django.http import HttpResponse
# from django.shortcuts import render
#
# # Create your views here.
#
#
# def home(request):
#     return render(request, 'home/home.html')
# The above method can also be implemented in a different way, by using class bsed views , implemented below
from django.shortcuts import render
from django.views.generic import TemplateView
from home.forms import HomeForm


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)
