from django.contrib import admin
from django.urls import path, include

import Petstagram

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Petstagram.common.urls")),
    path('accounts/', include("Petstagram.accounts.urls")),
    path('pets/', include("Petstagram.pets.urls")),
    path('photos/', include("Petstagram.photos.urls")),

]
