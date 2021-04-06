# StationDePesage

# Samuel Duclos
## Version alpha (il reste un peu de déboguage, mais sûrement pas grand chose.
## Voir les autres répertoires du projet (https://github.com/TSO-team/GestionDesTransports, https://github.com/TSO-team/Vehicule, https://github.com/TSO-team/PosteDeCommande, https://github.com/TSO-team/CentreDeTri, https://github.com/TSO-team/Usine, ...) pour voir mes contributions sur le rapport et les autres stations de l'usine... Je n'ai pas tout fait dans mon équipe de 5, mais presque... Vous me croyez maintenant?
## Ceci est un projet d'école. Je n'étais pas sensé toucher aux autres stations mais...

Pour pouvoir s'intégrer au système, la station de pesage devra pouvoir au minimum :
- Reconnaître et récupérer les messages CAN qui lui seront d'intérêts ;
- Décoder les messages qui lui permettront de savoir si elle doit être en arrêt ou en opération ;
- Décoder les messages qui lui permettront de savoir si elle doit produire des valeurs de poids en grammes ou en onces ;
- Émettre des messages qui permettront de connaître s'il est en fonction, en erreur ou en arrêt ;
- Se mettre en arrêt ou en opération ;
- Opérer à l'aide de pilotes, d'interfaces, de processus et de services et opérer au besoin à l'aide de machines à états, d'une base de temps, d'un service de base de temps, de processus Linux, de fils d'exécution, de tuyau, de mutex et d'appels système ;
- Utiliser son bras robotisé et son capteur de distances pour localiser les blocs à peser ;
- Procéder au déchargement du véhicule et déposer les blocs à peser sur le plateau de sa balance ;
- Déterminer le poids des blocs en interagissant avec sa balance ;
- Déposer les blocs dans une unité d'entreposage (e.g. un plat) après leur pesée ;
- Émettre des messages qui permettront de connaître le poids des blocs.
