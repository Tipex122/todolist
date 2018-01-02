from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView

from todos import views as todos_views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('TodoList.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here

    # path('', views.index, name='home'),
    url(r'^$', todos_views.index, name='home'),

    # path('<int:pk>/todo_detail/', views.todo_detail, name='todo_detail'),
    url(r'^todo_detail/(?P<pk>[0-9]+)/$', todos_views.todo_detail, name='todo_detail'),

    # path('todo_new/', views.todo_new, name='todo_new'),
    url(r'^todo_new/$', todos_views.todo_new, name='todo_new'),

    # path('<int:pk>/todo_edit/', views.todo_edit, name='todo_edit'),
    url(r'^todo_edit/(?P<pk>[0-9]+)/$', todos_views.todo_edit, name='todo_edit'),

    # path('<int:pk>/todo_checked/', views.todo_checked, name='todo_checked'),
    url(r'^todo_checked/(?P<pk>[0-9]+)/$', todos_views.todo_checked, name='todo_checked'),

    # path('<int:pk>/todo_list_by_category/', views.todo_list_by_category, name='todo_list_by_category'),
    url(r'^todo_list_by_category/(?P<pk>[0-9]+)/$', todos_views.todo_list_by_category, name='todo_list_by_category'),

    # path('categories_list/', views.categories_list, name='categories_list'),
    url(r'^categories_list/$', todos_views.categories_list, name='categories_list'),

    # path('category_new/', views.category_new, name='category_new'),
    url(r'^category_new/$', todos_views.category_new, name='category_new'),

    # path('<int:pk>/category_edit/', views.category_edit, name='category_edit'),
    url(r'^category_edit/(?P<pk>[0-9]+)/$', todos_views.category_edit, name='category_edit'),

    # used by jquery search
    url(r'^suggest_todos/$', todos_views.suggest_todos, name='suggest_todos'),
    url(r'^auto_add_todo/$', todos_views.auto_add_todo, name='auto_add_todo'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
