from fastapi import APIRouter, Depends

from db.session import get_db

router = APIRouter()

#userの追加
@router.post("/users", status_code=200)
def post_user_in_users(name: str, age: int):
    db = get_db()
    res = db["users"].insert_one({
        "name": name,
        "age": age
        })
    return {"id": str(res.inserted_id)}

#user一覧の取得
@router.get("/users", status_code=200)
def get_users_in_users():
    db = get_db()
    users = db["users"].find()
    res = [{"id": str(user["_id"]), "name": user["name"], "age": user["age"]} for user in users]
    return res