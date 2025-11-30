#ifndef GRAFO_BASE_H
#define GRAFO_BASE_H

#include <vector>
#include <string>
#include <utility>

/**
 * Clase Abstracta GrafoBase
 * Define la interfaz para todas las implementaciones de grafos
 */
class GrafoBase {
public:
    virtual ~GrafoBase() {}
    
    // Métodos virtuales puros
    virtual void cargarDatos(const std::string& nombreArchivo) = 0;
    virtual std::vector<int> BFS(int nodoInicio, int profundidadMaxima) = 0;
    virtual int obtenerGrado(int nodo) = 0;
    virtual std::vector<int> getVecinos(int nodo) = 0;
    virtual int obtenerNumNodos() const = 0;
    virtual int obtenerNumAristas() const = 0;
    virtual std::pair<int, int> obtenerNodoMaxGrado() = 0;
    virtual std::vector<std::pair<int, int>> obtenerAristasSubgrafo(const std::vector<int>& nodos) = 0;
};

#endif // GRAFO_BASE_H
