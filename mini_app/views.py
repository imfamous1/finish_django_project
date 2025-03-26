import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from finish.mini_app.models import User


# Create your views here.
@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data('user_id')
            username = data('username', '')
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')

            user, created = User.objects.update_or_create(
                user_id=user_id,
                default={
                    'username': username,
                    'first_name': first_name,
                    'last_name': last_name
                }
            )

            return JsonResponse({
                'status': 'success',
                'user_id': user.user_id,
                'created': created
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


def get_all_users(request):
    if request.method == 'GET':
        users = User.object.all()
        users_list = []

        for user in users:
            users_list.append({
                'user_id': user.user_id,
                'user_name': getattr(user, 'username', ''),
                'first_name': getattr(user, 'first_name', ''),
                'last_name': getattr(user, 'last_name', '')
            })

        return JsonResponse({
            'users': users_list
        })