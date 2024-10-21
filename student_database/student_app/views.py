from django.shortcuts import render, get_object_or_404
from .models import Student

# View for the student list page
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})

# View for individual student details
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_app/student_detail.html', {
        'name': student.name,
        'student_id': student.student_id,
        'course': student.course,
        'join_date': student.join_date,
    })
