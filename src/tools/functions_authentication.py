import config.base as CONFIG
from api.v1.services.services import ServicesService

# def check_service_permissions(service_name: str, end_point: str):
#     """Verifies if the service is authorized to use the requested EndPoint

#     Args:
#         service_name (str)
#         end_point (str)

#     Returns:
#         bool: [True] if valid permission, opposite case [False]
#     """
#     try:
#         permissions = CONFIG.SERVICE_PERMISSIONS[service_name]
#         for permission in permissions:
#             if permission == end_point:
#                 return True
#     except SystemError as e:
#         print(e)

#     return False


def valid_API_KEY(service: str, api_key: str) -> bool:
    """Validates if an API_KEY is authorized for the use of the API

    Args:

    Returns:
    """

    ServicesService().get_services()
    service_obj = CONFIG.API_KEYS.get(service)
    if service_obj:
        return api_key == service_obj.api_key
    return False


def valid_credentials(_request):

    is_valid_api_key = valid_API_KEY(
        service=_request.headers.get("Service"), api_key=_request.headers.get("Api-Key")
    )
    response = {
        "Success": is_valid_api_key,
        "Message": "API_KEY Valid" if is_valid_api_key else "Not API_KEY Valid",
        "Data": {},
    }
    return response
