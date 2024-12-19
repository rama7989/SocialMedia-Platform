from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, PostViewSet, CommentViewSet, LikeViewSet, FollowViewSet

router = DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)
router.register('follows', FollowViewSet)

urlpatterns = router.urls
