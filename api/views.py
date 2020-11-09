from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import UserCreateSerializer, NoteSerializer
from users.models import CustomUser, Note
from rest_framework.filters import SearchFilter, OrderingFilter
class Users(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()

class User(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()

class EditUpdateNote(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    def get_queryset(self):
        user = self.request.user.id
        return Note.objects.filter(user=user)

class AddCreateNote(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    def get_queryset(self):
        user = self.request.user.id
        return Note.objects.filter(user=user)

class ViewNotes(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

class ViewUserNotes(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title')
    def get_queryset(self):
        user = self.request.user.id
        return Note.objects.filter(user=user)

class ViewUserNote(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    def get_queryset(self):
        user = self.request.user.id
        return Note.objects.filter(user=user)







