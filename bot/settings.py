from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ('process.env','.env'),
        #env_file_encoding = 'utf-8'
    )
    debug: bool=True
    bot_token: SecretStr = "default_bot_token_string"
    webhook_url:str="https://meow.meow.meow"
    webhook_path:str="/path/to/webhook"
    secret_tg_token:str="hehehehehehehehehemeow"
    user_id : int="1234567890"
    print(f"{bot_token}")


@lru_cache()
def get_settings():
    return Settings()

