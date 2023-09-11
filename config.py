import os


class Config:
    """Base configuration."""
    DEBUG = False
    TESTING = False
    TEMPLATE_FOLDER = os.path.join(os.getcwd(), 'src/interfaces/web/templates')
    STATIC_FOLDER = os.path.join(os.getcwd(), 'src/interfaces/web/static')
    SECRET_KEY = 'my_precious'
    DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
