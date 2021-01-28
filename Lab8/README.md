# Laboratorium nr 8 - Czat z użyciem Web Socket + Web Workers

## 1. Socket chat
### Tworzymy folder wraz z plikiem package.json
### npm install express@4
### ![](./img/1.PNG)
### odpalamy projekt poleceniem:
### node index.js
### ![](./img/2.PNG)
### Instalacja socketów:
### ![](./img/3.PNG)
### stworzenie podstawowego widoku index.html:
### ![](./img/4.PNG)
### Nasłuchiwanie zdarzenia connection
### ![](./img/6.PNG)
### ![](./img/5.PNG)
### ![](./img/7.PNG)
### Nasłuchiwanie zdarzenia connection - disconected
### ![](./img/8.PNG)
### ![](./img/9.PNG)
### Pisanie na czacie:
### ![](./img/10.PNG)
### ![](./img/11.PNG)
### ![](./img/12.PNG)

## 2.Workers
### ![](./img/13.PNG)
### Aby bez pomocy django utworzyć projekt, musimy włączyć python server:
### ![](./img/14.PNG)
### Wygląd strony:
### ![](./img/15.PNG)
### Działanie:
### ![](./img/16.PNG)
### ![](./img/18.PNG)
### Gdy podamy złe dane otrzymamy błąd:
### ![](./img/17.PNG)
### fibonacci.js:
### ![](./img/20.PNG)
### silnia.js:
### ![](./img/19.PNG)
### script.js
### Tworzenie workerów ( new Worker())
### onmessage -> EventHandler, który będzie wywołany gdy będzie zdarzenie
### ![](./img/21.PNG)
### index.js - kod:
### ![](./img/23.PNG)
### index.js - przekazanie danych poprzez input
### ![](./img/22.PNG)
