from django.urls import path
from contas.views import home, new, list, update, delete

urlpatterns = [
    path('', home, name='home'),
    path('new/', new, name='url_new'),
    path('list/', list, name='url_list'),
    path('update/<int:pk>', update, name='url_update'),
    path('delete/<int:pk>', delete, name='url_delete')
]