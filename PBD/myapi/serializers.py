from rest_framework import serializers

from .models import Post, Category, Tag, Author, User

# serializery objektów do jsonów dla wszystkich tabel, serializery dzielą się na te które dostajemy w metodzie GET oraz na te które wysyłamy w metodzie POST


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_on', 'category_posts')


class CategoryAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_on', 'tag_posts')


class TagAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Author
        fields = ('id', 'email', 'username', 'role', 'author_posts')


class PostAddSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Post
        fields = ('post_title', 'content', 'categories', 'tags', 'author')


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    tags = TagSerializer(many=True)
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ('id', 'post_title', 'content', 'categories',
                  'tags', 'author', 'created_on')
