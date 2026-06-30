import os
import re
import json
from collections import defaultdict
from datetime import datetime

def analizar_web():
    log_path = "lab1/access.log"
    print("--- INICIANDO PROCESAMIENTO WEB ---")
    
    if not os.path.exists(log_path):
        print(f"[ERROR] No existe el archivo: {log_path}")
        return

    # Patrones de inyección SQL solicitados
    sqli_patterns = [r"UNION", r"SELECT", r"--", r"OR\s+.*=.*", r"'"]
    sqli_regex = re.compile("|".join(sqli_patterns), re.IGNORECASE)
    
    ip_timestamps = defaultdict(list)
    errores_por_ip = defaultdict(lambda: {"4xx": 0, "5xx": 0})
    intentos_sqli = []
    lineas = 0
    
    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            lineas += 1
            parts = line.split()
            if not parts:
                continue
            ip = parts[0]
            
            # Buscar código de estado
            status_match = re.search(r'"\s+(\d{3})\s+', line)
            if status_match:
                status = int(status_match.group(1))
                if 400 <= status < 500:
                    errores_por_ip[ip]["4xx"] += 1
                elif 500 <= status < 600:
                    errores_por_ip[ip]["5xx"] += 1

            # Extraer la sección de la URL
            url_match = re.search(r'"[A-Z]+\s+(\S+)\s+HTTP', line)
            url = url_match.group(1) if url_match else line
            
            if sqli_regex.search(url):
                intentos_sqli.append({"ip": ip, "url": url.strip()})
            
            # Extraer fecha y hora
            time_match = re.search(r'\[([^\]]+)\]', line)
            if time_match:
                try:
                    time_str = time_match.group(1).split()[0]
                    dt = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S")
                    ip_timestamps[ip].append((dt, url))
                except:
                    pass

    print(f"[OK] Lineas procesadas exitosamente: {lineas}")

    # Detectar escaneo de directorios (>20 peticiones a rutas distintas en <60s)
    escaneos_detectados = []
    for ip, peticiones in ip_timestamps.items():
        peticiones.sort(key=lambda x: x[0])
        for i in range(len(peticiones)):
            inicio = peticiones[i][0]
            rutas = set()
            for j in range(i, len(peticiones)):
                if (peticiones[j][0] - inicio).total_seconds() <= 60:
                    rutas.add(peticiones[j][1])
                else:
                    break
            if len(rutas) > 20:
                escaneos_detectados.append({"ip": ip, "rutas_solicitadas": len(rutas)})
                print(f"[ALERTA WEB] Escaneo detectado de IP: {ip} ({len(rutas)} rutas en 60s)")
                break

    if intentos_sqli:
        print(f"[ALERTA WEB] Detectados {len(intentos_sqli)} intentos SQL Injection.")

    # Estructura del reporte JSON
    reporte = {
        "escaneos_directorios": escaneos_detectados,
        "errores_por_ip": errores_por_ip,
        "intentos_sql_injection": intentos_sqli
    }
    
    with open("lab1/reporte_web.json", "w", encoding="utf-8") as jf:
        json.dump(reporte, jf, indent=4)
    print("[FINALIZADO] Reporte guardado en lab1/reporte_web.json")

if __name__ == "__main__":
    analizar_web()