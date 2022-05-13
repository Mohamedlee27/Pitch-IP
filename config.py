class Config:
    '''
    General configuration parent class
    '''
    

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:lee123@localhost/pitch'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:lee123@localhost/pitch'
    
    DEBUG = True

    config_options={
    'development':Config,
    'production':ProdConfig
}