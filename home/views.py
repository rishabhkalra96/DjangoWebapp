# from django.http import HttpResponse
# from django.shortcuts import render
#
# # Create your views here.
#
#
# def home(request):
#     return render(request, 'home/home.html')
# The above method can also be implemented in a different way, by using class bsed views , implemented below
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from home.forms import HomeForm
from home.models import Post, Friend
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-date')
        users = User.objects.exclude(id=request.user.id)
        args = {'form': form, 'posts': posts, 'users': users}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            text = form.cleaned_data['post']
            post.save()
            return redirect('home:home')
        text = form.cleaned_data['post']
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def change_friends(request, operation, pk):
    new_friend = User.objects.get(pk=pk)

    if operation == 'add':
        Friend.make_friend(request.user,new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, pk=pk)

    return redirect('home:home')
