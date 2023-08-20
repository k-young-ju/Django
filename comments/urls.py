from django.urls import path
from django.views.generic import TemplateView

from comments.views import CommentCreateView, CommentDeleteView

app_name = 'comment'

urlpatterns =[
    path('create/', CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]