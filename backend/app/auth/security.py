
#app
#auth
#security.py

#bibliotecs
from werkzeug.security import generate_password_hash, check_password_hash
from jose import jwt, JWTError

#modules
from datetime import datetime, timedelta


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








