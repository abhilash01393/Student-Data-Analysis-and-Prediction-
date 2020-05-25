# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administator(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    admin_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password_admin = models.CharField(max_length=64)
    department = models.ForeignKey('Department', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administator'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Class(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING)
    class_id = models.IntegerField(primary_key=True)
    session_info = models.CharField(max_length=1)
    professor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class'


class Course(models.Model):
    couse_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=64)
    campus = models.CharField(max_length=64)
    department = models.ForeignKey('Department', models.DO_NOTHING)
    available_session = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'course'


class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Professor(models.Model):
    professor_id = models.IntegerField(primary_key=True)
    professor_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    campus = models.CharField(max_length=64)
    work_role = models.CharField(max_length=64)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    password_professor = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'professor'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    campus = models.CharField(max_length=64)
    session_enrolled = models.IntegerField()
    department = models.ForeignKey(Department, models.DO_NOTHING)
    student_password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'student'


class StudentGrades(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING)
    grade_id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    score = models.FloatField()

    class Meta:
        managed = False
        db_table = 'student_grades'