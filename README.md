# NB_SCHOOL: 

phonebook

Realizzare una rubrica telefonica, che permetta tramite menu interattivo l'inserimento, la modifica, cancellazione e visualizzazione dei contatti (per semplicità limitati a nome e telefono). Dal menu deve essere possibile scegliere una di queste opzioni o di uscire dall'applicazione, e sarà necessario salvare la rubrica in un file json che dovrà poi essere caricato all'avvio della stessa. Sarà necessario gestire in modo opportuno condizioni di errori come file di salvantaggio non presente, non leggibile o non in formato json.
I comandi dovranno avere i seguenti requisiti:
- l'inserimento di un utente con un nome quando esiste già un utente con quel nome dovrà fallire.
- la visualizzazione dei contatti dovrà avvenire in ordine alfabetico con un messaggio in caso in cui non esistano contatti.
- la modifica di un contatto dovrà essere possibile solo nel caso in cui esista almeno un contatto e dovrà permettere di modificare solo il nome o solo il telefono senza doverlo re-inserire
- la cancelazione di un contatto dovrà essere possibile solo nel caso in cui esista almeno un contatto. 


