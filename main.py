from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel, Field

app = FastAPI(
    title="Поиск при помощи wikipedia"
)

class Parametrs(BaseModel):
    search: str
    result: int = Field(ge=1)


@app.get("/{search}", description="Все статьи по вашему запросу")
def get_search(search : str):
    return wikipedia.search(search)


@app.get("/{search2}?result={result}", description="Статьи по количество результатов")
def get_result_searches(search2 : str, result : int = 1):
    if result < 1: return "impossible"
    return wikipedia.search(search2, results=result)


@app.post("/search/answer", description="Статьи, которые интересуют", response_model=dict)
def get_states(parametrs: Parametrs):
    return {response : wikipedia.summary(response)
            for response in wikipedia.search(parametrs.search, results=parametrs.result) if response}


