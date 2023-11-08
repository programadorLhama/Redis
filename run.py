from datetime import datetime
from models.redis.connection.redis_connection import RedisConnectionHandle
from models.redis.redis_repository import RedisRepository
from configs.start_form import start_form

######################################################
# 1. Conectar ao banco de dados e buscar elementos

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)

data_atual = datetime.now()
data_formatada = data_atual.strftime('%Y-%m-%d')
hash_items = redis_conn.hgetall(data_formatada)
print(hash_items)

######################################################
# 2. Carregar dados ao formulario
python_dict = {}
for key, value in hash_items.items():
    python_dict[key.decode('utf-8')] = value.decode('utf-8')

print(python_dict)
start_form.load_info(python_dict)
#######################################################
# 3. Utilizar valor armazenado -> Ligar API

value = start_form.get_info('Uva')
value2 = start_form.get_info('banana')
print(value)
print(value2)