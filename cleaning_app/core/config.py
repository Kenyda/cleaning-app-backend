from pydantic import BaseSettings


class EnvConfig(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    SECRET: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


env_config = EnvConfig()
