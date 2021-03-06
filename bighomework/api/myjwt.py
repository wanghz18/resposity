import jwt
from rest_framework_jwt.settings import api_settings


def create_jwt(username, password):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    user = {'username': username, 'password': password}
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token