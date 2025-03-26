import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mini_app.models import User


# Create your views here.
@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            username = data.get('username', '')
            first_name = data.get('first_name')
            last_name = data.get('last_name')

            user, created = User.objects.update_or_create(
                user_id=user_id,
                defaults={
                    'username': username,
                    'first_name': first_name,
                    'last_name': last_name
                    # Другие поля можно оставить по умолчанию
                }
            )
            return JsonResponse({
                'status': 'success',
                'user_id': user.user_id,
                'created': created
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_list = []

        for user in users:
            users_list.append({
                'user_id': user.user_id,
                'username': user.username,
                'first_name': getattr(user, 'first_name', ''),
                'last_name': getattr(user, 'last_name', '') # Функция getattr() здесь используется как безопасный способ обращения к полям модели, которые могут быть не заполнены или отсутствовать.
            })

        return JsonResponse({'users': users_list})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
