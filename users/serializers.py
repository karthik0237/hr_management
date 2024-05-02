from rest_framework.serializers import ModelSerializer

from users import models




class BaseUserSerializer(ModelSerializer):

    class Meta:
        fields = ['id','created_at','updated_at','is_active']
        fields_read_only = ['id','created_at','updated_at']



class DepartmentSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.Department
        fields = '__all__'



class CountrySerializer(BaseUserSerializer):
    
    class Meta:
        model = models.Country
        fields = '__all__'
        read_only_fields = BaseUserSerializer.Meta.fields_read_only + ['name_uc']

    def validate(self, attrs):

        if attrs.get('name', None):
            name = attrs.get('name')
            attrs['name_uc'] = str(name).upper()
        return super().validate(attrs)


class StateSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.State
        fields = '__all__'
        read_only_fields = BaseUserSerializer.Meta.fields_read_only + ['name_uc']
    
    def validate(self, attrs):

        if attrs.get('name', None):
            name = attrs.get('name')
            attrs['name_uc'] = str(name).upper()
        return super().validate(attrs)

    



class CitySerializer(BaseUserSerializer):
    
    class Meta:
        model = models.City
        fields = '__all__'
        read_only_fields = BaseUserSerializer.Meta.fields_read_only + ['name_uc']
    
    def validate(self, attrs):

        if attrs.get('name', None):
            name = attrs.get('name')
            attrs['name_uc'] = str(name).upper()
        return super().validate(attrs)



class UserSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.User
        fields = '__all__'


class UserBankdetailsSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserBankdetails
        fields = '__all__'


class FamilyMembersSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.FamilyMembers
        fields = '__all__'



class EduactionDetailsSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.EducationDetails
        fields = '__all__'


class UserExperienceSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserExperience
        fields = '__all__'


class UserGroupSerializer(BaseUserSerializer):
    
    class Meta:
        model = models.UserGroup
        fields = '__all__'




