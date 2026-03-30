from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from matching_app.views.index import index
from matching_app.views.login import login_view
from matching_app.views.signup import signup
from matching_app.views.user_profile import user_home

urlpatterns = (
    [
        path("", index, name="index"),
        path("signup/", signup, name="signup"),
        path("login/", login_view, name="login"),
        path("home/", user_home, name="user_home"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
