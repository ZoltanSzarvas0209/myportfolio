from django.urls import path
from portfolio.views import edit_comment, delete_comment

urlpatterns = [
    path('edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]