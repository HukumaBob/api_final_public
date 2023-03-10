from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from . import serializers
from .permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """Viewset of posts."""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (AuthorOrReadOnly, IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Create record with current user."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset of groups."""
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """Viewset of comments."""
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AuthorOrReadOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Viewset of followers."""

    serializer_class = serializers.FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()
