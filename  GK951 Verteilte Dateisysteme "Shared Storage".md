# GK951 Verteilte Dateisysteme "Shared Storage"

**Authors:** Stuppig Markus 5DHIT, Wallpach Melissa 5BHIT
**Version:** 2024-11-14

## Einführung 
Diese Aufgabe soll die Möglichkeit von gemeinsam genutzten Speicher in Cloud und Cluster Umgebungen näher bringen. Dabei sollen die verschiedenen Technologien im Bereich verteilte Dateisysteme gegenübergestellt und auf ihre Einsetzbarkeit überprüft werden.

Ziele sind der Einsatz von Objektspeichern und der Vergleich von verteilten Dateisystemen.

## Fragestellungen 
### 1. Welche verschiedenen Einsatzgebiete bieten distributed Object Storages an?
- Speicherung großer Mengen unstrukturierter Daten wie Bilder, Videos, Dokumente
- Backup und Archivierung von Daten
- Content Delivery Networks (CDN) für die schnelle Bereitstellung von Medieninhalten
- Big Data Analytics und Data Lakes
- Cloud-native Anwendungen und Microservices
- Internet of Things (IoT) Datenerfassung und -speicherung
- Wissenschaftliche und medizinische Datenanalyse
- Disaster Recovery und Geschäftskontinuität

###2. Was sind die Kernkomponenten von MinIO und wie spielen diese zusammen?

Die Kernkomponenten von MinIO sind:

- MinIO Server: Verwaltet die Speicherung und den Zugriff auf Objekte
- Buckets: Logische Container für Objekte
- Objects: Die eigentlichen gespeicherten Daten
- Metadata: Zusätzliche Informationen zu den Objekten
- Access Control: Verwaltung von Zugriffsrechten
- Load Balancer: Verteilt Anfragen auf mehrere Server
- MinIO Client (mc): Kommandozeilen-Tool für die Interaktion mit dem Server

Diese Komponenten arbeiten zusammen, um eine skalierbare und zuverlässige Objektspeicherung zu ermöglichen. Der Server verwaltet Buckets und Objekte, während der Load Balancer für die Lastverteilung sorgt. Access Control stellt die Sicherheit sicher, und der Client ermöglicht die einfache Verwaltung.

### 3. Was heißt WORM und wo kommt dieses Prinzip zum Einsatz?

WORM steht für "Write Once Read Many". Es bezeichnet ein Datenspeicherprinzip, bei dem Daten nur einmal geschrieben und danach nicht mehr verändert werden können. 

Einsatzgebiete:

- Compliance und Regulierung (z.B. in der Finanzbranche)
- Langzeitarchivierung von Dokumenten
- Schutz vor versehentlicher oder böswilliger Datenmanipulation
- Forensische Datenanalyse
- Medizinische Aufzeichnungen
- Blockchain-Technologien

### 4. Welche Systemtopologien unterstützt MinIO? Und wo liegen hier die Unterschiede?

- Standalone: Ein einzelner MinIO-Server für einfache Setups
- Distributed: Mehrere MinIO-Server arbeiten zusammen für höhere Skalierbarkeit
- Gateway: MinIO als Gateway zu anderen Speichersystemen wie NAS oder Cloud-Speicher
- Kubernetes: Deployment von MinIO in Kubernetes-Clustern

Die Unterschiede liegen in:

- Skalierbarkeit: Distributed und Kubernetes bieten höhere Skalierbarkeit als Standalone
- Komplexität: Standalone ist am einfachsten zu konfigurieren, während Distributed und Kubernetes komplexer sind
- Redundanz: Distributed und Kubernetes bieten bessere Datenverfügbarkeit durch Replikation
- Flexibilität: Gateway ermöglicht die Integration mit bestehenden Speichersystemen
- Performance: Distributed und Kubernetes können höhere Durchsatzraten erreichen

Die Wahl der Topologie hängt von den spezifischen Anforderungen an Skalierbarkeit, Verfügbarkeit und Verwaltbarkeit ab.

## Citations:
[1] https://min.io/docs/minio/kubernetes/upstream/index.html
[2] https://www.virtono.com/community/tutorial-how-to/how-to-deploy-minio-on-kubernetes/
[3] https://min.io/docs/minio/kubernetes/eks/operations/installation.html
[4] https://www.youtube.com/watch?v=6BlY8Zr8-Cc
[5] https://thelinuxforum.com/articles/555-how-to-install-kubectl-on-mac
[6] https://faun.pub/what-is-minio-and-how-to-configure-it-in-kubernetes-18072ac80fb2?gi=ad2d49f57197
[7] https://www.aquasec.com/cloud-native-academy/kubernetes-101/kubernetes-architecture/
[8] https://devtron.ai/blog/kubernetes-architecture-the-ultimate-guide/