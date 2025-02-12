from rest_framework import generics, permissions, viewsets
from food.models import Food, FoodSection, FoodComment, FoodCategory, FoodLike
from .serializers import (
    FoodSerializer, FoodCreateUpdateSerializer,
    FoodCommentSerializer, FoodCommentCreateSerializer,
    FoodCategorySerializer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .permissions import IsAuthorOrReadOnly



# Food Views
class FoodCreateView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]




class FoodDetailView(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'




class FoodUpdateView(generics.UpdateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise PermissionDenied("شما اجازه ویرایش این غذا را ندارید.")
        serializer.save()



# Food Comment Views
class FoodCommentCreateView(generics.CreateAPIView):
    queryset = FoodComment.objects.all()
    serializer_class = FoodCommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class FoodCommentListView(generics.ListAPIView):
    queryset = FoodComment.objects.all()
    serializer_class = FoodCommentSerializer
    permission_classes = [permissions.AllowAny]




class FoodCommentDetailView(generics.RetrieveAPIView):
    queryset = FoodComment.objects.all()
    serializer_class = FoodCommentSerializer
    permission_classes = [permissions.AllowAny]




class FoodCommentUpdateView(generics.UpdateAPIView):
    queryset = FoodComment.objects.all()
    serializer_class = FoodCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionDenied("شما اجازه ویرایش این نظر را ندارید.")
    
        serializer.save()



# Food Like and Visit Views
class FoodVisitCountView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, food_id):
        food = get_object_or_404(Food, id=food_id)
        food.view_count += 1
        food.save()
        return Response({'view_count': food.view_count})



class FoodLikeCountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, food_id):
        food = get_object_or_404(Food, id=food_id)
        user = request.user
        like, created = FoodLike.objects.get_or_create(food=food, user=user)
        if not created:
            like.liked = not like.liked
            like.save()
        else:
            like.liked = True
            like.save()
        like_count = FoodLike.objects.filter(food=food, liked=True).count()
        return Response({'like_count': like_count})




# Food Category ViewSet
class FoodCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
