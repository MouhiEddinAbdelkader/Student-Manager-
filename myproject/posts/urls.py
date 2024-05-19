from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'
urlpatterns = [
    path('', views.Postes_Listes, name='listes'),
    path('stages_list', views.Stages_list, name='stages_list'),
    path('stage-edit/<int:id>/', views.edit_stage, name='stage-edit'),
    path('stage-delete/<int:pk>/', views.StageDeleteView.as_view(), name='stage-delete'),
    path('ajouter/', views.CreerStage.as_view(), name='creer_stage'),
    path('ajouterEvenClub/', views.creerEvenClub.as_view(), name='creer_EvenClub'),
    path('like-post', views.like_post, name='like-post'),
    path('even_club_list', views.EvenClub_list, name="evenclublist"),
    path('new-post/', views.post_new, name='new-post'),
    path('<slug:slug>', views.Poste_page, name='poste_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

