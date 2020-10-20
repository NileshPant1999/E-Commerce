from rest_framework import serializers


from .models import Item



class ItemSerializer(serializers.ModelSerializer):
	#url = serializers.HyperlinkedIdentityField(view_name='items_detail_api')
	class Meta:
		model = Item
		fields = [
			"title",
			"price",
            'category',
		]



#CREATE RETRIEVE UPDATE DESTROY