import datetime

from django.contrib.auth.models import Group, User

from rest_framework import serializers

from fiber.models import Cable, Panel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='get_full_name', required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ['pk', 'url', 'username', 'email', 'password', 'first_name', 'last_name', 'name', 'groups', 'is_staff']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group
        fields = ['pk', 'url']


class CableSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cable
        fields = [
            'location', 'fiber_strand_count', 'strand_config',
            'other_strand_config', 'cable_type', 'other_cable_type',
            'infrastructure_class', 'foot_stamp_units', 'foot_stamp_number',
            'manufacturer', 'other_manufacturer',
            'manufacturer_catalog_number', 'date', 'owner', 'other_owner',
            'installer', 'other_installer', 'comments'
        ]
    
    def create(self, validated_data):
        cable = Cable.objects.create(
            location=validated_data['location'],
            fiber_strand_count=validated_data['fiber_strand_count'],
            strand_config=validated_data['strand_config'],
            other_strand_config=validated_data.get('other_strand_config', None),
            cable_type=validated_data['cable_type'],
            other_cable_type=validated_data.get('other_cable_type', None),
            infrastructure_class=validated_data['infrastructure_class'],
            foot_stamp_units=validated_data['foot_stamp_units'],
            foot_stamp_number=validated_data['foot_stamp_number'],
            manufacturer=validated_data['manufacturer'],
            other_manufacturer=validated_data.get('other_manufacturer', None),
            manufacturer_catalog_number=validated_data['manufacturer_catalog_number'],
            date=validated_data['date'],
            owner=validated_data['owner'],
            other_owner=validated_data.get('other_owner', None),
            installer=validated_data['installer'],
            other_installer=validated_data.get('other_installer', None),
            comments=validated_data.get('comments', None)
        )
        return cable


class PanelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Panel
        fields = [
            'location', 'owner', 'other_owner', 'mount_type',
            'installation_type', 'location_type', 'card_rows', 'card_columns',
            'slot_orientation', 'ports_per_card', 'port_type',
            'other_port_type', 'installation_date', 'installer',
            'other_installer', 'model', 'other_model', 'comments'
        ]
    
    def create(self, validated_data):
        panel = Panel.objects.create(
            location=validated_data['location'],
            owner=validated_data['owner'],
            other_owner=validated_data.get('other_owner', None),
            mount_type=validated_data['mount_type'],
            installation_type=validated_data['installation_type'],
            location_type=validated_data['location_type'],
            card_rows=validated_data['card_rows'],
            card_columns=validated_data['card_columns'],
            slot_orientation=validated_data['slot_orientation'],
            ports_per_card=validated_data['ports_per_card'],
            port_type=validated_data['port_type'],
            other_port_type=validated_data.get('other_port_type', None),
            installation_date=validated_data['installation_date'],
            installer=validated_data['installer'],
            other_installer=validated_data.get('other_installer', None),
            model=validated_data['model'],
            other_model=validated_data.get('other_model', None),
            comments=validated_data.get('comments', None)
        )
        return panel
