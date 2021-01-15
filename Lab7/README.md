# Laboratorium nr 7 -  Python + Django + Redis

## Uruchamianie redisa poprzez dockera:
![](./img/1.PNG)
![](./img/2.PNG)

## Poprawna konfiguracja:
![](./img/3.PNG)

## Przyklad 1:
![](./img/4.PNG)

## Redis-cli:
![](./img/5.PNG)

## Przyklad 2(String):
### Bez decode_responses = True:
![](./img/8.PNG)
## decode_responses = True:
![](./img/6.PNG)
![](./img/7.PNG)
![](./img/9.PNG)

## Przyklad 3:
### Nadpisanie instniejącej wartości z kluczem + dołączenie do niej drugiego stringa + usuwanie(delete)
![](./img/10.PNG)

## Przyklad 4:
### Float / int:
* INCR - dodaj
* DECR - odejmij
![](./img/11.PNG)
![](./img/12.PNG)

##  Przykład 5:
### Listy:
#### LPUSH - dodawanie na poczatek listy
#### RPUSH - dodawanie na koniec
![](./img/12.PNG)
![](./img/13.PNG)
### Wyświetlenie tylko indeksów od 1-3:
![](./img/15.PNG)
![](./img/16.PNG)

## Przykład 6:
### LPOP - usuwanie i zwracanie pierwszego elementu listy
### RPOP - usuwanie i zwracanie ostatniego elementu listy
![](./img/17.PNG)
![](./img/18.PNG)

## Przykład 7:
### SELECT:
#### Tutaj mamy doczynienia z bazami indeksowanymi od 0 do 15.

### W pierwszym wyświetleniu zwróci nam none, bo nie mamy podanego klucza do pierwszej przestrzeni
![](./img/19.PNG)
![](./img/20.PNG)

## Przyklad 8:
### TTL - określa żywotność dla wybranego klucza. Po upłynięciu delay'u jest usuwany.
### SETEX:
![](./img/21.PNG)
![](./img/22.PNG)
### SET/EXPIRE(działanie kodu takie samo):
![](./img/23.PNG)

## Przykład 9:
### Zbiory:
### Bez sortowanie:
![](./img/24.PNG)
### Tutaj otrzymamy losową kolejność
![](./img/25.PNG)

## Przyklad 10:
### Sortowanie:
### zrange - pokazuje sortowanie wg wartości
![](./img/26.PNG)
![](./img/27.PNG)

## Przyklad 11:
### Hashe - są to mapy między polami ciągów a wartościami.
### HSET- ustawia pole w hashu przechowywanym w kluczu
![](./img/28.PNG)
### Można tym w łatwy sposób tworzyć obiekty z wartościami np gracz z liczbą zycia, wytrzymałość i inne atrybuty.
### cli:
![](./img/29.PNG)

## Przykład 12:
### Publish:
### PUBSUB:
![](./img/30.PNG)
![](./img/31.PNG)
### SUBSCRIBE - metoda która daje subskrybcje klienta do wybranego kanału
![](./img/32.PNG)

## Przykład 13:
### Strumienie:
### Wiadomości które wklimy do strumienia znajdą się nakoncu. Nie można dodać w konkretne miejsce!
![](./img/33.PNG)
### Te liczby to czas od 1 stycznia 1970 + numer sekwencji
![](./img/34.PNG)
### Dodajmy element strumienia
![](./img/35.PNG)
![](./img/36.PNG)
### Cli - dodanie strumienia
![](./img/37.PNG)
### redis_connection.xdel(stream_name, msg_id) - aby elementy nie były zgubione
![](./img/38.PNG)

## Przykład 14:
### Pipelining - inaczej przetwarzanie potokowe, które pozwala wysyłanie wielu instrukcji do redisa na raz.
![](./img/39.PNG)
### Pokazanie sprawdzania kluczy, czy są takie same.
![](./img/40.PNG)
### Błąd pokazuje zmiane kluczy

### Transakcje - Integrowanie kilku operacji w jedną całość.
* MULTI - rozpoczęcie transakcji. Zwracanie rezultatu wykonanych komend.
* EXEC - kolejne polecenia umieszczane w kolejce
* DISCARD - opóżnia wszystkie poprzednio umieszczone w kolejce polecania.
* WATCH - zaznacza klucze które mają być obserwowane w celu wykonania transakcji.

## Przykład 15:
### LUA 
### eval - przekazanie ciała skryptu. Wykonanie operacji i wyswietlenie wyniku. Drugi argument(0) to ilosc argumentów które mozna przekazać do skryptu 
![](./img/41.PNG)
![](./img/42.PNG)
### Przekazanie dwóch kluczy i dworch argumentów:
![](./img/43.PNG)
![](./img/44.PNG)
### Zwrócenie 10-elementowej tablicy:
![](./img/45.PNG)
![](./img/46.PNG)

## Przykład 16:
### Format JSON - dodawanie 2 liczb.
![](./img/47.PNG)
![](./img/48.PNG)

### Format JSON dodawanie 10 i 5:
![](./img/49.PNG)
###Tutaj możemy zobaczyć ze pierwsze wyświetla się "none", jest to efekt funkcji eval(zwraca null), a w key 2 wynik.
![](./img/50.PNG)

### Cache:
![](./img/51.PNG)
![](./img/52.PNG)

# Django Celery:
## Instalacja:
## Wchodzimy w wirtualne srodowisko i wpisujemy:
* pip install Django Celery redis Pillow django-widget-tweaks
* pip freeze > requirements.txt
![](./img/53.PNG)
![](./img/54.PNG)

## Tworzenie celery.py:
![](./img/55.PNG)

## Settings.py:
## +aplikacja widget_tweaks
![](./img/56.PNG)
![](./img/57.PNG)

## plik _init_.py:
 ![](./img/58.PNG)

## thumbnailer/tasks.py:
 ![](./img/59.PNG)
## Redis cli bez dockera:
  ![](./img/60.PNG)

## Run celery:
### "celery -A image_parroter worker -l info -P gevent"
    ![](./img/61.PNG)

### Wygląd strony tumbnailer:
  ![](./img/62.PNG)
### Pobrane zdjęcie:
 ![](./img/63.PNG)

 ## Zapytania do serwera:
 ![](./img/64.PNG)
## Konsola celery:
 ![](./img/65.PNG)

## Taski:
 ![](./img/66.PNG)
 ## Teraz wpisujemy komende :
 ## celery -A image_parroter beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
  ![](./img/67.PNG)

## ..oraz:
##celery -A image_parroter worker -l info -P gevent
  ![](./img/68.PNG)
