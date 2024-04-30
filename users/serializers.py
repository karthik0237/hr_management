from rest_framework.serializers import ModelSerializer

from users import models




class BaseSerializer(ModelSerializer):

    class Meta:
        fields = ['id','created_at','updated_at','is_active']
        fields_read_only = ['id','created_at','updated_at']

class DepartmentSerializer(BaseSerializer):
    
    class Meta:
        model = models.Department
        fields = '__all__'


class CountrySerializer(BaseSerializer):
    
    class Meta:
        model = models.Country
        fields = '__all__'

class StateSerializer(BaseSerializer):
    
    class Meta:
        model = models.State
        fields = '__all__'

class CitySerializer(BaseSerializer):
    
    class Meta:
        model = models.City
        fields = '__all__'

class UserSerializer(BaseSerializer):
    
    class Meta:
        model = models.User
        fields = '__all__'


class UserBankdetailsSerializer(BaseSerializer):
    
    class Meta:
        model = models.UserBankdetails
        fields = '__all__'


class FamilyMembersSerializer(BaseSerializer):
    
    class Meta:
        model = models.FamilyMembers
        fields = '__all__'



class EduactionDetailsSerializer(BaseSerializer):
    
    class Meta:
        model = models.EducationDetails
        fields = '__all__'


class UserExperienceSerializer(BaseSerializer):
    
    class Meta:
        model = models.UserExperience
        fields = '__all__'


class UserGroupSerializer(BaseSerializer):
    
    class Meta:
        model = models.UserGroup
        fields = '__all__'




