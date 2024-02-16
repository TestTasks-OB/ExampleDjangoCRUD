from rest_framework import viewsets
from .models import Client, Request, Operator
from .serializers import ClientSerializer, RequestSerializer, OperatorSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_update(self, serializer):
        # Only allow updating of the status field by the Operator
        if 'processed_by' in serializer.validated_data:
            serializer.save(processed_by=self.request.user.operator)
        else:
            serializer.save()

class OperatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
