from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import ModelForm
from django import forms
from .models import Page
from django.views.generic import  ListView
from django.db.models import Q


class IndexView(ListView):
    model = Page
    template_name = "pages/index.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query:
            pages_list = Page.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
            print("search ",pages_list)
        else:
            pages_list = Page.objects.order_by('-created')[:5]

            print("else   ",pages_list)

        return pages_list


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

