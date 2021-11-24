from typing import Any

from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def to_json_tip(message: str, code: int = -1) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': code,
            'message': message
        }
    )


def to_json(data: Any, code: int = 0) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': code,
            'message': "Success",
            'data': jsonable_encoder(data),
        }
    )
