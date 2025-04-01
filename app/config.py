from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    SECRET_KEY: str
    ALGORITHM: str


    model_config = ConfigDict(env_file=".env", extra="ignore")


settings = Settings()
