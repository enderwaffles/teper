
from .users import router as users
from .posts import router as posts
from .authentication import router as authentication

routers = [users, posts, authentication]
