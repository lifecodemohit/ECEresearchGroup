from django.contrib import admin

# Register your models here.
from ece.models import homepage, News, News_image, createGroup, courseprerequisite, author, facultymem, courses, facultycoursecode, publications, Comingevent, Comingevent_image

class News_Imageinline(admin.StackedInline):
    model = News_image
    extra = 0
class NewsAdmin(admin.ModelAdmin):
    inlines = [News_Imageinline]

class Comingevent_Imageinline(admin.StackedInline):
    model = Comingevent_image
    extra = 0
class ComingeventAdmin(admin.ModelAdmin):
    inlines = [Comingevent_Imageinline]

#class Group_Pubinline(admin.StackedInline):
#    model = latestPub
#    extra = 0
#class GroupAdmin(admin.ModelAdmin):
#    inlines = [Group_Pubinline]

class courses_Pubinline(admin.StackedInline):
    model = courseprerequisite
    extra = 0
class courseAdmin(admin.ModelAdmin):
    inlines = [courses_Pubinline]

class faculty_Pubinline(admin.StackedInline):
    model = facultycoursecode
    extra = 0
class facultyAdmin(admin.ModelAdmin):
    inlines = [faculty_Pubinline]

class author_Pubinline(admin.StackedInline):
    model = author
    extra = 0
class authorAdmin(admin.ModelAdmin):
    inlines = [author_Pubinline]

admin.site.register(homepage)
admin.site.register(News, NewsAdmin)
#admin.site.register(createGroup, GroupAdmin)
admin.site.register(createGroup)
admin.site.register(courses, courseAdmin)
admin.site.register(facultymem, facultyAdmin)
admin.site.register(publications, authorAdmin)
admin.site.register(Comingevent, ComingeventAdmin)