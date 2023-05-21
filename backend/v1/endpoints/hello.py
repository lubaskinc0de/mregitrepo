from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

router = APIRouter()


class Foo:
    pass


@router.get("/hello/")
async def hello(foodep: Session = Depends()) -> str:
    return 'hello'
