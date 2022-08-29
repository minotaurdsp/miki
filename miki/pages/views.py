from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import ModelForm
from django import forms
from .models import Page


def index(request):
    pages_list = Page.objects.order_by('-created')[:5]
    context = {
        'pages_list': pages_list,
    }
    return render(request, 'pages/index.html', context)


def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'pages/detail.html', {'page': page})


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['title','content','author','is_published','linked_page']
        
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)


class PageCreate(PermissionRequiredMixin,CreateView):
    model = Page
    form_class = PageForm
    template_name = "pages/create_form.html"
    permission_required = ('pages.add_page')    
    raise_exception = True


class PageEdit(PermissionRequiredMixin,UpdateView):
    model = Page
    form_class = PageForm
    template_name = "pages/update_form.html"
    permission_required = ('pages.change_page')    
    raise_exception = True

