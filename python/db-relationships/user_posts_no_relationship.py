### the models — no Relationship attributes

from sqlmodel import SQLModel, Field, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str

class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    user_id: int = Field(foreign_key="user.id")


### the endpoints

from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import create_engine, Session

app = FastAPI()

# db boilerplate

db_url = "sqlite:///./user_posts_no_relationship.db"
engine = create_engine(db_url, echo=True)
SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session


# creation endpoints

@app.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.post("/posts/", response_model=Post)
def create_post(post: Post, session: Session = Depends(get_session)):
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


# retrieval endpoints

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


class UserWithPosts(SQLModel):
    id: int
    name: str
    posts: list[Post] = []

@app.get("/users/{user_id}/with-posts", response_model=UserWithPosts)
def get_user_with_posts(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    posts = session.exec(select(Post).where(Post.user_id == user_id)).all()
    return UserWithPosts(
        id=user.id,
        name=user.name,
        posts=posts,
    )

"""
http :8000/users/ name="Alice"
http :8000/posts/ content="Hello world!" user_id:=1
http :8000/posts/ content="Another post" user_id:=1
http :8000/users/1
http :8000/users/1/with-posts
"""
