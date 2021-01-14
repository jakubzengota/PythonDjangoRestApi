from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='testuj'

redis_connection.hset(hash_key,'klucz','value')
