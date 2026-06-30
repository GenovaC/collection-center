from pydantic import BaseModel


class LoginInput(
    BaseModel
):

    user_name: str