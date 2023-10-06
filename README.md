# CM_getOSM_for_Geojson
Das Skript dient dazu, das GeoJson in einem bestimmten Bereich aus Open Street Map auszulesen. 

## Verwendung:
1. pip install -r requirements.txt
2. [boundary.geojson](boundary.geojson) auf den Bereich anpassen, der abgefragt werden soll. (https://geojson.io)
![img.png](img/img.png)
3. passe in [OSMreader.py](OSMreader.py) die Variablen point und dist an. (point sollte ungefähr der Mittelpunkt des abzufragenden Bereichs sein. dist der Radius in Meter).
4. Ausführen und [output.geojson](output.geojson) ist dein GeoJson.