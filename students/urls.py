from django.urls import path

from .views import (
    student_profile,
    students_detail_view,
    students_previous_school_detail_view,
    delete_students,
    delete_previous_school,
    students_previous_school_update_view,
    settings_update_form,
    settings_update_course,
    settings_update_majors,
    settings_update_campus,

    export_students,
    settings,

    delete_campus,
    delete_college,
    delete_majors,
    delete_course,
)


app_name = 'students'

urlpatterns = [
    path('student-profile/', student_profile, name = 'student_profile'),
    path('student-detail-view/<int:pk>/', students_detail_view, name = 'students_detail_view'),
    path('student-previous-school-detail-view/<int:pk>/', students_previous_school_detail_view, name = 'students_previous_school_detail_view'),
    path('student-delete-view/<int:pk>/', delete_students, name = 'delete_students'),
    path('delete-previous-school/<int:pk>/', delete_previous_school, name = 'delete_previous_school'),
    path('update-previous-school/<int:pk>/', students_previous_school_update_view, name = 'students_previous_school_update_view'),

    path('export-student-information', export_students, name = "export_students"),
    path('settings-page', settings, name = "settings"),
    path('update-settings-form/<int:pk>/', settings_update_form, name = 'settings_update_form'),
    path('update-settings-course/<int:pk>/', settings_update_course, name = 'settings_update_course'),
    path('update-settings-campus/<int:pk>/', settings_update_campus, name = 'settings_update_campus'),
    path('update-settings-majors/<int:pk>/', settings_update_majors, name = 'settings_update_majors'),

    path('delete-college/<int:pk>/', delete_college, name = 'delete_college'),
    path('delete-course/<int:pk>/', delete_course, name = 'delete_course'),
    path('delete-majors/<int:pk>/', delete_majors, name = 'delete_majors'),
    path('delete-campus/<int:pk>/', delete_campus, name = 'delete_campus'),

]
