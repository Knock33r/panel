# panel

###important : 
J'utilise la librairie **customTkinter** pour le GUI et je ne suis pas sur qu'elle fonctionne sur autre chose que windows.
Les fichiers sont également parametrés sur mon pc. Je ne pensais pas forcément partager ce code avant que je l'ai terminé, et je comptait regler ces problemes de "compatibilitée" plus tard.

###But du logiciel :
Créer un GUI permettant de simplement créer, gérer et utiliser des serveurs minecraft. Ce genre de systèmes existent déja pour des serveur hébergés sur des VPS mais cela n'existe pas pour des serveur hébergés sur son pc. Créer ses derniers est également complexe pour quelqu'un qui ne s'y connait pas. La création d'un serveur est différente en fonction de la version du serveur (vanilla => minecraft normal ; Spigot, sponge et paper => Plugins, petites extension ; forge, fabric => mods, grosses extensions). Je voulais donc tout simplifier dans un GUI.
Dans un second temps, je pense qu'il serait également interessant de faire une grosse documentation sur les étapes de la création de serveurs minecraft. Tels que les plugins utiles pour les différents mode de jeu.

J'ai également fait ce programme car il me permettait de développer mes compétences en python sur plusieurs points : Gui, pour l'interface graphique ; Réseau, pour ouvrir les ports et s'assurer du bon fonctionnement et de la mise en ligne du serveur ; Ecriture de texte dans des fichiers, pour sauvegarder les doonées ; Telechargement, pour les telechargements des serveurs.

###Avancée et fonctionnement actuel :
Pour le moment, le panel n'est vraiment pas avancé esthetiquement parlant. Je cherche déja a faire quelque chose de fonctionnel avant d'améliorer l'apparence du GUI.
Je stock les données des serveurs dans un fichier xlsx. C'est également quelque chose que je souhaite changer. Peut etre pour passer sur du CSV.
Je suis actuellement entrain de faire la partie "downloadJar" du programme, qui permettra d'installer et de créer les serveurs. Cette partie est actuellement bugguée.
