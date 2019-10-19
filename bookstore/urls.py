from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^add_book',views.add_book),
    url(r'^all_book',views.all_book),
    url(r'^update/(\d+)',views.update),
    url(r'^ultimal(\d+)',views.ultimal),
    url(r'^delete/(\d+)', views.delete),
    url(r'^test',views.test)

]