# Breizhibus

![img1](https://www.lesuricate.org/wp-content/uploads/2017/02/the-magic-school-bus.jpg)


Préparer une base de données et écrire un code qui permet à Breizhibus de gérer ses lignes de bus.


## Contexte du projet


Breizhibus souhaite informatiser la gestion de ses lignes de bus. Pour le moment, l'appli n'est prévue que pour une utilisation interne. Dans un second temps, elle sera peut-être ouvert au public (avec, par exemple, une fonctionnalitée de calcul d'itinéraire).

La DSI a décidé d'utiliser MySQL et Python pour ce projet. MySQL, car Breizhibus gère les transports de Ploukusanagi, une petit ville. Il n'y a donc pas beaucoup de données à stocker. Et Python, parce que la DSI a entendu dire que c'était bien pour faire des sites web et des calculs sur les données. Et à terme, c'est des projets qui pourraient se développer.

Votre première mission est de mettre en place les bases de cette appli. Vous devez créer et remplir la base de donnée comme demandé dans la documentation client (Kata 1 MySQL) et préparer un code Python qui affiche la liste des lignes. Ce code doit aussi, pour une ligne choisie, afficher la liste des arrêts de cette ligne. L'affichage en mode console suffit pour cette première phase, mais si vous avez le temps, vous pouvez préparer une interface plus évoluée.

Après discussion avec les collaborateurs, Breizhibus ne souhaite plus d'affichage console, qui est jugé pas UX du tout. Il vous faut développer une interface graphique, même rudimentaire. De plus, ils ont besoin de pouvoir gérer les bus. Il vous faut faire un formulaire qui permet d'ajouter des bus en base et de les assigner à une ligne (un bus ne peut avoir qu'une seule ligne, mais une ligne peut avoir plusieurs bus). Il faut aussi pouvoir les modifier et les supprimer; Enfin, lorsque vous affichez les arrêts par ligne, affichez aussi les bus par ligne.

LA DSI aimerait savoir s'il est possible d'ouvrir l'application au publique. Pour ça, il vous est demandé un petit POC (Proof Of Concept) sur votre appli. Il faudrai une page pour saisir un arrêt de départ et un arrêt d'arrivée. Quand les saisies sont validées, l'appli affiche toutes les lignes à emprunter pour aller du départ à l'arrivée.

## Modalités pédagogiques

C'est un travail individuel. Il est à faire lorsque vous avez terminé lorsque vous avez du temps, lorsque vous êtes en avance sur les projets ou les ateliers. Le dead line est pour le 18 décembre.

Attention, suivant l'avancé de l'ensemble de la promo, les livrables attendus peuvent être mis à jour. A vous de savoir vous montrez suffisament souple pour intégrer les nouvelles demandes du client.

## Critères de performance

Une base de donnée propre et remplie. Un code python qui fonctionne, peu importe les choix techniques. Et une appli qui répond aux demandes du client.

## Modalités d'évaluation
Revu de code par les formateurs, puis un débrief oral individuel avec auto-évaluation.

## Livrables

Sur Github : - une fichier SQL qui contient tout ce qu'il faut pour importer la base. - votre code - un readme.md documenté, avec captures d'écran, qui explique, dans un premier chapitre le fonctionnement de votre appli, dans un second les choix techniques fait (par exemple, utiliser le connecteur MySQL), et dans un troisième les difficultés rencontrées et la façon de les résoudre (par exemple un lien vers un tuto qui vous a aidé).
