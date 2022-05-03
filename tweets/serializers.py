from importlib.resources import contents
from django.conf import settings
from rest_framework import serializers
from tweetSNS.settings import TWEET_ACTION_OPTIONS
from .models import Tweet
from profiles.serializers import PublicProfileSerializer

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS

class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for tweets")
        return value

class TweetCreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True) #serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['user','id','content','likes', 'timestamp']
    
    def get_likes(self, obj):
        return obj.likes.count()
    
    def validate_content(self, content):
        if len(content) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return content

    # def get_user(self, obj):
    #     return obj.user.id


class TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['user','id','content','likes','is_retweet','parent','timestamp']
    
    def get_likes(self, obj):
        return obj.likes.count()
    
    # def get_user(self, obj):
    #     return obj.user.id