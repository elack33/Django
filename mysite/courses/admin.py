from django.contrib import admin

from courses.models import Department, Faculty, Student, Course

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)

class FacutlyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Faculty, FacutlyAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)



