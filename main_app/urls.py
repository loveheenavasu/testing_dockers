from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router = DefaultRouter()


# router.register(r'role', AssignRole, basename='role'),
# router.register(r'user/edit', UserEdit, basename='register'),
router.register(r'company', CompanyDetails, basename='company'),
router.register(r'menu', MenuDetails, basename='Menu_get'),
router.register(r'menu-category', MenuCategoryDetails, basename='menu_category'),
router.register(r'items', ItemsDetails, basename='menu_item_get'),
router.register(r'addon/category', AddonCategoryDetails, basename='addonCategory'),
router.register(r'addon/item', AddonItemsDetails, basename='addon_item'),
# router.register(r'room/edit', RoomEdit, basename='room_edit'),
# router.register(r'room', RoomGet, basename='room'),
router.register(r'room', RoomDetails, basename='room'),
router.register(r'guest', Guest, basename='guest'),
router.register(r'hotel', HotelDetails, basename='hotel'),
router.register(r'standard', StandardDetails, basename='standard'),
router.register(r'quick-link', GetQuickLinks, basename='quick-link'),
router.register(r'update-quick-link', UpdateQuickLinks, basename='update-quick-link'),


urlpatterns = [
     # path('user/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('', include(router.urls)),
     # path('menu_category/', GetMenuCategory.as_view(), name="menu_category"),
     # Room  CRUD
     # path('room/update/<int:id>/', views.room_put, name="update"),
     # path('room/delete/<int:id>/', views.room_delete, name="delete"),
     path('get-menu-category', GetMenuCategory.as_view(), name="get-menu-category"),
     path('image-link', ImageLink.as_view(), name="image-link"),
     path('flat_files_upload', FlatDataUpload.as_view(), name="flat_files_upload"),
     path('qr_code', Qrdata.as_view(), name="qr_code"),

]
# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL,
#                            document_root=settings.MEDIA_ROOT)
