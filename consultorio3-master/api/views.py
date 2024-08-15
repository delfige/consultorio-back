from rest_framework import viewsets
from .models import CustomUser, Role, Speciality, MedicalReport, Appointment
from .serializers import CustomUserSerializer, CustomUserCreateUpdateSerializer, RoleSerializer, SpecialitySerializer, MedicalReportSerializer, AppointmentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser, Role, Speciality, MedicalReport, Appointment
from .serializers import CustomUserSerializer, CustomUserCreateUpdateSerializer, RoleSerializer, SpecialitySerializer, MedicalReportSerializer, AppointmentSerializer



class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CustomUserCreateUpdateSerializer
        return CustomUserSerializer

class MedicalReportViewSet(viewsets.ModelViewSet):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer



    @action(detail=False, methods=['get'], url_path='professional/(?P<professional_id>\d+)')
    def by_professional(self, request, professional_id=None):
        """Filtra las citas por el profesional dado"""
        appointments = self.queryset.filter(professional_id=professional_id)
        serializer = self.get_serializer(appointments, many=True)
        return Response(serializer.data)