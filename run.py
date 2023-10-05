from datetime import datetime
from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)


data_atual = datetime.now()
data_formatada = data_atual.strftime('%Y-%m-%d')
print(data_formatada)

# Frutas em promoção
redis_repository.insert_hash_ex(data_formatada, "banana", 3.12, 40)
redis_repository.insert_hash(data_formatada, "morango", 4.12)
redis_repository.insert_hash(data_formatada, "Uva", 12.12)
