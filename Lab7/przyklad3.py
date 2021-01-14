from redis import Redis

redis_connection = Redis(decode_responses=True) 

key ="x"
value ="test"

redis_connection.set(key, value)
print(redis_connection.get(key))

redis_connection.append(key, " redisa")
print(redis_connection.get(key))

redis_connection.delete(key)
print(redis_connection.get(key))