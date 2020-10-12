from django.urls import include, path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('/',views.index, name='aoi'),
    path('/<int:aoi_id>/', views.one_aoi, name='one_aoi'),


    path('/addAOI',views.addAOI, name='addAoi'),
    path('/addPost',views.addPost, name='addPost'),
    path('/del_post',views.del_post, name='del_post'),
    path('/search_results',views.search_res, name='search_res'),


#url(r'^admin/', admin.site.urls)
#url(r'^$',) // URL for homepage
     ]