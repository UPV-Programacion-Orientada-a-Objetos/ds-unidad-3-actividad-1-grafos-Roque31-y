#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Prueba del Backend de NeuroNet (sin GUI)
"""

import sys

print("="*60)
print("  NeuroNet - Prueba de Backend C++")
print("="*60)

# Verificar si el módulo está compilado
try:
    import neuronet_core
    print("✅ Módulo neuronet_core importado correctamente\n")
except ImportError as e:
    print("❌ ERROR: No se pudo importar neuronet_core")
    print("   Ejecute primero: python setup.py build_ext --inplace")
    print(f"   Detalle: {e}")
    sys.exit(1)

# Crear instancia del grafo
print("Creando instancia de PyGrafoDisperso...")
grafo = neuronet_core.PyGrafoDisperso()
print("✅ Instancia creada\n")

# Cargar dataset de prueba
archivo = "test_graph.txt"
print(f"Cargando dataset: {archivo}")
try:
    grafo.cargar_datos(archivo)
    print("✅ Dataset cargado\n")
except Exception as e:
    print(f"❌ ERROR al cargar dataset: {e}")
    sys.exit(1)

# Mostrar estadísticas
print("-" * 60)
print("ESTADÍSTICAS DEL GRAFO")
print("-" * 60)

num_nodos = grafo.obtener_num_nodos()
num_aristas = grafo.obtener_num_aristas()
memoria = grafo.obtener_memoria_estimada()

print(f"Nodos:    {num_nodos}")
print(f"Aristas:  {num_aristas}")
print(f"Memoria:  {memoria / 1024:.2f} KB ({memoria} bytes)")
print()

# Nodo con mayor grado
nodo_max, grado_max = grafo.obtener_nodo_max_grado()
print(f"Nodo con Mayor Grado: {nodo_max}")
print(f"Grado:                {grado_max}")
print()

# Probar algunos nodos individuales
print("-" * 60)
print("ANÁLISIS DE NODOS INDIVIDUALES")
print("-" * 60)

for nodo_id in [0, 1, 5]:
    grado = grafo.obtener_grado(nodo_id)
    vecinos = grafo.get_vecinos(nodo_id)
    print(f"Nodo {nodo_id}:")
    print(f"  Grado:   {grado}")
    print(f"  Vecinos: {vecinos}")
    print()

# Ejecutar BFS
print("-" * 60)
print("BÚSQUEDA BFS")
print("-" * 60)

nodo_inicio = 0
profundidad = 2

print(f"Ejecutando BFS desde nodo {nodo_inicio} con profundidad {profundidad}...\n")

nodos_visitados = grafo.bfs(nodo_inicio, profundidad)

print(f"\nNodos visitados ({len(nodos_visitados)}):")
print(nodos_visitados)
print()

# Obtener aristas del subgrafo
aristas = grafo.obtener_aristas_subgrafo(nodos_visitados)
print(f"Aristas en el subgrafo ({len(aristas)}):")
for origen, destino in aristas[:10]:  # Mostrar solo las primeras 10
    print(f"  {origen} -> {destino}")
if len(aristas) > 10:
    print(f"  ... y {len(aristas) - 10} más")
print()

# Imprimir estadísticas completas
print("-" * 60)
grafo.imprimir_estadisticas()
print("-" * 60)

print("\n✅ Todas las pruebas completadas exitosamente!")
print("\nPara usar la interfaz gráfica, ejecute:")
print("    python neuronet_gui.py")
