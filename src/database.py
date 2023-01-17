from sqlalchemy import create_engine
import base64


user = 'tvm'
pwd = 'T5aoePV7W5DnmpAcSTDO09KQVesEZPPw'
host = 'tvm2.db.homolog.open-co.tech'
db = 'tvm'

engine = create_engine(f'postgresql+psycopg2://{user}:{pwd}@{host}:5432/{db}')
query = engine.execute('select * from v_note limit 1;')

columns = query.keys()

for row in query:
    print(columns)
    print(row)
