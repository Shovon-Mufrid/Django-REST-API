from django.urls import path
from django.urls.conf import include
from MyApp.views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contact', ContactViewSet, basename='contact')
urlpatterns = [
        path('', include(router.urls), )
]

# 4,5
# from rest_framework.urlpatterns import format_suffix_patterns
# from MyApp import views

# app_name = 'MyApp'

# urlpatterns = format_suffix_patterns([
#     # path('', views.api_root),
#     path('list/', views.ContactList.as_view()),
#     # path('list/', views.ContactList.as_view(), name='contact-list'),
#     path('details/<int:pk>/', views.ContactDetail.as_view()),
#     # path('list/', views.api_list),
#     # path('details/<int:pk>/', views.api_detail),
# ])