.. _gate:

============================
Système barrière automatique
============================

Le système installé se base sur les équipement de la marque Axis.

Principe de fonctionnement:

1. Détection et lecture de la plaque d’immatriculation. 
2. Vérification que la plaque d’immatriculation figure sur la liste d’autorisation.
3. Confirmation que la plaque d’immatriculation est autorisée à accéder au parking ouest entre 8 h et 18 h.
4. Ouverture de la barrière d’accès.

.. image:: assets/pacs.png 

La gestion des autorisations d'accès sont accessible au opérateur sur site via une interface web de l'hyperviseur qui sera restreint aux utilisateur autorisé.

Pour ce faire, nous utilisons ONVIF pour assuré la communication entre la caméra de reconnaissance de plaque et la gestion de la barrière.

