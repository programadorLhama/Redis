from models.redis.connection.redis_connection import RedisConnectionHandle
from models.redis.redis_repository import RedisRepository
from models.mysql.mysql_repository import MysqlRepository


redis_conn = RedisConnectionHandle().connect()
redis_repository = RedisRepository(redis_conn)
mysql_repository = MysqlRepository()


############################### Logica
name = "Aroldo"
print('Buscando Redis')
value = redis_repository.get(name)
if value:
    print('Achei No Redis!!!!!')
    print(value)

else:
    print('Buscando Mysql...')
    value_2 = mysql_repository.select_by_name(name)
    print('Achei no Mysql!!!')
    redis_repository.insert_ex(name, value_2, 10)
