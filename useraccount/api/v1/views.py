from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView, ListAPIView
from useraccount.models import User
from .serializers import UserDetailSerializer
from property.api.v1.serializers import ReservationsListSerializer

# اگر نیاز به فیلتر کردن مجوزها یا احراز هویت نداشته باشیم
class LandlordDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)



# لیست کردن رزروهای کاربر (درخواست رزروها)
class ReservationsListView(APIView):
    def get(self, request, *args, **kwargs):
        reservations = request.user.reservations.all()

        print('user:', request.user)
        print('reservations:', reservations)

       
        serializer = ReservationsListSerializer(reservations, many=True)
        return JsonResponse(serializer.data, safe=False)

        return JsonResponse({"message": "این ویو به درستی کار می‌کند!"}, safe=False)






# from django.http import JsonResponse
#
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
#
# from useraccount.models import User
# from .serializers import UserDetailSerializer

# from property.serializers import ReservationsListSerializer


# @api_view(['GET'])
# @authentication_classes([])
# @permission_classes([])
# def landlord_detail(request, pk):
#     user = User.objects.get(pk=pk)
#
#     serializer = UserDetailSerializer(user, many=False)
#
#     return JsonResponse(serializer.data, safe=False)


# @api_view(['GET'])
# def reservations_list(request):
#     reservations = request.user.reservations.all()
#
#     print('user', request.user)
#     print(reservations)
    
    # serializer = ReservationsListSerializer(reservations, many=True)
    # return JsonResponse(serializer.data, safe=False)

