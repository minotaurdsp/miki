from . import views
from django.urls import  path

app_name = 'pages'

urlpatterns = [
    path(
        '', views.IndexView.as_view(), name='index'
    ),
    path(
        '<int:page_id>/', views.detail, name='detail'
    ),
    path(
        'edit/<int:pk>/', views.PageEdit.as_view(), name='edit'
    ),
    path(
        'create', views.PageCreate.as_view(), name='create'
    )
]