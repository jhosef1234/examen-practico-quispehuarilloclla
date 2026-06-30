# Examen Final: Analítica de Datos y Reglas de Correlación Avanzada en Entornos SOC

Este repositorio contiene el desarrollo práctico del examen final, enfocado en el análisis de logs de seguridad, entrenamiento de modelos de Machine Learning para la detección de anomalías de red y el despliegue de reglas HIDS.

## 👥 Integrantes
* **Jhosef** - Estudiante de Ingeniería de Sistemas

---

## 📊 Laboratorio 1: Análisis Exploratorio de Datos (EDA) y Procesamiento de Logs (`lab1/`)
Implementación de scripts en Python para la ingesta, parseo y análisis estadístico de logs de servidores web y de autenticación.

### Componentes y Archivos
* `auth.log` y `access.log`: Datasets crudos de auditoría del sistema.
* `analizar_ssh.py` y `analizar_web.py`: Scripts de extracción de características y generación de estructuras estructurales.
* `reporte_ssh.json` y `reporte_web.json`: Datos limpios estructurados listos para analítica.

### Evidencias de Ejecución (Estructura de Datos)
* **SCR-1.1a_ssh_ejecucion.png:** Ejecución del pipeline de procesamiento del protocolo SSH.
* **SCR-1.1b_ssh_json.png:** Formateo y serialización de eventos de autenticación a formato JSON de auditoría.
* **SCR-1.2a_web_ejecucion.png:** Parseo de peticiones y códigos de estado HTTP (logs Apache/Nginx).
* **SCR-1.2b_web_json.png:** Almacenamiento JSON de telemetría de tráfico web.

### Gráficas de Telemetría Generadas (`lab1/graficas/`)
* `heatmap_http.png`: Matriz de calor de densidad de peticiones HTTP por hora/IP.
* `timeline_http.png`: Línea de tiempo secuencial de ráfagas e inyecciones de tráfico anómalo.
* `top10_ssh.png`: Distribución estadística de los vectores IP con mayor tasa de fallos de autenticación.

---

## 🛡️ Laboratorio 2: Despliegue de Reglas Personalizadas HIDS (Wazuh) (`lab2/`)
Despliegue defensivo en caliente mediante el aprovisionamiento de firmas de detección de intrusos.

### Configuraciones XML Desplegadas
* **`local_rules_ssh.xml` (ID: 100001):** Firma basada en umbrales de frecuencia para mitigar ataques activos de Fuerza Bruta SSH (Frecuencia: 10 intentos / Ventana: 60s).
* **`local_rules_exfil.xml` (ID: 100002, 100003):** Correlación lógica orientada a la identificación de accesos en horario nocturno no habitual (22:00 a 06:00) correlacionados con payloads de exfiltración masiva de datos corporativos salientes.

### Evidencias de Cumplimiento
* **SCR-2.1_wazuh_activo.png:** Estado operativo del daemon de control (`wazuh-manager`) inicializado correctamente en el core del SOC.
* **SCR-2.2_reglas_validadas.png:** Análisis de carga sintáctica XML e integración de firmas perimetrales.
* **SCR-2.3.png:** Ejecución interactiva del motor de simulación (`wazuh-logtest`) validando el flujo completo de alertas y mapeo bajo la taxonomía de la matriz MITRE ATT&CK.

---

## 🔍 Laboratorio 3: Detección de Anomalías con Machine Learning (`lab3/`)
Despliegue de un pipeline analítico predictivo para clasificar tráfico malicioso y vectores de exfiltración mediante modelos de aprendizaje automático no supervisado / supervisado.

### Artefactos del Modelo
* `network_traffic.csv`: Dataset de vectores de red estructurados para el entrenamiento.
* `scaler_anomalias.pkl`: Objeto de normalización estadística de características numéricas.
* `modelo_anomalias.pkl`: Modelo entrenado y persistido para la detección de intrusiones.
* `predecir.py`: Script de inferencia en tiempo real para la clasificación de nuevos vectores incidentes.

### Evidencias del Pipeline Predictivo
* **SCR-3.1_eda.png:** Distribución de densidad y correlación de variables críticas del tráfico de red.
* **SCR-3.2_metricas.png:** Evaluación del modelo (Matriz de confusión, curvas Precision-Recall y F1-Score).
* **SCR-3.3_umbral_f1.png:** Optimización del umbral de decisión matemática para minimizar falsos negativos.
* **SCR-3.4_predecir.png:** Inferencia de producción clasificando anomalías y tráfico benigno en tiempo real.

---

## 🚀 Laboratorio 4: Simulación de Ataque Perimetral con Netcat (`lab4/`)
Auditoría ofensiva y pruebas de conectividad de sockets de red para validar el comportamiento defensivo del entorno corporativo.

### Metodología de Simulación Técnica
1. **Reconocimiento y Port Scanning:** Simulación de recopilación de información exterior hacia los puertos expuestos del servidor:
   ```bash
   nc -zv 192.168.1.80 22-80