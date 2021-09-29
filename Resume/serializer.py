from rest_framework.serializers import Serializer
from rest_framework import serializers
from Resume.models import Profile , Experience , Projects,Certification,Education, Skills


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['certificate_name','Certificate_url']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['company_name','ex_year_or_month']

class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
