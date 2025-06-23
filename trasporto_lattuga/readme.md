# Esempio esame "Trasporto lattuga"

Adam Trask vuole trasportare via treno della lattuga da Los Angeles ad altre parti degli USA,
refrigerando i vagoni con del ghiaccio. Ci sono varie città interessate all'acquisto, che offrono prezzi
diversi.
Il file listino.txt contiene su ogni riga separati da spazi:
<lettera identificativa di una città> <nome della città> <prezzo di acquisto>
La città di partenza, Los Angeles, si trova nella prima riga ed è associata alla lettera a. Il restante contenuto
del file non è noto a priori.
Il file distanze.txt contiene un elenco di tratte ferroviarie che si diramano partendo da Los Angeles. Ogni
riga descrive una tratta nel seguente formato:
<lettera identificativa della città di partenza>-<lettera identificativa della città di arrivo>:<numero
intero indicante la distanza in km>
Ogni riga riporta, con lo stesso ordine, la tratta ferroviaria per raggiungere una nuova città del file listino.txt.
Si assuma che:
il percorso per raggiungere la città di partenza di ogni tratta sia sempre già stato descritto nelle righe
precedenti;
esista un unico percorso (di uno o più tratte) per connettere Los Angeles ad ogni altra città.
```
```
Si scriva un programma Python che stampi a video:
l'elenco delle città direttamente connesse a Los Angeles (cioè, raggiungibili con un' unica tratta
ferroviaria).
il nome della città con l'offerta migliore in assoluto, e quanti km devono essere percorsi per
raggiungerla.
la città con il peggior rapporto offerta/km di percorrenza, escludendo Los Angeles.
Supponendo di poter mantenere il ghiaccio per al massimo 4000 km, stampare il nome della città
raggiungibile con la migliore offerta.
```
```
Si assuma che entrambi i file esistano e che il loro formato sia corretto.
```
# Esempio

```
contenuto di listino.txt
a Los Angeles 5
b San Diego 9
c San Francisco 11
d Sacramento 12
e Portland 14
f Seattle 15
g Albuquerque 18
h Kansas City 20
i Denver 19
l Chicago 25
m Boston 40
n Washington 41
o New Orleans 30
p Miami 23
```
```
contenuto di distanze.txt
```

```
a-b:
a-c:
a-d:
d-e:
e-f:
a-g:
g-h:
d-i:
h-l:
l-m:
l-n:
l-o:
n-p:
```
**output a video**

```
Città direttamente connesse a Los Angeles:
San Diego
San Francisco
Sacramento
Albuquerque
```
```
Per raggiungere l'offerta migliore, Washington, devono essere percorsi: 4780 km
La città con il peggior rapporto è Miami
La migliore offerta entro 4000 km è a Chicago
