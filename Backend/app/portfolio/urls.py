from django.urls import path

from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("skills/", views.SkillListView.as_view()),
    path("techs/", views.TechListView.as_view()),
    path("works/", views.WorkListView.as_view()),
    path("person/", views.PersonListView.as_view()),
]
#
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()