# Hill Cipher

Sviluppo del cifrario di Hill. Permette all'utente di cifrare e decifrare con il cifrario di Hill e di forzare un 
ciphertext tramite l'attacco known plaintext, utilizzando l'alfabeto inglese "ABCDEFGHIJKLMNOPQRSTUVWXYZ".

Esercizio di programmazione per il Corso Data Security and Privacy - Set 1

# Come Utilizzarlo



# Come Funziona

Una volta avviato, il programma stampa a video un piccolo menù dove vengono indicate le quattro possibili funzioni che
l'utente può eseguire. L'utente può eseguire una funzione semplicemete inserendo nella console il numero relativo alla 
funzione scelta. Di seguito viene riportata una breve descrizione delle tre funzioni e cosa richiedono in input.

1. Encrypt a Message.
   Funzione che consente all'utente di cifrare un messsagio inserito dall'utente (plaintext) in base
   ad una chiave anch'essa inserita dall'utente.
   - Il testo che l'utente inserisce, sia per la chaive sia per il plaintext, deve rispettare l'alfabeto inglese e non 
     deve contenere spazi ma può essere scritto sia in minuscolo che in maiuscolo.
   - L'utente deve inserrie una chiave che ha una lunghezza quadrata, dovendo creare uan matrice per la chiave 
     quadrata. Se questo non viene fatto la funzione ritorna un messaggio di errore.
   - Una volta inseriti i due input la funzione stamperà a video le matrici estrapolate dal plaintext e della chiave 
     inserita e procederà alla cifratura del plaintext.
   - Infine la funzione stamperà il testo del ciphertext generato e anche la matrice da cui è stato creato in fase di 
     cifratura.
2. Decipher a Message.
   Funzione che consente all'utente di decifrare un messsagio inserito dall'utente (ciphertext) in 
   base ad una chiave anch'essa inserita dall'utente.
   - Il testo che l'utente inserisce, sia per la chaive sia per il plaintext, deve rispettare l'alfabeto inglese e non 
     deve contenere spazi ma può essere scritto sia in minuscolo che in maiuscolo.
   - L'utente deve inserrie una chiave che ha una lunghezza quadrata, dovendo creare uan matrice per la chiave 
     quadrata. Se questo non viene fatto la funzione ritorna un messaggio di errore.
   - La matrice generata dalla chiave deve inoltre risultare quadrata altrimenti verrà restituito un errore.
   - Una volta inseriti i due input la funzione stamperà a video le matrici estrapolate dal ciphertext e della chiave 
     inserita e procederà alla decifratura del ciphertext.
   - Infine la funzione stamperà il testo del plaintext generato e anche la matrice da cui è stato creato in fase di 
     decifratura.
3. Force a Ciphertext (Known Plaintext Attack).
   Funzione che consente all'utente di eseguire l'attacco di tipo Known 
   Plaintext al cifrario. Viene richiesto un plaintext, un ciphertext e la dimensione degli m-grammi (m) con cui 
   testare l'attacco.
   - Il testo che l'utente inserisce, sia per la chaive sia per il plaintext, deve rispettare l'alfabeto inglese e non 
     deve contenere spazi ma può essere scritto sia in minuscolo che in maiuscolo.
   - L'utente deve inserire una chiave che ha una lunghezza appropriata rispetto alla dimensione degli m-grammi. Se 
     questo non viene fatto la funzione ritorna un messaggio di errore.
   - Il numero di m-grammi generati dal plaintext e dal ciphertext deve essere lo stesso. L'utente deve quindi inserire
     un plaintext e un ciphertext di lunghezza appropriati altrimenti la funzione ritorna un messaggio di errore.
   - La matrice generata dal plaintext deve inoltre risultare invertibile altrimenti l'attacco non può andare a buon 
     fine e dunque in quest'ultimo caso la funzione restituisce un messaggio di errore.
   - Una volta inseriti i tre input la funzione stamperà a video le matrici estrapolate dal ciphertext e del plaintext 
     inseriti e procederà all'esecuzione dell'attacco.
   - Terminato l'attacco, se è andato a buon fine, la funzione stamperà il testo della chiave trovata e anche la 
     matrice da cui è stata ricavata.
4. Quit.
   Funzione che consente la chiusura del programmma.

# Ultime Note

Se durante la creazione degli m-grammi l'ultimo blocco risulta parzialmente vuoto viene inserita un lettera 'Z' per
ogni lettera mancante.

Le matrici del ciphertext e del plaintext si leggono per collonna dall'alto verso il basso, mentre le matrici delle
chiavi si leggono per riga da sinistra a destra.

English
======================================================================================================================

Hill cipher. It allows the user to encrypt and decrypt with Hill's cipher and to force a
ciphertext through the known plaintext attack.

Programming exercise for the Data Security and Privacy Course - Set 1

# Author
Elia Mercatanti