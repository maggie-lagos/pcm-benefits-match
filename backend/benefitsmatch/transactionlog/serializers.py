from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ['id','date', 'vendor', 'customer', 'purchase_total', 'snap', 
                  'wicsenior', 'match_snap', 'match_wicsenior','cash_credit']
		
        # can handle validation here too