from django.contrib import admin
from lmsapp.models import Students, Books
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'status','course','department','address','email','contact','gender','last_name','middle_name','first_name']
admin.site.register(Students, StudentAdmin)

class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','student', 'description','author','publisher','date_published','delete_flag','date_added','date_created']
admin.site.register(Books, BooksAdmin)