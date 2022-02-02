#DXTrackerProxy

## Installation
Cloner le projet dans le `/opt` de RRF2.

```
cd /opt
git clone https://github.com/armel/DXTrackerProxy.git
```

## Lignes grises

À ajouter dans la crontab de RRF2, via `crontab -e`

```
*/2 * * * * /opt/DXTrackerProxy/DXGreyline.py
*/2 * * * * /opt/DXTrackerProxy/DXSunmap.py
```

> Le script `DXEarth.py` produit une carte de qualité moyenne. Je ne l'ai pas donc activé, mais il est fonctionnel.

## Sat et Cluster

Copier `DXSat.py` et `DXCluster.py` dans le `/var/www/RRFBlockIP/back/`

That's all.
