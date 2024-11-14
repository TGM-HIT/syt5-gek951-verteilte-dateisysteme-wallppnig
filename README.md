# GK951 Verteilte Dateisysteme "Shared Storage"

**Authors:** Stuppig Markus 5DHIT, Wallpach Melissa 5BHIT
**Version:** 2024-11-14

## Einführung 
Diese Aufgabe soll die Möglichkeit von gemeinsam genutzten Speicher in Cloud und Cluster Umgebungen näher bringen. Dabei sollen die verschiedenen Technologien im Bereich verteilte Dateisysteme gegenübergestellt und auf ihre Einsetzbarkeit überprüft werden.

Ziele sind der Einsatz von Objektspeichern und der Vergleich von verteilten Dateisystemen.


## Umsetzug 

To get the minio executable for arm

```
curl -O https://dl.min.io/server/minio/release/darwin-arm64/minio
chmod +x ./minio
```

To start the minio server
```
minio server minio_folder
```

To access the minio server (standard credentials)
```
minioadmin
minioadmin
```

To run the CRUD fastapi python webserver
```
uvicorn main:app --reload
```
