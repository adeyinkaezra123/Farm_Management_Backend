from django.urls import path
from .views import *
urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view()),
    path('list', ListInventory.as_view()),
    path('create_invt', CreateInventory.as_view()),
    path('delete_invt/<int:pk>', DeleteInventory.as_view()),
    path('list_bmgt', ListBarnMgt.as_view()),
    path('createBM', CreateBarnMgt.as_view()),
    path('delete_BM/<int:pk>', DeleteBarnMgt.as_view()),
    path('list_profile', ListProfiles.as_view()),
    path('createProfile', CreateProfile.as_view()),
]