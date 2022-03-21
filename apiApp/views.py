# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from .serializers import StudentSerializer
# from .models import Student
# from rest_framework.response import Response
# from rest_framework import status
# Create your views here.


# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_Api(request,id=None):
#     if request.method == 'GET':
#         if id is None:
#             students = Student.objects.all()   
#             serializer_student = StudentSerializer(students,many=True)     
#             return Response(serializer_student.data)
#         else :
#             students = Student.objects.get(id=id) 
#             serializer_student = StudentSerializer(students)     
#             return Response(serializer_student.data)
            
#     if request.method == "POST":
#         #print(request.body)        # You cannot access body after reading from request's data stream, 
#                                     # it is already a stream data
                                    
#         print(request.data)         # {'name': 'Nalita Palai', 'roll': 3, 'city': 'BBSR'}
#         print(type(request.data))   # <class 'dict'>
#         serializer_data = StudentSerializer(data = request.data)
#         if serializer_data.is_valid():
#             serializer_data.save()
            
#             return Response({'msg': 'Data inserted sucessfully'})
        
#         return Response(serializer_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     if request.method == "PUT":
#         id  = request.data.get('id')
#         student = Student.objects.get(id=id)
#         serializer_data = StudentSerializer(student,data = request.data)
#         if serializer_data.is_valid():
#             serializer_data.save()
            
#             return Response({"msg": "Partial Update Sucessfully"})
#         return Response(serializer_data.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
#     if request.method == "PATCH":
#         id  = request.data.get('id')
#         student = Student.objects.get(id=id)
#         serializer_data = StudentSerializer(student,data = request.data,partial=True)
#         if serializer_data.is_valid():
#             serializer_data.save()
            
#             return Response({"msg": "completely Update Sucessfully"})
#         return Response(serializer_data.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     if request.method == "DELETE":
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response({"msg": "delete Sucessfully : %s and roll No: %i "%(student.name,student.roll)})



################################################### For API View class ##########################################################
# from .serializers import StudentSerializer
# from .models import Student
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView

# class StudentAPI(APIView):      # Here APIView is subclasses of Django view class
#     def get(self, request, id = None, format = None):   # Here request id DRF's request instance, but not Django's
#                                                         # HttpRequest instance
#         if id is None:
#             students = Student.objects.all()
#             serializer_student = StudentSerializer(students,many=True)
#             return Response(serializer_student.data)
#         else :
#             students = Student.objects.get(id=id) 
#             serializer_student = StudentSerializer(students)     
#             return Response(serializer_student.data)
        
        
#     def post(self,request, format = None):
#         #print(request.body)        # You cannot access body after reading from request's data stream, 
#                                     # it is already a stream data                          
#         print(request.data)         # {'name': 'Nalita Palai', 'roll': 3, 'city': 'BBSR'}
#         serializer_data = StudentSerializer(data = request.data)
#         if serializer_data.is_valid():
#             serializer_data.save()       
#             return Response({'msg': 'Data inserted sucessfully'})   
#         return Response(serializer_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     def put(self,request,format=None):
#         id  = request.data.get('id')
#         student = Student.objects.get(id=id)
#         serializer_data = StudentSerializer(student,data = request.data,partial=True)
#         if serializer_data.is_valid():
#             serializer_data.save()
#             return Response({"msg": "Partial Update Sucessfully"})
#         return Response(serializer_data.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     def patch(self, request, format=None):
#         id  = request.data.get('id')
#         student = Student.objects.get(id=id)
#         serializer_data = StudentSerializer(student,data = request.data)
#         if serializer_data.is_valid():
#             serializer_data.save()
#             return Response({"msg": "completely Update Sucessfully"})
#         return Response(serializer_data.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     def delete(self,request,id=None, format=None):
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response({"msg": "delete Sucessfully : %s and roll No: %i "%(student.name,student.roll)})
  
  
################################################### For Generic APIView class with Mixin class ##########################################################
      

#from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
#from rest_framework.generics import GenericAPIView


# class StudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self,request,*args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class StudentAPI_view(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self,request,*args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self,request,*args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


################################################### For Using Concrete View Classes ##########################################################

# from rest_framework.generics import (GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,
#                                      UpdateAPIView,DestroyAPIView,ListCreateAPIView, RetrieveUpdateAPIView,
#                                      RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)

# class Student_Re_Up_De(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    

# class Student_Li_Cr(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    

################################################### For ViewSets Classes ##########################################################

# from rest_framework.viewsets import  ViewSet,ModelViewSet
# class StudentViewSet(ViewSet):
    
#     def list(self,request):
#         students = Student.objects.all()
#         serializer_student = StudentSerializer(students,many=True)
#         return Response(serializer_student.data)
    
#     def retrieve(self, request, pk=None):
#         student = Student.objects.get(id=pk)
#         serializer_student = StudentSerializer(student)
#         return Response(serializer_student.data)
        
    
#     def create(self, request):
#         serializer_student = StudentSerializer(data = request.data)
#         if serializer_student.is_valid():
#             serializer_student.save()
#             return Response({'msg' : 'student created successfully'})
#         return Response(serializer_student.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     def update(self,request,pk=None):
#         student = Student.objects.get(id=pk)
#         serializer_student = StudentSerializer(student,data= request.data)
#         if serializer_student.is_valid():
#             serializer_student.save()
#             return Response({'msg' : 'student fully Updated successfully'})
#         return Response(serializer_student.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     def partial_update(self, request, pk=None):
#         student = Student.objects.get(id=pk)
#         serializer_student = StudentSerializer(student,data= request.data, partial=True)
#         if serializer_student.is_valid():
#             serializer_student.save()
#             return Response({'msg' : 'student partially Updated successfully'})
#         return Response(serializer_student.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
#     def delete(self,request,pk=None):
#         student = Student.objects.get(id=pk)
#         student.delete()
#         return Response({'msg': "student - %s Delete sucessfully"%(student.name)})
		

from rest_framework.viewsets import  ViewSet,ModelViewSet
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer      
    