# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import json
import re
from collections import Counter, defaultdict
from datetime import datetime

print("--- INICIANDO GENERACION DE GRAFICAS HTTP Y SSH ---")

# 1. Grafico de barras: Top 10 IPs con mas intentos fallidos SSH leyendo de auth.log
try:
    failed_attempts = []
    pattern = re.compile(r"Failed password for .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    
    with open("lab1/auth.log", "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                failed_attempts.append(match.group(1))
                
    contador_ips = Counter(failed_attempts)
    top_10 = contador_ips.most_common(10)
    
    ips = [item[0] for item in top_10]
    intentos = [item[1] for item in top_10]

    plt.figure(figsize=(10, 5))
    plt.barh(ips[::-1], intentos[::-1], color='crimson')
    plt.title("Top 10 IPs con Mas Intentos Fallidos SSH")
    plt.xlabel("Numero de Intentos")
    plt.ylabel("Direcciones IP")
    plt.tight_layout()
    plt.savefig("lab1/graficas/top10_ssh.png")
    plt.close()
    print("[OK] Grafica 1 generada exitosamente: top10_ssh.png")
except Exception as e:
    print(f"[ERROR Grafica 1]: {e}")

# Parsear access.log para las graficas HTTP
horas_peticiones = []
matriz_calor = defaultdict(lambda: defaultdict(int))
log_pattern = re.compile(r'\S+ \S+ \S+ \[(?P<time>[^\]]+)\] "\S+ \S+\s*.*?" (?P<status>\d{3})')

try:
    with open("lab1/access.log", "r") as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                status = data['status']
                time_str = data['time'].split()[0]
                dt = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S")
                hora = dt.hour
                horas_peticiones.append(hora)
                if status in ['200', '301', '404', '500']:
                    matriz_calor[hora][status] += 1

    # 2. Linea de tiempo - Numero de peticiones HTTP por hora
    counts_hora = Counter(horas_peticiones)
    df_linea = pd.DataFrame(sorted(counts_hora.items()), columns=['Hora', 'Peticiones'])

    plt.figure(figsize=(10, 4))
    plt.plot(df_linea['Hora'], df_linea['Peticiones'], marker='o', color='royalblue', linewidth=2)
    plt.title("Numero de Peticiones HTTP por Hora durante el Dia")
    plt.xlabel("Hora del Dia (0-23)")
    plt.ylabel("Cantidad de Peticiones")
    plt.xticks(range(0, 24))
    plt.grid(True, linestyle='--')
    plt.tight_layout()
    plt.savefig("lab1/graficas/timeline_http.png")
    plt.close()
    print("[OK] Grafica 2 generada exitosamente: timeline_http.png")

    # 3. Representacion de codigos de respuesta por hora
    df_heatmap = pd.DataFrame(matriz_calor).T.fillna(0)
    for col in ['200', '301', '404', '500']:
        if col not in df_heatmap.columns:
            df_heatmap[col] = 0
    df_heatmap = df_heatmap[['200', '301', '404', '500']].sort_index()

    plt.figure(figsize=(10, 6))
    for col in df_heatmap.columns:
        plt.plot(df_heatmap.index, df_heatmap[col], label=f"Status {col}", marker='s')
    plt.title("Distribucion de Peticiones por Hora y Codigo de Respuesta")
    plt.xlabel("Hora del Dia")
    plt.ylabel("Cantidad de Eventos")
    plt.xticks(range(0, 24))
    plt.legend()
    plt.grid(True, linestyle=':')
    plt.tight_layout()
    plt.savefig("lab1/graficas/heatmap_http.png")
    plt.close()
    print("[OK] Grafica 3 generada exitosamente: heatmap_http.png")

except Exception as e:
    print(f"[ERROR Graficas Web]: {e}")

print("--- PROCESO DE VISUALIZACION FINALIZADO ---")
