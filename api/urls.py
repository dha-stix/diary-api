
from django.urls import path
from .views import Users, User, EditUpdateNote,ViewUserNotes, ViewNotes, AddCreateNote, ViewUserNote
urlpatterns = [
    path('users/', Users.as_view(), name="users"),
    path('user/<int:pk>/', User.as_view(), name="user"),
    path('note/edit/<int:pk>/', EditUpdateNote.as_view(), name="edit-note"),
    path('note/view/', ViewNotes.as_view(), name="view-note"),
    path('mynote/view/', ViewUserNotes.as_view(), name="view-notes"),
    path('mynote/view/<int:pk>/', ViewUserNote.as_view(), name="view-note"),
    path('note/create/', AddCreateNote.as_view(), name="createuser-note"),

]
