Cette appli permet de créer des objets java à partir des fichiers à notre disposition.

Dans lib, vous trouverez les deux fichiers csv que j'ai utilisé pour représenter les données (au format Json) 
et les archives jar de weka et de la librairie que j'ai utilisée pour déserialiser les Json : google-gson-2.2.4

Dans src, il y a mes classes :
	- les beans : 
		User (qui représente un utilisateur : id / age / sexe / job / notes qu'il a données)
		Movie (qui représente un film : id / timestamp de date de sortie / style / notes qu'il a reçues )
	- les classes de traitement des fichiers csv
		Users_handling (qui permet de s'occuper de users.csv)
		Movies_handling (qui permet de s'occuper de movies.csv)
	- main ... qui montre comment utiliser tout ça

En espérant que ça serve !

Benz.