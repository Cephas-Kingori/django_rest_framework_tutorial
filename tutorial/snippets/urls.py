from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),

    #serialzer 2
    path('snippets2/', views.snippet_list),
    path('snippets2/<int:pk>/', views.snippet_detail),

    #serializer 3
    path('snippets3/', views.SnippetList.as_view()),
    path('snippets3/<int:pk>/', views.SnippetDetail.as_view()),

    #serializer 3mixin1
    path('snippets3mixins1/', views.SnippetListMixins1.as_view()),
    path('snippets3mixins1/<int:pk>/', views.SnippetDetailMixins1.as_view()),

        #serializer 3generic
    path('snippets3generic/', views.SnippetListGeneric.as_view()),
    path('snippets3generic/<int:pk>/', views.SnippetDetailGeneric.as_view()),

    # Part 4
    path('snippets4/', views.SnippetListGeneric4.as_view()),
    path('snippets4/<int:pk>/', views.SnippetDetailGeneric4.as_view()),

    path('api-auth/', include('rest_framework.urls')),

    # part 5
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),

    path('snippets5/', views.SnippetListGeneric4.as_view(), name='snippet-list'),
    path('snippets5/<int:pk>/', views.SnippetDetailGeneric4.as_view(),   name='snippet-detail'),

    path('snippets5/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

]

############## Part 6 ####################

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns += [
        # part 6
    path('apisnippets6', api_root),
    path('snippets6/', snippet_list, name='snippet-list'),
    path('snippets6/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets6/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users6/', user_list, name='user-list'),
    path('users6/<int:pk>/', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


########################## part 7###############################
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns += [
    path('snippets7/', include(router.urls)),
]

