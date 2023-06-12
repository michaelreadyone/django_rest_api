from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Var, DOE, DOEvar, Varlevel, DOErun 
from .serializers import VarSerializer

@api_view(['GET', 'POST'])
def VariableHandler(request):
    if request.method == 'GET':
        variables = Var.objects.all()
        serializer = VarSerializer(variables, many=True)
        return Response(serializer.data)
    else:
        serializer = VarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

