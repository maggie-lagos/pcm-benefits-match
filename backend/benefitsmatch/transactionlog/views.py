from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]  
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	#  can override action methods like create(), update(), or destroy() to add custom logic.