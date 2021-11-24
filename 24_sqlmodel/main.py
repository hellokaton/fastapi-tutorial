from typing import Optional

import uvicorn
from fastapi import FastAPI, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

# 通过引擎创建数据库
SQLModel.metadata.create_all(engine)


class Hero(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


@app.get('/heros', summary="查询列表")
async def query_heros(q: Optional[str] = Query(None)):
    with Session(engine) as session:
        statement = select(Hero)
        if q:
            statement = statement.where(Hero.name == q)
        results = session.exec(statement).all()
    return results


@app.get('/heros/{hid}', summary="根据ID查询")
async def query_hero_by_id(hid: int):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == hid)
        hero = session.exec(statement).one()
    return hero


@app.post('/heros', summary="新增")
async def save_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
    return hero


@app.put('/heros/{hid}', summary="修改")
async def update_hero(hid: int, hero: Hero):
    with Session(engine) as session:
        hero_tmp = session.exec(select(Hero).where(Hero.id == hid)).one()
        hero_tmp.name = hero.name
        hero_tmp.secret_name = hero.secret_name
        session.add(hero_tmp)
        session.commit()
        session.refresh(hero_tmp)
    return hero_tmp


@app.delete('/heros/{hid}', summary="根据ID删除")
async def update_hero(hid: int):
    with Session(engine) as session:
        hero_tmp = session.exec(select(Hero).where(Hero.id == hid)).one()
        session.delete(hero_tmp)
        session.commit()
    return {'msg': 'success'}


# pip install sqlmodel
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True, port=9000)
