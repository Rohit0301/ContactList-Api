from django.urls import path
from .views import ContactListView,ContactDetailView

urlpatterns=[
 path('',ContactListView.as_view())
 path('<int:id>/',ContactDetailView.as_view())
]