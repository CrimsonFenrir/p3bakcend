mysite/
├── calificaciones/   # App principal con modelos y vistas
├── api/              # Endpoints REST
├── consumers/        # Lógica de Kafka consumidor
├── producers/        # Lógica de Kafka productor
├── metrics/          # Integración Prometheus
├── docker-compose.yml
├── requirements.txt
└── manage.py





# 📘 Sistema de Calificaciones – Django + Kafka + Prometheus

## 🔎 Descripción general
Implementar una aplicación web en **Django** para gestionar calificaciones financieras y factores asociados. Integrar con **Kafka** para manejar eventos en tiempo real y con **Prometheus** para habilitar observabilidad del sistema.

El sistema combina:
- **Gestión de datos:** ofrecer CRUD completo de calificaciones y factores.
- **Streaming en tiempo real:** publicar y consumir eventos vía Kafka.
- **Monitoreo:** exponer métricas para Prometheus y visualizarlas en Grafana.
- **Carga masiva:** importar calificaciones desde archivos Excel.
- **API RESTful:** proporcionar endpoints modernos para integración con otros sistemas.

---

## 🎯 Funcionalidades principales
- Proveer interfaz web segura con login/logout y gestión de usuarios.
- Permitir creación, edición y eliminación de calificaciones y factores.
- Emitir eventos Kafka al crear o actualizar calificaciones.
- Procesar eventos Kafka mediante consumidor y persistir datos en base de datos.
- Importar calificaciones y factores desde archivos Excel.
- Exponer datos en formato JSON mediante API RESTful.
- Registrar métricas de uso y exponerlas en `/metrics`.
- Ejecutar pruebas unitarias para validar modelos y vistas.

---

## 🛠 Instalación

### 1. Requisitos previos
- **Python 3.10+** → https://www.python.org/downloads/
- **Docker Desktop (Windows)** → https://www.docker.com/products/docker-desktop
- **Git** → https://git-scm.com/downloads
- **Prometheus** → https://prometheus.io/download/
- **Grafana** → https://grafana.com/grafana/download

### 2. Clonar repositorio
``bash
git clone https://github.com/CrimsonFenrir/p3backend
cd mysite
3. Crear entorno virtual
bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
4. Instalar dependencias
bash
pip install -r requirements.txt
5. Aplicar migraciones
bash
python manage.py migrate
🚀 Ejecución del servidor
Levantar el servidor en modo seguro con certificados SSL:

bash
python manage.py runserver_plus --cert ../certs/cert.pem --key ../certs/key.pem
--cert: apuntar al certificado SSL (cert.pem).

--key: apuntar a la clave privada (key.pem).

Ubicación: colocar ambos archivos en ../certs/.

🔑 Credenciales iniciales
Superusuario preconfigurado:

Usuario: admin

Contraseña: 123admin

Acceder al panel de administración en /admin o al login de la aplicación en /login.

🐳 Kafka en Docker Desktop (Windows)
Pasos
Instalar Docker Desktop y habilitar WSL2.

Utilizar archivo docker-compose.yml existente.

Levantar servicios:

bash
docker-compose up -d
Verificar disponibilidad:

Zookeeper: localhost:2181

Kafka broker: localhost:9092

Configurar la aplicación para conectarse automáticamente a localhost:9092.

📊 Monitoreo con Prometheus
Acceder a /metrics para obtener métricas en formato Prometheus.

Métricas disponibles:

login_total → logins exitosos.

calificacion_creada_total → calificaciones creadas.

calificacion_actualizada_total → calificaciones actualizadas.

calificacion_importada_total → calificaciones importadas.

Integrar con Grafana para visualización avanzada.

🌐 Navegación rápida
Login → /login

Lista de calificaciones → /calificaciones

API RESTful → /api/

API JSON básica → /api/calificaciones/json/

Métricas Prometheus → /metrics

Panel de administración Django → /admin

📈 Casos de uso
Gestionar y analizar instrumentos financieros con factores de riesgo.

Simular flujos de datos en tiempo real mediante Kafka.

Integrar observabilidad en entornos DevOps con Prometheus/Grafana.

Proveer API RESTful para aplicaciones móviles o sistemas externos.

✅ Checklist de funcionalidades
[x] Autenticación y gestión de usuarios.

[x] CRUD de calificaciones y factores.

[x] Integración con Kafka (productor y consumidor).

[x] Importación desde Excel.

[x] API RESTful con Django REST Framework.

[x] Monitoreo con Prometheus.

[x] Pruebas unitarias incluidas.

[x] Ejecución segura con certificados SSL.

[x] Credenciales iniciales documentadas.

📌 Conclusión
Consolidar una aplicación profesional lista para producción que combina gestión de datos, streaming en tiempo real y observabilidad. Proporcionar una plataforma robusta, extensible y fácil de integrar en entornos financieros, analíticos o tecnológicos.
