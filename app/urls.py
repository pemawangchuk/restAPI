from django.urls import path

from app.views import HomeView, home, api_home, EmployeeDetail, EmployeeDetailSerializer, EmployeeListSerializer

urlpatterns = [
    path('withoutapi', home, name='home'),  # Home view
    path('api/', api_home, name='api_home'),  # API home view
    path('apiCDB/', HomeView.as_view(), name='api_home_class_based'),  # Class-based API home view
    path('api/employee/<int:id>/', EmployeeDetail.as_view(), name='employee_detail'),  # Employee detail view
    path('api/employee/serializer/<int:id>/', EmployeeDetailSerializer.as_view(), name='employee_detail_serializer'),  # Employee detail with serializer
    path('api/employee/list/', EmployeeListSerializer.as_view(), name='employee_list_serializer'),  # Employee list with serializer
]