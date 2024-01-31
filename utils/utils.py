from fastapi import HTTPException
import getpass


def get_user(request):
    if request is None:
        raise HTTPException(status_code=400, detail="Request object is None")

    if not hasattr(request, "headers"):
        raise HTTPException(status_code=400, detail="Invalid request object")

    auth_user = request.headers.get('auth_user')

    if not auth_user:
        auth_user = getpass.getuser()
    return auth_user