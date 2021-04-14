from redis import Redis

redis_connection = Redis() 

key ="x"
value ="test"

redis_connection.set(key, value)
print(redis_connection.get(key))