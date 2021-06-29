from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo
from user.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from datetime import datetime
# Create your views here.

class TodoView(CreateAPIView):
    query_set = Todo.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = TodoSerializer

    def post(self, request, **args):
        if not request.user:
            response = {
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid user'
            }

            status_ = status.HTTP_400_BAD_REQUEST

        else:
            print('args', len(args))

            path_uid = args['user_id']

            if str(request.user.id) == str(path_uid):
                user = {'host': request.user.id}

                request.data.update(user)

                serializer_class = TodoSerializer(data=request.data)

                serializer_class.is_valid(raise_exception=True)

                serializer_class.save()

                response = {
                        'success': True,
                        'status_code': status.HTTP_200_OK ,
                        'message': 'Task created'
                    }

                status_ = status.HTTP_200_OK

            else:
                print(request.user.id, path_uid)
                response = {
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message': 'invalid user id'
                }

                status_ = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_)



class TodoRetrieveView(RetrieveAPIView):
    query_set = Todo.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = TodoSerializer

    def get(self, request, **args):
        if not request.user:
            response = {
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid user'
            }

            status_ = status.HTTP_400_BAD_REQUEST

        else:
            
            path_uid = args['user_id']

            if str(request.user.id) == str(path_uid):
                if len(args) > 1 and args['todo_id']:
                    task_id = args['todo_id']
                    todo_objects = Todo.objects.get(id=task_id)
                    data = {
                            'title': todo_objects.title,
                            'description': todo_objects.description,
                            'venue': todo_objects.venue,
                            'priority': todo_objects.priority,
                            'time': todo_objects.time,
                            'date': todo_objects.date
                        }

                    response = {
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': 'user task fetched!',
                        'data': data
                    }
                    status_ = status.HTTP_200_OK


                else:
                    todo_objects = Todo.objects.filter(host=path_uid)
                    todo_list = []
                    for todo_ in todo_objects:
                        data = {
                            'title': todo_.title,
                            'description': todo_.description,
                            'venue': todo_.venue,
                            'priority': todo_.priority,
                            'time': todo_.time,
                            'date': todo_.date
                        }
                        todo_list.append(data)


                    response = {
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': 'user task fetched!',
                        'data': todo_list
                    }

                    status_ = status.HTTP_200_OK

        return Response(response, status=status_)


    
    def delete(self, request, **args):
        if not request.user:
            response = {
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid user'
            }

            status_ = status.HTTP_400_BAD_REQUEST

        else:
            
            path_uid = args['user_id']

            if str(request.user.id) == str(path_uid):
                if len(args) > 1 and args['todo_id']:
                    task_id = args['todo_id']
                    
                    try:
                        todo_objects = Todo.objects.get(id=task_id)
                        todo_objects.delete()
                        response = {
                            'success': True,
                            'status_code': status.HTTP_200_OK,
                            'message': 'user task deleted!'
                        }
                        status_ = status.HTTP_200_OK
                    
                    except Exception as error:
                        response = {
                            'success': False,
                            'status_code': status.HTTP_400_BAD_REQUEST,
                            'message': 'error deleting task {}'.format(str(error)),
                        }

                        status_ = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_)


    def patch(self, request, **args):
        if not request.user:
            response = {
                'success': False,
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid user'
            }

            status_ = status.HTTP_400_BAD_REQUEST

        else:
            
            path_uid = args['user_id']

            if str(request.user.id) == str(path_uid):
                if len(args) > 1 and args['todo_id']:
                    task_id = args['todo_id']
                    
                    request.data.update({'host': path_uid})
                    
                    todo_objects = Todo.objects.get(host=path_uid, id=task_id)
                    serializer_class = TodoSerializer(todo_objects, data=request.data)
                    serializer_class.is_valid(raise_exception=True)
                    serializer_class.save()
                    response = {
                        'success': True,
                        'status_code': status.HTTP_200_OK,
                        'message': 'Todo updated successfully!'
                    }
                    
                    status_ = status.HTTP_200_OK

        return Response(response, status_)