# Laboratorium nr 6 -  Zezwolenia i uwierzytelnianie w DRF

Dodanie licznika wejsc(cookie)
Dodanie widoku: login, logout, password reset, password reset-confirm
Widok rejestracji django rest-auth

Login:
# http://127.0.0.1:8000/api/v1/rest-auth/login/
![](./img/1.png)

Logout:
# http://127.0.0.1:8000/api/v1/rest-auth/logout/
![](./img/2.png)

Reset password:
# http://127.0.0.1:8000/api/v1/rest-auth/password/reset/
![](./img/3.png)

Reset password confirm:
# http://127.0.0.1:8000/api/v1/rest-auth/password/reset/confirm/
![](./img/4.png)

Registration:
# http://127.0.0.1:8000/api/v1/rest-auth/registration
![](./img/5.png)

Rejestracja nowego uzytkownika:
![](./img/8.png)
Otrzymujemy token po załozeniu konta:
![](./img/9.png)
Otrzymany mail  z potwierdzeniem w konsoli:
![](./img/16.png)

Tokeny uwierzytelniajace + email zwracany.
Wgląd do widoku postów mają tylko uzytkownicy z tokenem
![](./img/6.png)

Widok tokenów:
# http://127.0.0.1:8000/admin/authtoken/tokenproxy/
![](./img/11.png)

Router:
![](./img/14.png)
Viewset:
nie posiadamy metod takich jak get()
![](./img/15.png)

Licznik wizyt oraz informacja o ostatniej wizycie:

![](./img/12.png)
W samym kodzie ustawiamy ilosc odwiedzin jezeli ich nie ma na 0 i jezeli wizyta nastąpi wartosc++
![](./img/13.png)

