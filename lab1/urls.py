from django.urls import path
from lab1.views import home, home_color, books, students, delete_student, update_student

urlpatterns = [
    path('home', home, name='home'),
    path('home/<str:color>/', home_color, name='home_color'),
    path('books/', books, name='books'),
    path('students/', students, name='students'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
    path('update_student/<int:student_id>/', update_student, name='update_student'),
    # path('update_student/', update_student, name='update_student_post')
]