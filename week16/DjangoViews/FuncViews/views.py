from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from .serialiers import FuncViewsSerializer


@api_view(["GET"])
def getEmployee_data(request):
    student_data = models.EmployeeData.objects.all()
    serialized_data = FuncViewsSerializer(student_data, many=True)
    return Response(data=serialized_data.data)


@api_view(["POST"])
def postEmployee_data(request):
    student_data = request.data
    serialized_data = FuncViewsSerializer(data=student_data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(status=status.HTTP_201_CREATED, data=serialized_data.data)
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serialized_data.errors)

@api_view(["PUT"])
def updateEmployee_data(request):
    employee_info = models.EmployeeData.objects.get(id=id)
    serializer = FuncViewsSerializer(employee_info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data})
    else:
        return Response({"status": "error", "data": serializer.errors})


@api_view(["DELETE"])
def deleteEmployee_data(request):
    result = models.EmployeeData.objects.get(id=id)
    result.delete()
    return Response({"status": "success", "data": "Record Deleted"})