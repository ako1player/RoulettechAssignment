from rest_framework import routers
from TodoBackend.TodoBackend.viewsets import TodoViewSet

router = routers.SimpleRouter()

router.register(r'todo', TodoViewSet, basename="todo")

urlpatterns = router.urls