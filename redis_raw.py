''' Comandos Redis Básicos '''
import redis

redis_connection = redis.Redis(host='localhost', port=6379, db=0)

# Chave Valor
redis_connection.set('chave_1', 'outro_valor')
valor = redis_connection.get('chave_1').decode("utf-8")
redis_connection.delete('chave_1')

# Hash
redis_connection.hset('meu_hash', 'nome', 'joao')
redis_connection.hset('meu_hash', 'idade', 30)
redis_connection.hset('meu_hash', 'cidade', 'Belo Horizonte')
nome = redis_connection.hget('meu_hash', 'nome').decode("utf-8")
cidade = redis_connection.hget('meu_hash', 'cidade').decode("utf-8")
redis_connection.hdel('meu_hash', 'cidade')

# exist
chave1 = redis_connection.exists('chave_1')
hash_key = redis_connection.exists('meu_hash')
field_key = redis_connection.hexists('meu_hash', 'nome')

print(chave1)
print(hash_key)
print(field_key)
