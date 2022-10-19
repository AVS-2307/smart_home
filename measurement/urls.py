from django.urls import path
from measurement.views import *

urlpatterns = [
    path('sensors/', SensorView.as_view(), name='view_sensors'),
    path('sensors/create/', SensorCreateView.as_view(), name='create_sensors'),
    path('sensors/<int:pk>', SensorUpdateView.as_view(), name='update_sensors'),
    path('measurements/', MeasurementCreateView.as_view(), name='create_measurements'),
    path('sensors/detail/<int:pk>', SensorDetailView.as_view(), name='detail__info_sensors'),
]
