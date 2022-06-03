from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentData
from .serialiers import ClassViewsSerializer


class StudentEntries(APIView):

    def get(self, request):
        student_data = StudentData.objects.all()
        serialized_data = ClassViewsSerializer(student_data, many=True)
        return Response(data=serialized_data.data)

    def post(self, request):
        student_data = request.data
        serialized_data = ClassViewsSerializer(data=student_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(status=status.HTTP_201_CREATED, data=serialized_data.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized_data.errors)