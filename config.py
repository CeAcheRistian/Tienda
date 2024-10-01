class Config:
    SECRET_KEY = "el_pepe_123"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
