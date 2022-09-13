from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from lmsapp.models import Students, Books 

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    stu_book = BooksSerializer(read_only= True, many= True)
    class Meta:
        model = Students
        fields = '__all__'
