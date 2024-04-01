from rest_framework.authentication import TokenAuthentication as base_authentication

class TokenAuthentication(base_authentication):
    keyword = "Bearer"