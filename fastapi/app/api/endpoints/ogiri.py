from fastapi import APIRouter, HTTPException, Depends
from pymongo import MongoClient
from bson import ObjectId
from typing import List

from db.session import get_db

router = APIRouter()

#お題の追加
@router.post("/themes", status_code=200)
def post_theme_in_themes(theme: str):
    db = get_db()
    res = db["themes"].insert_one({"theme": theme})
    return {"id": str(res.inserted_id)}

#お題一覧の取得
@router.get("/themes", status_code=200)
def get_themes_in_themes():
    db = get_db()
    themes = db["themes"].find()
    res = [{"id": str(theme["_id"]), "theme": theme["theme"]} for theme in themes]
    return res

#回答の追加
@router.post("/themes/{theme_id}/answers", status_code=200)
def add_answer_to_theme(theme_id: str, answer: str, user_id: str):
    db = get_db()
    res = db["themes"].update_one(
        {"_id": ObjectId(theme_id)},
        {"$push": {"answers": {
            "answer_id": ObjectId(),
            "answer": answer,
            "user_id": user_id,
            "point": 0
        }}}
    )
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail="Theme not found")
    return {"message": "Answer added successfully"}
#特定のお題の回答一覧の取得