from rest_framework.routers import SimpleRouter
from .views import LinksUser, LinksAll

router = SimpleRouter()
router.register('link_user', LinksUser)
router.register('links', LinksAll)

urlpatterns = []
urlpatterns += router.urls