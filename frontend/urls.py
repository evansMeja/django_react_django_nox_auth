from django.urls import path

from .views import index, TodoDetailView
from django.conf import settings

urlpatterns = [
    path('', index),
    path('edit/<int:pk>', TodoDetailView.as_view()),
    path('delete/<int:pk>', TodoDetailView.as_view()),
]



react_routes = getattr(settings, 'REACT_ROUTES', [])

for route in react_routes:
    urlpatterns += [
        path('{}'.format(route), index)
    ]


