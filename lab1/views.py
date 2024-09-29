from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseBadRequest,
                         HttpResponseNotFound)
from lab1.models import Book, Student
from lab1.forms import BookForm, StudentForm, DelStudentForm
from django.shortcuts import get_object_or_404

def home(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        color = request.GET.get('color')
        return render(request, 'student.html',
                      {'name': name, 'program': 'Software Engineer', 'course': 1, 'group': 1, "color": color})
    else:
        return HttpResponseNotAllowed


def home_color(request, color):
    if request.method == 'GET':
        return render(request, 'student.html',
                      {'name': 'Ivan', 'program': 'Software Engineer', 'course': 1, 'group': 1, "color": color})
    else:
        return HttpResponseNotAllowed


def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        form = BookForm()

        return render(request, 'books.html', context={'books': books, 'form': form})
    elif request.method == 'POST':
        book = Book()
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.save()
        return HttpResponseRedirect('/books')

    elif request.method == 'DELETE':
        pass

    elif request.method == 'PUT':
        pass


def students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        form = StudentForm()

        return render(request, 'students.html', context={'students': students, 'form': form})
    elif request.method == 'POST':
        student = Student()
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.save()
        return HttpResponseRedirect('/students')


def delete_student(request, student_id):
    if request.method == 'POST':
        # student_id = int(request.POST.get('id'))
        student = Student.objects.filter(id=student_id)
        student.delete()
        return HttpResponseRedirect('/students')


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'GET':
        # student = Student.objects.filter(id=student_id).first()
        form = StudentForm(instance=student)
        return render(request, 'update_student.html', context={'form': form})
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse('Студент успешно обновлен', status=200)
        return HttpResponse('Новые данные не прошли валидацию', status=400)
    # Если метод не POST
    return HttpResponseNotAllowed(['POST'], 'Метод запроса должен быть POST')


def add_books(request):
    pass
