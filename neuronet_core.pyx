# distutils: language = c++
# distutils: sources = cpp/GrafoDisperso.cpp

from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.pair cimport pair

# Declaración de la clase C++
cdef extern from "cpp/GrafoDisperso.h":
    cdef cppclass GrafoDisperso:
        GrafoDisperso() except +
        void cargarDatos(const string& nombreArchivo)
        vector[int] BFS(int nodoInicio, int profundidadMaxima)
        int obtenerGrado(int nodo)
        vector[int] getVecinos(int nodo)
        int obtenerNumNodos()
        int obtenerNumAristas()
        pair[int, int] obtenerNodoMaxGrado()
        vector[pair[int, int]] obtenerAristasSubgrafo(const vector[int]& nodos)
        void imprimirEstadisticas()
        size_t obtenerMemoriaEstimada()

# Wrapper de Python
cdef class PyGrafoDisperso:
    cdef GrafoDisperso* c_grafo  # Puntero a la instancia C++
    
    def __cinit__(self):
        """Constructor - crea la instancia de C++"""
        self.c_grafo = new GrafoDisperso()
    
    def __dealloc__(self):
        """Destructor - libera memoria de C++"""
        del self.c_grafo
    
    def cargar_datos(self, str nombre_archivo):
        """
        Carga un archivo de grafo en formato Edge List
        
        Args:
            nombre_archivo: Ruta al archivo .txt con formato "NodoOrigen NodoDestino"
        """
        cdef string c_nombre = nombre_archivo.encode('utf-8')
        self.c_grafo.cargarDatos(c_nombre)
    
    def bfs(self, int nodo_inicio, int profundidad_maxima):
        """
        Ejecuta búsqueda en anchura (BFS) desde un nodo inicial
        
        Args:
            nodo_inicio: ID del nodo desde donde iniciar
            profundidad_maxima: Número máximo de niveles a explorar
            
        Returns:
            Lista de IDs de nodos visitados
        """
        cdef vector[int] resultado = self.c_grafo.BFS(nodo_inicio, profundidad_maxima)
        return list(resultado)
    
    def obtener_grado(self, int nodo):
        """
        Obtiene el grado de salida de un nodo
        
        Args:
            nodo: ID del nodo
            
        Returns:
            Número de aristas salientes del nodo
        """
        return self.c_grafo.obtenerGrado(nodo)
    
    def get_vecinos(self, int nodo):
        """
        Obtiene los vecinos (nodos adyacentes) de un nodo
        
        Args:
            nodo: ID del nodo
            
        Returns:
            Lista de IDs de vecinos
        """
        cdef vector[int] vecinos = self.c_grafo.getVecinos(nodo)
        return list(vecinos)
    
    def obtener_num_nodos(self):
        """Retorna el número total de nodos en el grafo"""
        return self.c_grafo.obtenerNumNodos()
    
    def obtener_num_aristas(self):
        """Retorna el número total de aristas en el grafo"""
        return self.c_grafo.obtenerNumAristas()
    
    def obtener_nodo_max_grado(self):
        """
        Encuentra el nodo con el mayor grado de salida
        
        Returns:
            Tupla (nodo_id, grado)
        """
        cdef pair[int, int] resultado = self.c_grafo.obtenerNodoMaxGrado()
        return (resultado.first, resultado.second)
    
    def obtener_aristas_subgrafo(self, list nodos):
        """
        Obtiene todas las aristas entre un conjunto de nodos
        
        Args:
            nodos: Lista de IDs de nodos
            
        Returns:
            Lista de tuplas (origen, destino) representando aristas
        """
        cdef vector[int] c_nodos = nodos
        cdef vector[pair[int, int]] aristas = self.c_grafo.obtenerAristasSubgrafo(c_nodos)
        
        # Convertir a lista de Python
        resultado = []
        for i in range(aristas.size()):
            resultado.append((aristas[i].first, aristas[i].second))
        
        return resultado
    
    def imprimir_estadisticas(self):
        """Imprime estadísticas del grafo en consola"""
        self.c_grafo.imprimirEstadisticas()
    
    def obtener_memoria_estimada(self):
        """
        Calcula la memoria estimada usada por el grafo
        
        Returns:
            Memoria en bytes
        """
        return self.c_grafo.obtenerMemoriaEstimada()
