from django.urls import path, include
from . import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="My API", default_version="1.0.0", description="Documentation for my API"
    ),
    public=True,
)

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("api_login/", views.LoginView.as_view()),
    path("logout/", views.logout_page),
    path("catalog/", views.catalog),
    path("order/", views.order),
    path("", views.index),
    path("books/", views.BookPostListCreate.as_view(), name="book-view-create"),
    path("cost/<int:add>", views.BookAPI.as_view()),
    path("books/<int:pk>", views.BookRetrieveUpdateDestroy.as_view(), name="update"),
    path("tinymce/", include("tinymce.urls")),
    path("post/", views.code),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("schedule/", views.schedule_task, name="schedule"),
    path("test/", views.test_cel, name="schedule"),
]
