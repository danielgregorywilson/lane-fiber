from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import include, path

# from api.views import RegisterView, UploadImageView, UploadStoryView, UploadVideoView, UploadAudioView
from fiber.api_views import (
    CurrentUserView, GroupViewSet, SubmitCableView, SubmitPanelView,
    UserViewSet, 
    # AudioViewSet, ImageViewSet, StoryViewSet,
    # VideoViewSet,
    # EmployeeViewSet, FileUploadViewSet,
    # PerformanceReviewViewSet, ReviewNoteViewSet, SignatureViewSet, 
)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('v1/current-user/', CurrentUserView.as_view(), name='current_user'),
    path('submit-cable/', SubmitCableView.as_view(), name='submit_cable'),
    path('submit-panel/', SubmitPanelView.as_view(), name='submit_panel'),
    # path('register/', RegisterView.as_view(), name='auth_register'),
    # path('upload-image/', UploadImageView.as_view(), name='upload_image'),
    # path('upload-story/', UploadStoryView.as_view(), name='upload_story'),
    # path('upload-video/', UploadVideoView.as_view(), name='upload_video'),
    # path('upload-audio/', UploadAudioView.as_view(), name='upload_audio'),
]

router = routers.DefaultRouter(trailing_slash=False)
router.register('v1/user', UserViewSet)
# router.register('v1/groups', GroupViewSet)
# router.register('v1/images', ImageViewSet)
# router.register('v1/stories', StoryViewSet)
# router.register('v1/videos', VideoViewSet)
# router.register('v1/audio', AudioViewSet)
# router.register('v1/employee', EmployeeViewSet)
# router.register('v1/performancereview', PerformanceReviewViewSet)
# router.register('v1/fileupload', FileUploadViewSet, basename='fileupload')
# router.register('v1/signature', SignatureViewSet)
# router.register('v1/reviewnote', ReviewNoteViewSet)

urlpatterns = router.urls + urlpatterns
