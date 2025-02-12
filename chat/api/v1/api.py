from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from chat.models import Conversation, ConversationMessage
from .serializers import ConversationListSerializer, ConversationDetailSerializer, ConversationMessageSerializer, ConversationSerializer

from useraccount.models import User


@api_view(['GET'])
def conversations_list(request):
    serializer = ConversationListSerializer(request.user.conversations.all(), many=True)

    return JsonResponse(serializer.data, safe=False)




@api_view(['GET'])
def conversations_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)

    conversation_serializer = ConversationDetailSerializer(conversation, many=False)
    messages_serializer = ConversationMessageSerializer(conversation.messages.all(), many=True)

    return JsonResponse({
        'conversation': conversation_serializer.data,
        'messages': messages_serializer.data
    }, safe=False)



@api_view(['GET'])
def conversations_start(request, user_id):
    conversations = Conversation.objects.filter(users__in=[user_id]).filter(users__in=[request.user.id])

    if conversations.count() > 0:
        conversation = conversations.first()
        
        return JsonResponse({'success': True, 'conversation_id': conversation.id})
    else:
        user = User.objects.get(pk=user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.users.add(user)

        return JsonResponse({'success': True, 'conversation_id': conversation.id})













# conversation with admin
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def conversations_with_admin(request):
    # پیدا کردن ادمین (فرض می‌کنیم فقط یک ادمین داریم)
    admin_user = User.objects.filter(is_staff=True).first()
    if not admin_user:
        return JsonResponse({'success': False, 'error': 'Admin user not found.'}, status=404)
    
    # بررسی اینکه آیا مکالمه‌ای بین کاربر و ادمین وجود دارد یا خیر
    conversations = Conversation.objects.filter(users=admin_user).filter(users=request.user)
    
    if conversations.exists():
        conversation = conversations.first()
    else:
        # ایجاد مکالمه جدید
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.users.add(admin_user)
    
    # سریال‌سازی مکالمه با استفاده از ConversationDetailSerializer
    conversation_serializer = ConversationDetailSerializer(conversation, many=False)
    
    return JsonResponse({'success': True, 'conversation': conversation_serializer.data})












