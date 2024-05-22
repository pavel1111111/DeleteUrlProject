from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('texts/', views.TextViewSet.as_view({'get': 'list', 'post': 'create'}), name='text_list'),
    path('texts/<uuid:id>',  views.TextViewSet.as_view({'get': 'get_one'}), name='one_text'),
    path('texts/<uuid:id>/findurls',  views.TextViewSet.as_view({'get': 'find_urls'}), name='urls_from_text'),
    path('texts/<uuid:id>/deleteurls',  views.TextViewSet.as_view({'get': 'delete_urls'}), name='text-without_urls'),
    path('texts/<uuid:id>/deletetext',  views.TextViewSet.as_view({'delete': 'delete_text'}), name='delete_text_from_list')
]
