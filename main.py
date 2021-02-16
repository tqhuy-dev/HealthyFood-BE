import sys
import module_cmd
import psycopg2
from psycopg2.extras import RealDictCursor
import configparser

# Read Config File
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
# Run App
if len(sys.argv) < 2:
    print("Missing Args")
else:
    if len(sys.argv) == 2 and sys.argv[1] == 'api':
        print("run api")
        module_cmd.run_api(pg_db)
    else:
        print("Hello World")

