# Laboratorium nr 7 -  Python + Django + Redis

Uruchamianie redisa poprzez dockera:
![](./img/1.PNG)
![](./img/2.PNG)


Sprawdzenie połączenia z Redisem:
![](./img/.PNG)

Poprawna konfiguracja:
![](./img/3.PNG)

Przyklad 1:
![](./img/4.PNG)

Redis-cli:
![](./img/5.PNG)

Przyklad 2(String):
Bez decode_responses = True:
![](./img/8.PNG)
decode_responses = True:
![](./img/6.PNG)
![](./img/7.PNG)
![](./img/9.PNG)

Przyklad 3:
Nadpisanie instniejącej wartości z kluczem + dołączenie do niej drugiego stringa + usuwanie(delete)
![](./img/10.PNG)

Przyklad 4:
Float / int:
INCR - dodaj
DECR - odejmij
![](./img/11.PNG)
![](./img/12.PNG)

Przykład 5:
Listy:
LPUSH - dodawanie na poczatek listy
RPUSH - dodawanie na koniec
![](./img/12.PNG)
![](./img/13.PNG)
Wyświetlenie tylko indeksów od 1-3:
![](./img/15.PNG)
![](./img/16.PNG)

Przykład 6:
LPOP - usuwanie i zwracanie pierwszego elementu listy
RPOP - usuwanie i zwracanie ostatniego elementu listy
![](./img/17.PNG)
![](./img/18.PNG)

Przykład 7:
SELECT:
Tutaj mamy doczynienia z bazami indeksowanymi od 0 do 15.

W pierwszym wyświetleniu zwróci nam none, bo nie mamy podanego klucza do pierwszej przestrzeni
![](./img/19.PNG)
![](./img/20.PNG)

Przyklad 8:
TTL - określa żywotność dla wybranego klucza. Po upłynięciu delay'u jest usuwany.
SETEX:
![](./img/21.PNG)
![](./img/22.PNG)
SET/EXPIRE(działanie kodu takie samo):
![](./img/23.PNG)

Przykład 9:
Zbiory:
Bez sortowanie:
![](./img/24.PNG)
Tutaj otrzymamy losową kolejność
![](./img/25.PNG)

Przyklad 10:
Sortowanie:
zrange - pokazuje sortowanie wg wartości
![](./img/26.PNG)
![](./img/27.PNG)

Przyklad 11:
Hashe - są to mapy między polami ciągów a wartościami.
HSET- ustawia pole w hashu przechowywanym w kluczu
![](./img/28.PNG)
Można tym w łatwy sposób tworzyć obiekty z wartościami np gracz z liczbą zycia, wytrzymałość i inne atrybuty.
cli:
![](./img/29.PNG)

Przykład 12:
Publish:
PUBSUB:
![](./img/30.PNG)
![](./img/31.PNG)
SUBSCRIBE - metoda która daje subskrybcje klienta do wybranego kanału
![](./img/32.PNG)

Przykład 13:
Strumienie:








