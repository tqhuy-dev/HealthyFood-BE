import psycopg2
from psycopg2.extras import RealDictCursor
import configparser


def connection_pg_db():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print(config.get('APP', 'ENVIRONMENT'))
    # Connect Postgres
    pg_db = psycopg2.connect(user=config.get('DATABASE', 'USER'),
                             password=config.get('DATABASE', 'PASSWORD'),
                             host=config.get('DATABASE', 'HOST'),
                             port=config.get('DATABASE', 'PORT'),
                             database="FoodDB",
                             cursor_factory=RealDictCursor)

    print("Connect Postgres Success")
    return pg_db
