import jwt
import os

ALGORITHM = 'HS256'


class JwtService:
    @staticmethod
    def encode(**kwargs) -> str:
        secret_key = os.environ['SECRET_KEY']
        token = jwt.encode(kwargs, secret_key, algorithm=ALGORITHM)

        return token

    @staticmethod
    def decode(
            *,
            token: str
    ) -> dict:
        pass
        secret_key = os.environ['SECRET_KEY']
        decoded_payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        return decoded_payload
