import json
import sqlalchemy
import os

def f():
    if os.path.exists(os.path.abspath(".env")):
        return open(os.path.abspath(".env"))
    if os.path.exists(os.path.abspath("../.env")):
        return open(os.path.abspath("../.env"))

# open file via main dir
json_file = f()
data = json.load(json_file)

db_keys = data['DB']
locals().update(db_keys)

engine = sqlalchemy.create_engine(
    "{0}+{1}://{2}:{3}@{4}:{5}/{6}".format(
        system, driver,
        user_name, password,
        ip, port, db_name
    ),
    client_encoding='utf8',
    echo=True
)
