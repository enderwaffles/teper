
#app
#auth
#security.py

from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import Header, HTTPException

from datetime import datetime, timedelta
from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError

def hash_password(password: str) -> str:
    return generate_password_hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return check_password_hash(hashed, password)


secretkey = "хомяки"
algorithm = "HS256"
token_access_time = 1000

def create_token(user_id: int) -> str:
    now = datetime.utcnow()
    expire = now + timedelta(minutes=token_access_time)
    
    data = {
        "sub": str(user_id), 
        "exp": int(expire.timestamp()),
        }
    
    token = jwt.encode(data, secretkey, algorithm=algorithm)
    return token

def decode_token(token: str) -> str:
    data = jwt.decode(token, secretkey, algorithms=[algorithm])
    user_id = data.get("sub")
    if not user_id:
        raise JWTError("No sub")
    return user_id








