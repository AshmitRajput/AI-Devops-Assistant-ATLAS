from django.urls import path

from accounts.views.register import (
    RegisterView
)

from accounts.views.profile import (
    ProfileView
)

urlpatterns = [

    path(
        "register/",
        RegisterView.as_view()
    ),

    path(
        "profile/",
        ProfileView.as_view()
    ),

]