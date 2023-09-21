# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Describe

# create a serializer class
class LocalSerializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Describe
		fields = ('id', 'description')
