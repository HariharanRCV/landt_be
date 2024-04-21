from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print('username: %s' % username)
        print('password: %s' % password)
        table_name = User._meta.db_table
        print("Table name: ", table_name)
        # Authenticate user
        users = User.objects.all()
        print("users: ",users)
        # Print all user data
        for user in users:
            print("User ID:", user.id)
            print("Username:", user.username)
            print("First Name:", user.first_name)
            print("Last Name:", user.last_name)
            print("Email:", user.email)
            print("Is Staff:", user.is_staff)
            print("Is Active:", user.is_active)
            print("Date Joined:", user.date_joined)
            print("---------------------------------------")
            print(type(username))
            if username == username and password == password:
            # User is authenticated
                return Response({"message": "Login successful", "type": "success"}, status=status.HTTP_200_OK)
            else:
                # Check if the username exists in the database
                if User.objects.filter(username=username).exists():
                    # Username exists, but password is incorrect
                    return Response({"message": "Invalid password", "type": "error"})
                else:
                    # Username does not exist in the database
                    return Response({"message": "Invalid username or password", "type": "error"})
    
        user = authenticate(username=username, password=password)
        print('user: ',user)
        
    
