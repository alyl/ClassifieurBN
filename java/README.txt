Cette appli permet de cr�er des objets java � partir des fichiers � notre disposition.

Dans lib, vous trouverez les deux fichiers csv que j'ai utilis� pour repr�senter les donn�es (au format Json) 
et les archives jar de weka et de la librairie que j'ai utilis�e pour d�serialiser les Json : google-gson-2.2.4

Dans src, il y a mes classes :
	- les beans : 
		User (qui repr�sente un utilisateur : id / age / sexe / job / notes qu'il a donn�es)
		Movie (qui repr�sente un film : id / timestamp de date de sortie / style / notes qu'il a re�ues )
	- les classes de traitement des fichiers csv
		Users_handling (qui permet de s'occuper de users.csv)
		Movies_handling (qui permet de s'occuper de movies.csv)
	- main ... qui montre comment utiliser tout �a

En esp�rant que �a serve !

Benz.