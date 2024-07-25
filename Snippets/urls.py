from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('snippets/my', views.my_snippets, name="my-snippets"),
    path('snippets/<int:snippet_id>', views.snippet_detail, name="snippet-detail"),
    path('snippets/<int:snippet_id>/edit', views.snippet_edit, name="snippet-edit"),
    path('snippets/<int:snippet_id>/delete', views.snippet_delete, name="snippet-delete"),
    path('comments/add', views.comments_add, name='comments_add'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.create_user, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
