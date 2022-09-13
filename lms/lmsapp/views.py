from lmsapp.models import Students, Books
from lmsapp.serializers import StudentSerializer, BooksSerializer
from rest_framework import generics 

# Create your views here.

class Student_info(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()

class Student_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Students.objects.all()

class Books_info(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class Books_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
