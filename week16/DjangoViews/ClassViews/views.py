from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentData
from .serialiers import ClassViewsSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

"""
view created to get all the student entries
"""


class StudentEntries(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        student_data = StudentData.objects.all()
        serialized_data = ClassViewsSerializer(student_data, many=True)
        return Response(data=serialized_data.data)


"""
view created to create a student entre
"""


class CreateStudentEntries(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request):
        student_data = request.data
        serialized_data = ClassViewsSerializer(data=student_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(status=status.HTTP_201_CREATED, data=serialized_data.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized_data.errors)


"""
view created to update a student entre
"""


class UpdateStudentEntries(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def put(self, request, id):
        student_info = StudentData.objects.get(id=id)
        serializer = ClassViewsSerializer(student_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


"""
view created to partly update a student entre
"""


class ParUpdateStudentEntries(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def patch(self, request, id):
        student_info = StudentData.objects.get(id=id)
        serializer = ClassViewsSerializer(student_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


"""
view created to delete a  student entre
"""


class DeleteStudentEntries(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def delete(self, request, id=None):
        result = StudentData.objects.get(id=id)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"})
