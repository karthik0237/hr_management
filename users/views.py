from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin,\
                                    DestroyModelMixin
from rest_framework.routers import DefaultRouter

from users.models import *
from users.serializers import *


# Create your views here.
class DepartmentViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer




class CountryViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class StateViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = State.objects.all()
    serializer_class = StateSerializer



class CityViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = City.objects.all()
    serializer_class = CitySerializer




class UserViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer



class FamilyMembersViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = FamilyMembers.objects.all()
    serializer_class = FamilyMembersSerializer



class EducationDetailsViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = EducationDetails.objects.all()
    serializer_class = EducationDetailsSerializer



class UserExperienceViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = UserExperience.objects.all()
    serializer_class = UserExperienceSerializer



class UserBankdetailsViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = UserBankdetails.objects.all()
    serializer_class = UserBankdetailsSerializer



class UserGroupViewset(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
                  DestroyModelMixin, GenericViewSet):
    
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer



router = DefaultRouter()

router.register('users', UserViewset, basename = 'user')
router.register('usergroups', UserGroupViewset, basename = 'usergroup')
router.register('countries', CountryViewset, basename = 'country')
router.register('states', StateViewset, basename = 'state')
router.register('cities', CityViewset, basename = 'city')
router.register('userexperience', UserExperienceViewset, basename = 'userexperience')
router.register('userbankdetails', UserBankdetailsViewset, basename = 'userbankdetails')
router.register('familymembers', FamilyMembersViewset, basename = 'familymember')
router.register('eduacationdetails', EducationDetailsViewset, basename = 'educationdetails')
router.register('departments', DepartmentViewset, basename = 'department')










    
    
