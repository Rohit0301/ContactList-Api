from rest_framework import serializers
from .models import Contact
class ContactSerializer(serializers.ModelSerializers):

    class Meta:
        model=Contact
        fields=['country_code','first_name','last_name','phone_number','contact_picture','is_favourite']