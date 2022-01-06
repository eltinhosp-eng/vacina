from rest_framework.routers import DefaultRouter
from .views import VacinaViewSet, PessoaViewSet, NotificacaoViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'vacinas', VacinaViewSet)
router.register(r'pessoas', PessoaViewSet)
router.register(r'notificacoes', NotificacaoViewSet)

urlpatterns = router.urls
