from redis import Redis
redis_connection = Redis(decode_responses=True)
key ="some-key"
value =15
redis_connection.set(key, value)
print(redis_connection.get(key)) #wypisanie
print(redis_connection.incr(key,15)) #dodawanie
print(redis_connection.decr(key,20)) #odejmowanie