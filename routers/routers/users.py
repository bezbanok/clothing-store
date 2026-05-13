from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter()


class UserCreate(BaseModel):
    """Данные для регистрации пользователя."""

    name: str = Field(description="Имя пользователя")
    email: str = Field(description="Электронная почта пользователя")
    password: str = Field(description="Пароль пользователя")


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Зарегистрировать пользователя",
    description="Создает учетную запись пользователя интернет-магазина."
)
def register_user(user: UserCreate):
    if "@" not in user.email:
        raise HTTPException(status_code=400, detail="Некорректный адрес электронной почты")

    return {
        "message": "Пользователь успешно зарегистрирован",
        "name": user.name,
        "email": user.email
    }


@router.get(
    "/profile/{user_id}",
    summary="Получить профиль пользователя",
    description="Возвращает данные профиля пользователя по его идентификатору."
)
def get_profile(user_id: int):
    return {
        "user_id": user_id,
        "name": "Пользователь",
        "email": "user@example.com"
    }
