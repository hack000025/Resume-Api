from django.contrib import admin
from Resume.models import Education,Experience,Projects,Certification,Profile ,Skills
from . import models




class ProjectAdmin(admin.ModelAdmin):
    list_display = ['live_projects','personal','project_name','langauges','role','description','project_url']

admin.site.register(Projects,ProjectAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company_name','ex_year_or_month']

admin.site.register(Experience,ExperienceAdmin)



class EducationAdmin(admin.ModelAdmin):
    list_display = ['college_name','stream','percentage','subject','Passout_Date']

admin.site.register(Education,EducationAdmin)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ['certificate_name','Certificate_url']

admin.site.register(Certification,CertificationAdmin)


class SkillsAdmin(admin.ModelAdmin):
    list_display = ['Programming_lang']

admin.site.register(Skills,SkillsAdmin)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','Name','sex','phone','email','city','zip','state','country','job_title']

admin.site.register(Profile,ProfileAdmin)
