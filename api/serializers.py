from rest_framework import serializers
from base.models import Var, DOE, DOEvar, Varlevel, DOErun 

class VarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Var
        fields = '__all__'