from pydantic import BaseSettings, BaseModel


class DB(BaseModel):
    """Database config"""

    host: str
    db_name: str
    user: str
    password: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        fields = {
            "host": {
                "env": "DB_HOST",
            },
            "db_name": {
                "env": "DB_NAME",
            },
            "user": {
                "env": "DB_USER",
            },
            "password": {
                "env": "DB_PASS",
            },
        }


class Settings(BaseSettings):
    """App settings"""

    db = DB()


def load_settings() -> Settings:
    """Get app settings"""

    return Settings()
