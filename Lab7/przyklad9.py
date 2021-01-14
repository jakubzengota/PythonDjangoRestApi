from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("klucz","1")
redis_connection.sadd("klucz","2")
redis_connection.sadd("klucz","3")

print(redis_connection.smembers("klucz"))