import psycopg2
from psycopg2.extras import RealDictCursor


def connection_pg_db(config):
    # Connect Postgres
    pg_db = psycopg2.connect(user=config.get('DATABASE', 'USER'),
                             password=config.get('DATABASE', 'PASSWORD'),
                             host=config.get('DATABASE', 'HOST'),
                             port=config.get('DATABASE', 'PORT'),
                             database="FoodDB",
                             cursor_factory=RealDictCursor)

    print("Connect Postgres Success")
    return pg_db
