from redis import Redis
from time import sleep
from datetime import datetime

redis_connection = Redis(decode_responses=True)

redis_connection.set("key","value")
redis_connection.expire("key",30)

#podaj klucz
print(datetime.now().time(), redis_connection.get("key"))
sleep(10)
print(datetime.now().time(), redis_connection.get("key"))
sleep(30) #delay
print(datetime.now().time(), redis_connection.get("key"))