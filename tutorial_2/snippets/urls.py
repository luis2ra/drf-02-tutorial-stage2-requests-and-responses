from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

'''
Adding optional format suffixes to our URLs.

To take advantage of the fact that our responses are no longer hardwired to a 
single content type let's add support for format suffixes to our API endpoints. 
Using format suffixes gives us URLs that explicitly refer to a given format, 
and means our API will be able to handle URLs such as 
http://example.com/api/items/4.json.

'''