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
            other_strand_config=validated_data['other_strand_config'],
            cable_type=validated_data['cable_type'],
            other_cable_type=validated_data['other_cable_type'],
            infrastructure_class=validated_data['infrastructure_class'],
            foot_stamp_units=validated_data['foot_stamp_units'],
            foot_stamp_number=validated_data['foot_stamp_number'],
            manufacturer=validated_data['manufacturer'],
            other_manufacturer=validated_data['other_manufacturer'],
            manufacturer_catalog_number=validated_data['manufacturer_catalog_number'],
            date=validated_data['date'],
            owner=validated_data['owner'],
            other_owner=validated_data['other_owner'],
            installer=validated_data['installer'],
            other_installer=validated_data['other_installer'],
            comments=validated_data['comments']
        )
        return cable


# class StorySerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Story
#         fields = ['pk', 'story', 'title', 'description', 'date']

#     def create(self, validated_data):
#         story = Story.objects.create(
#             story=validated_data['story'],
#             uploaded_by=self.context['request'].user,
#             title=validated_data.get('title', ''),
#             description=validated_data.get('description', ''),
#         )
#         if 'date' in validated_data:
#             story.date = validated_data['date']
#             story.save()
#         return story


# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#     date = serializers.DateField(required=False)

#     class Meta:
#         model = Image
#         fields = ['pk', 'image', 'title', 'description', 'date']
    
#     def create(self, validated_data):
#         image = Image.objects.create(
#             image=validated_data['image'],
#             uploaded_by=self.context['request'].user,
#             title=validated_data.get('title', ''),
#             description=validated_data.get('description', ''),
#         )
#         if 'date' in validated_data:
#             image.date = validated_data['date']
#             image.save()
#         return image


# class VideoSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Video
#         fields = ['pk', 'video', 'title', 'description', 'date']
    
#     def create(self, validated_data):
#         video = Video.objects.create(
#             video=validated_data['video'],
#             uploaded_by=self.context['request'].user,
#             title=validated_data.get('title', ''),
#             description=validated_data.get('description', ''),
#         )
#         if 'date' in validated_data:
#             video.date = validated_data['date']
#             video.save()
#         return video


# class AudioSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Audio
#         fields = ['pk', 'audio', 'title', 'description', 'date']

#     def create(self, validated_data):
#         audio = Audio.objects.create(
#             audio=validated_data['audio'],
#             uploaded_by=self.context['request'].user,
#             title=validated_data.get('title', ''),
#             description=validated_data.get('description', ''),
#         )
#         if 'date' in validated_data:
#             audio.date = validated_data['date']
#             audio.save()
#         return audio
