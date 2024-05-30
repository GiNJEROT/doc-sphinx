.. _blind:

=============
Gestion Store
=============

Les Stores sont gérés via KNX avec un retour d'information et commande disponnible via l'interface web d'OnSphere.

Les principaux paramètre sont:

- Protection solaire
- Sécurité vent, gel, pluie et incendie
- Reprise mode automatique après 3h

La protection solaire est faite graçe à un module de type JSB/S1.1 qui permet le paramétrage de la poursuite solaire du bâtiment en prenant en compte les ombres porté sur le bâtiment.

Les élements de sécurité sont assuré d'une part via une station météo installer sur le bâtiment et pour l'incendie, nous récupérons les infos des élements à piloter via une interface ESPA.

Si une action manuel est faite sur les stores, la poursuite solaire est mise en pause pendant 3 heures sans intervension nouvel.