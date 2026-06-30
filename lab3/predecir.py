# -*- coding: utf-8 -*-
import sys
import os
import pandas as pd
import joblib

def predecir_nuevo_trafico(csv_path):
    if not os.path.exists("modelo_anomalias.pkl") or not os.path.exists("scaler_anomalias.pkl"):
        print("Error: No se encontraron los archivos modelo_anomalias.pkl o scaler_anomalias.pkl.")
        return
        
    if not os.path.exists(csv_path):
        print(f"Error: El archivo {csv_path} no existe.")
        return
        
    # Cargar el modelo y el Scaler
    model = joblib.load("modelo_anomalias.pkl")
    scaler = joblib.load("scaler_anomalias.pkl")
    
    # Leer archivo
    df = pd.read_csv(csv_path)
    
    # Feature Engineering
    df['ratio_bytes'] = df['bytes_sent'] / (df['bytes_recv'] + 1)
    df['bytes_por_segundo'] = (df['bytes_sent'] + df['bytes_recv']) / (df['duration_sec'] + 0.1)
    
    features = ['bytes_sent', 'bytes_recv', 'duration_sec', 'packets', 'ratio_bytes', 'bytes_por_segundo']
    
    # Escalar datos
    X_scaled = scaler.transform(df[features])
    
    # Predecir
    df['pred'] = model.predict(X_scaled)
    df['score'] = model.decision_function(X_scaled)
    
    # Filtrar anomalias
    anomalias = df[df['pred'] == -1]
    
    print(f"\n--- CLASIFICACION DE TRAFICO DE CONSOLA SOC: {csv_path} ---")
    print(f"Registros evaluados: {len(df)} | Anomalias criticas detectadas: {len(anomalias)}")
    print("------------------------------------------------------------------")
    
    if not anomalias.empty:
        print(anomalias[['src_ip', 'dst_ip', 'dst_port', 'bytes_sent', 'score']].head(20).to_string(index=False))
    else:
        print("Trafico limpio. No se detectaron anomalias.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python predecir.py <ruta_del_archivo_nuevo.csv>")
    else:
        predecir_nuevo_trafico(sys.argv[1])
