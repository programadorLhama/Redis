from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)

redis_repository.insert('Estou', 'AQUI!!!!!!!')
value = redis_repository.get('Estou')

redis_repository.insert_hash("MeuHash", "campo_1", 'Este e meu valor')
val = redis_repository.get_hash("MeuHash", "campo_1")
print(val)