from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('Startbildschirm.html', views.start, name='startbildschirm'),

    path('', views.start, name='start'),
    path('AnleitungSchritte.html', views.anleitungsschritt, name='anleitungschritte'),
    path('a', views.add, name='neueAnleitung'),
    path('Entwurf_gespeichert.html', views.entwurf_gespeichert, name='anleitungalsentwurfbeendet'),
    path('Anleitung_gespeichert_und_hochgeladen.html', views.anleitung_gespeichert_und_hochgeladen, name='anleitungGespeichert'),
    

    path('Anleitung_durchgehen.html', views.anleitung_durchgehen, name='ersteSeiteanleitungdurchgehen'),
    path('Anleitung_durchgehen2.html', views.anleitung_durchgehen2, name='zweiteSeiteanleitungdurchgehen'),
    path('Anleitung_durchgehen3.html', views.anleitung_durchgehen3, name='dritteSeiteanleitungdurchgehen'),
    path('Anleitung_durchgehen4.html', views.anleitung_durchgehen4, name='vierteSeiteanleitungdurchgehen'),
    path('Anleitung_durchgehen5.html', views.anleitung_durchgehen5, name='fünfteSeiteanleitungdurchgehen'),
    path('Anleitung_durchgehen6.html', views.anleitung_durchgehen6, name='sechsteSeiteanleitungdurchgehen'),
    

    path('Mein_Profil.html', views.profil, name='meinProfil'),

    path('Meine_Anleitungen.html', views.meine_anleitungen, name='persanleitungen'),

    path('Anleitung_durchgehen.html', views.MyView.as_view()),


    # Redundant Views in generic views written
    # Anleitung Durchgehen

    path('Anleitung_durchgehen/<int:pk>', views.AnleitungViews.as_view(), name='anleitungdurchgehen'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)