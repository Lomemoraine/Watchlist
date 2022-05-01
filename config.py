# configuaration classes to fit our needs
import os
class Config: # contains configurations that are used in both production and development stages
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    pass



class ProdConfig(Config):#subclass contains configurations that are used in production stages of our application and inherits from the parent Config class
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):#subclass contains configurations that are used in development stages of our application and inherits from the parent Config class.


    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}