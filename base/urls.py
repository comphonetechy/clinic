from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patient-form/', views.patient_form, name='patient-form'),
    path('patient-details/<int:pk>', views.patient_details, name='patient-details'),
    path('patient-form-update/<int:pk>', views.patient_form_update, name='patient-form-update'),
    path('patient-delete/<int:pk>', views.delete_patient, name='delete-patient'),
    path('patient-diagnosis/<int:pk>', views.patient_diagnosis, name='patient-diagnosis'),
]
