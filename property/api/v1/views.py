
# property/api/v1/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PropertiesListSerializer, PropertiesDetailSerializer, ReservationsListSerializer
from property.models import Property, Reservation
from useraccount.models import User
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .forms import PropertyForm



class PropertiesListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = None
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.split('Bearer ')[1]
            try:
                validated_token = JWTAuthentication().get_validated_token(token)
                user = JWTAuthentication().get_user(validated_token)
            except Exception:
                pass

        favorites = []
        properties = Property.objects.all()

        # فیلترها
        is_favorites = request.GET.get('is_favorites', '')
        landlord_id = request.GET.get('landlord_id', '')
        country = request.GET.get('country', '')
        category = request.GET.get('category', '')
        checkin_date = request.GET.get('checkIn', '')
        checkout_date = request.GET.get('checkOut', '')
        bedrooms = request.GET.get('numBedrooms', '')
        guests = request.GET.get('numGuests', '')
        # bathrooms = request.GET.get('numBathrooms', '')
        buildingsmeter = request.GET.get('numBuildingsmeter', '')
        floorareameters =request.GET.get('numFloorareameters', '')

        if checkin_date and checkout_date:
            exact_matches = Reservation.objects.filter(start_date=checkin_date) | Reservation.objects.filter(end_date=checkout_date)
            overlap_matches = Reservation.objects.filter(start_date__lte=checkout_date, end_date__gte=checkin_date)
            all_matches = exact_matches | overlap_matches
            properties = properties.exclude(id__in=all_matches.values_list('property_id', flat=True))

        if landlord_id:
            properties = properties.filter(landlord_id=landlord_id)

        if is_favorites and user:
            properties = properties.filter(favorited__in=[user])

        if guests:
            properties = properties.filter(guests__gte=guests)

        if bedrooms:
            properties = properties.filter(bedrooms__gte=bedrooms)

        # if bathrooms:
        #     properties = properties.filter(bathrooms__gte=bathrooms)

        if buildingsmeter:
            properties = properties.filter(buildingsmeter__gte=buildingsmeter)


        if floorareameters:
            properties = properties.filter(floorareameters__gte=floorareameters)



        if country:
            properties = properties.filter(country=country)

        if category and category != 'undefined':
            properties = properties.filter(category=category)

        # جمع‌آوری علاقه‌مندی‌ها
        if user:
            favorites = properties.filter(favorited__in=[user]).values_list('id', flat=True)

        serializer = PropertiesListSerializer(properties, many=True)
        return Response({'data': serializer.data, 'favorites': favorites})








class PropertyDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'error': 'Property not found'}, status=404)

        serializer = PropertiesDetailSerializer(property)
        return Response(serializer.data)







class PropertyReservationsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'error': 'Property not found'}, status=404)

        reservations = property.reservations.all()
        serializer = ReservationsListSerializer(reservations, many=True)
        return Response(serializer.data)










class CreatePropertyView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        form = PropertyForm(request.data, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.landlord = request.user
            property.save()
            return Response({'success': True})
        else:
            return Response({'errors': form.errors}, status=400)






class BookPropertyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'error': 'Property not found'}, status=404)

        start_date = request.data.get('start_date', '')
        end_date = request.data.get('end_date', '')
        number_of_nights = request.data.get('number_of_nights', '')
        total_price = request.data.get('total_price', '')
        guests = request.data.get('guests', '')


        Reservation.objects.create(
            property=property,
            start_date=start_date,
            end_date=end_date,
            number_of_nights=number_of_nights,
            total_price=total_price,
            guests=guests,
            created_by=request.user
        )

        return Response({'success': True})






class ToggleFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'error': 'Property not found'}, status=404)

        if request.user in property.favorited.all():
            property.favorited.remove(request.user)
            return Response({'is_favorite': False})
        else:
            property.favorited.add(request.user)
            return Response({'is_favorite': True})
