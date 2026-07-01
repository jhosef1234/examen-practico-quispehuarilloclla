# Examen Práctico Final - Seguridad de Sistemas

**Autor:** Jhosef Anthony Quispe Huarilloclla  
**Fecha:** 30 Junio 2026  

## 📄 Descripción del Proyecto
Este repositorio contiene la resolución integral del examen práctico final. El proyecto está dividido en cuatro laboratorios enfocados en distintas áreas críticas de la ciberseguridad: análisis de logs mediante scripting en Python, configuración de SIEM con Wazuh, detección de anomalías usando Machine Learning, y visualización de eventos de seguridad (SOC) utilizando Grafana y Loki.

---

## 📂 Estructura del Repositorio

El repositorio está organizado en cuatro directorios principales, cada uno correspondiente a un laboratorio específico con sus respectivos scripts, datasets y evidencias de ejecución.

### 💻 Laboratorio 1: Procesamiento y Análisis de Logs (Python)
Desarrollo de scripts en Python para la ingesta, parseo y análisis de archivos log de servidores web (`access.log`) y sistemas Linux (`auth.log`), generando reportes estructurados y visualizaciones.

**Archivos principales:**
* `analizar_ssh.py`: Script para extraer intentos de conexión y geolocalización.
* `analizar_web.py`: Script para el análisis de tráfico web y códigos de estado HTTP.
* `visualizar.py`: Generador de gráficos de los datos procesados.
* `reporte_ssh.json` / `reporte_web.json`: Archivos de salida con los resultados.

**Evidencias (`lab1/evidencias/` y `lab1/graficas/`):**
* `SCR-1.1a_ssh_ejecucion.png` y `SCR-1.1b_ssh_json.png`: Ejecución y salida SSH.
* `SCR-1.2a_web_ejecucion.png` y `SCR-1.2b_web_json.png`: Ejecución y salida Web.
* Gráficas generadas: `heatmap_http.png`, `timeline_http.png`, `top10_ssh.png`.

---

### 🛡️ Laboratorio 2: Implementación de Reglas y Detección (Wazuh)
Creación e implementación de reglas personalizadas en el SIEM Wazuh para detectar tácticas específicas de ataque y validación de las mismas mediante la simulación controlada de incidentes.

**Archivos principales:**
* `local_rules_ssh.xml`: Reglas personalizadas para detección de ataques SSH.
* `local_rules_exfil.xml`: Reglas personalizadas para detección de exfiltración de datos.
* `simular_bruteforce.sh`: Script en Bash para simular ataques de fuerza bruta y activar las reglas.

**Evidencias (`lab2/evidencias/`):**
* `SCR-2.1_wazuh_activo.png`: Verificación del servicio Wazuh manager corriendo.
* `SCR-2.2_reglas_validadas.png`: Validación sintáctica de las reglas XML.
* `SCR-2.3_bruteforce_aler.png`: Captura de las alertas disparadas tras la ejecución del script.

---

### 🤖 Laboratorio 3: Machine Learning para Detección de Anomalías
Entrenamiento e implementación de un modelo de Machine Learning para identificar patrones anómalos dentro de un conjunto de datos de tráfico de red.

**Archivos principales:**
* `deteccion_anomalias_ipyn.ipynb`: Jupyter Notebook con el pipeline completo (EDA, preprocesamiento, entrenamiento y evaluación).
* `predecir.py`: Script para consumir los modelos exportados y predecir sobre nuevos datos.
* `network_traffic.csv`: Dataset utilizado para el entrenamiento.
* `modelo_anomalias.pkl` / `scaler_anomalias.pkl`: Modelo entrenado y escalador exportados para uso en producción.

**Evidencias (`lab3/evidencias/`):**
* `SCR-3.1_eda.png`: Análisis Exploratorio de Datos.
* `SCR-3.2_metricas.png`: Métricas de evaluación del modelo (Matriz de confusión, etc.).
* `SCR-3.3_umbral_f1.png`: Optimización del umbral (F1-Score).
* `SCR-3.4_predecir.png`: Ejecución exitosa del script de predicción `predecir.py`.

---

### 📊 Laboratorio 4: Monitoreo SOC (Grafana y Loki)
Despliegue de un panel de control (Dashboard) para un Centro de Operaciones de Seguridad (SOC), conectando Grafana con la base de datos de logs Loki (provenientes de Wazuh) y configurando alertas automatizadas.

**Archivos principales:**
* `dashboard_soc.json`: Exportación en formato JSON del Dashboard completo con las consultas LogQL configuradas.

**Evidencias (`lab4/evidencias/`):**
* `SCR-4.2_visualizaciones.png`: Visualizaciones individuales (Barras, Tabla Top 10, Timeline, Circular).
* `SCR-4.3_dashboard.png`: Dashboard completo integrado y funcional.
* `SCR-4.4_alerta.png`: Configuración de la regla de alerta de umbral crítico (> 5 eventos en 5 min).

---

## 🛠️ Requisitos y Tecnologías
* **Lenguajes:** Python 3.x, Bash, LogQL.
* **Bibliotecas de Python:** Pandas, Scikit-learn, Matplotlib, Seaborn, Json.
* **Herramientas de Seguridad y Monitoreo:** Wazuh (SIEM), Grafana, Loki.