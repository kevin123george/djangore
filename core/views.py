from datetime import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from .forms import UserRegForm, PostForm
# Create your views here.
from django.views import View
from .models import Post


class SignupView(View):
    form_class = UserRegForm
    initial = {'key': 'value'}
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print("sdfsdfsdfsdfsd")
        print(form)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            print(form)
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class Index(View):
    form_class = PostForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        aut = request.user.pk
        print(aut)
        form = self.form_class(initial=self.initial)
        return render(request, 'index.html', {'form': form,
                                              'aut': aut})

    def post(self, request, *args, **kwargs):
        aut = request.user.pk
        form = self.form_class(request.POST, request.FILES)
        print(form)
        form.save()
        form = self.form_class(initial=self.initial)
        return render(request, 'index.html', {'form': form,
                                              'aut': aut})


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class ArticleListView(ListView):
    model = Post
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class PostDelete(DeleteView):
    model = Post
    success_url = '/'
