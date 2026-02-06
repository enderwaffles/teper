
from .users import router as users
from .posts import router as posts
from .authentication import router as authentication
from .home import router as home

routers = [
    users, 
    posts, 
    authentication, 
    home,
    ]
