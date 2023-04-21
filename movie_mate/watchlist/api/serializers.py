from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform, Review



class ReviewSerializer(serializers.ModelSerializer):

    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist',)


class WatchListSerializer(serializers.ModelSerializer):

    len_title = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

    def get_len_title(self,object):
        return len(object.title)

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("title should be different from description")
        else:
            return data

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("title is too short")
        else:
            return value
        

class StreamPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"


# class WatchListSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()


#     def create(self, validated_data):
#         return WatchList.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name should be different from description")
#         else:
#             return data

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value