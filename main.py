import uvicorn
from fastapi import FastAPI
from models.user import UserIn, UserOut, fake_save_user
import logging

logger = logging.getLogger(__name__)

app = FastAPI()


@app.post('/user/', response_model=UserOut)
async def create_user(user_in: UserIn):
    logger.info("create_user function!!!")
    user_saved = fake_save_user(user_in)
    return user_saved

if __name__ == "__main__":
    uvicorn.run(app)
