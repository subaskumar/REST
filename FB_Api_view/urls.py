from django.contrib import admin
from django.urls import path,include
from apiApp import views
from rest_framework.routers import DefaultRouter

# Creating router object
router = DefaultRouter()
# register the router object
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.student_Api),
    # path('studentapi/<int:id>/', views.student_Api)

    # path('studentapi/<int:pk>/', views.StudentAPI_view.as_view()),
    # path('studentapi/', views.StudentAPI.as_view())
    
    # path('studentapi/<int:pk>/', views.Student_Re_Up_De.as_view()),
    # path('studentapi/', views.Student_Li_Cr.as_view())
    
    path('api', include(router.urls))
]
