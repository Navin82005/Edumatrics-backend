from django.urls import path
from .views import (
    InternalMark,
)

urlpatterns = [
    path("students/marks/iit/me", InternalMark.as_view(), name="internal_marks")
]
