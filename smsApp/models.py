from django.db import models


class Staff(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	username = models.CharField(primary_key=True, max_length=20)
	email = models.EmailField(unique=True)
	phone = models.IntegerField()
	date_of_birth = models.CharField(max_length=20)
	date_of_employment = models.DateField()


class FormClass(models.Model):
    form_class = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.form_class}'


class Subject(models.Model):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.subject}'


class Resources(models.Model):
    form_class = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    lesson_plan = models.FileField(upload_to="lesson_plans/")
    lesson_note = models.FileField(upload_to="lesson_notes/")
    assessment_question = models.FileField(upload_to="assessments")
    exam_question = models.FileField(upload_to="examination")


class Student(models.Model): 
    sex = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    ]
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    classes = [
        ('JS1', 'JS1'),
        ('JS2', 'JS2'),
        ('JS3', 'JS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3'),
    ]
    last_name = models.CharField(max_length=20)
    form_class = models.CharField(max_length=10, choices=classes) 
    date_of_birth = models.CharField(max_length=20)
    year_admitted = models.IntegerField()
    gender = models.CharField(max_length=10, choices=sex)