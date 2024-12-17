from src.utils import addLogAsync
from fastapi import APIRouter,HTTPException
from typing import Optional
from src.models.responseClasses import SchemaPost
from src.service.dao.posts import Posts

getPostsRouter = APIRouter(prefix="/posts")


@getPostsRouter.get("/posts/{post_id}")
async def get_posts(post_id: int) -> list[SchemaPost] | SchemaPost:
    resp = await Posts.get(post_id)
    if isinstance(resp, dict):
        raise HTTPException(**resp)
    else:
        return resp