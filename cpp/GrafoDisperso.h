#ifndef GRAFO_DISPERSO_H
#define GRAFO_DISPERSO_H

#include "GrafoBase.h"
#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <utility>

/**
 * Clase GrafoDisperso
 * Implementación de un grafo usando formato CSR (Compressed Sparse Row)
 * para optimizar el uso de memoria en grafos masivos poco densos
 */
class GrafoDisperso : public GrafoBase {
private:
    // Formato CSR: Compressed Sparse Row
    std::vector<int> row_ptr;      // Punteros de inicio de cada fila
    std::vector<int> col_indices;  // Índices de columnas (destinos)
    
    int num_nodos;
    int num_aristas;
    
    // Mapeo de IDs originales a índices internos
    std::map<int, int> id_to_index;
    std::map<int, int> index_to_id;
    int siguiente_indice;

public:
    GrafoDisperso();
    ~GrafoDisperso();
    
    // Implementación de métodos abstractos
    void cargarDatos(const std::string& nombreArchivo) override;
    std::vector<int> BFS(int nodoInicio, int profundidadMaxima) override;
    int obtenerGrado(int nodo) override;
    std::vector<int> getVecinos(int nodo) override;
    int obtenerNumNodos() const override;
    int obtenerNumAristas() const override;
    std::pair<int, int> obtenerNodoMaxGrado() override;
    std::vector<std::pair<int, int>> obtenerAristasSubgrafo(const std::vector<int>& nodos) override;
    
    // Utilidades
    void imprimirEstadisticas() const;
    size_t obtenerMemoriaEstimada() const;
    
private:
    int obtenerIndice(int id);
    int obtenerId(int indice);
};

#endif // GRAFO_DISPERSO_H
