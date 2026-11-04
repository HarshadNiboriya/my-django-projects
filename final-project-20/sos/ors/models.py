from django.db import models


class DropdownItem:
    def get_key(self):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError


class User(DropdownItem, models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login_id = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, default='')
    role_id = models.IntegerField(default='')
    role_name = models.CharField(max_length=50)

    def get_key(self):
        return self.id

    def get_value(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'sos_user'


class Role(DropdownItem, models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.name

    class Meta:
        db_table = "sos_role"


class College(DropdownItem,models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.name

    class Meta:
        db_table = 'sos_college'



class Course(DropdownItem,models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.name

    class Meta:
        db_table = 'sos_course'


class Subject(DropdownItem,models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)

    def get_key(self):
        return self.id

    def get_value(self):
        return self.name

    class Meta:
        db_table = 'sos_subject'


class Faculty(DropdownItem,models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    college_id = models.IntegerField()
    college_name = models.CharField(max_length=50)
    subject_id = models.IntegerField()
    subject_name = models.CharField(max_length=50)
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=50)

    def get_key(self):
        return self.id

    def get_value(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'sos_faculty'

class Student(DropdownItem,models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    college_id = models.IntegerField()
    college_name = models.CharField(max_length=50)

    def get_key(self):
        return self.id

    def get_value(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'sos_student'

class Marksheet(models.Model):
    roll_number = models.CharField(max_length=50)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_marksheet'






