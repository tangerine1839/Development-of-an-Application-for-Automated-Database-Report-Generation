from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CHECK_OFFICE_BASE_URL: str = "https://ckkb-mos.online"

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
