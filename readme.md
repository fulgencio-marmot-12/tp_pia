# Pokemon Huergo

Trabajo practico  de Laboratorio de Algoritmos y Estructuras de Datos

Motor logico (backend) de un juego estilo Pokemon que corre por consola, con menu interactivo. Implementa las principales estructuras de datos y algoritmos vistos en el ultimo bimestre.

## Estructura del proyecto


pokemon_huergo/
├── data/
│   ├── pokemones.json      # precarga de la pokedex (15 pokemon)
│   └── medallas.json       # precarga de medallas obtenidas
├── clases.py               # clases generales
├── lista_enlazada.py           # clases Nodo y ListaEnlazada 
├── stack.py                      # stack para deshacer transferencias
├── queque.py                       # queue para el centro pokemon
├── entrenador.py                  # equipo, pc, transferencias y captura
├── ordenamiento.py                 # bubble sort, insertion sort, quick sort
├── busqueda.py                      # busqueda lineal y busqueda binaria
├── main.py                           # menu principal, punto de entrada
└── analisis.txt                       # respuestas 


## Como correrlo

Se necesita Python 3


## Menu principal

```
1  ver pokedex
2  ver equipo principal
3  ver pc
4  capturar nuevo pokemon
5  ordenar pc
6  buscar pokemon en equipo
7  consultar pokemon por id en pokedex
8  enviar pokemon al centro pokemon
9  transferir pokemon al profesor oak
10 deshacer ultima transferencia
11 desafiar lider de gimnasio
12 salir del sistema
```

## Algunas aclaraciones

- Capturar genera un pokemon salvaje al azar . Si el equipo ya tiene 6, se manda solo a la PC.
- El stack de transferencias guarda como maximo los ultimos 5 pokemon transferidos, si se supera ese numero se descarta el mas viejo.
- Para ordenar la PC, la lista enlazada se copia a una lista de Python, se ordena ahi y despues se reconstruye la lista enlazada con el resultado.
- Ordenar por tipo agrupa a los pokemon por tipo ya que el ordenamiento es alfabetico sobre ese atributo.
- El resultado de cada desafio de gimnasio es aleatorio (gana o pierde).
- El analisis de complejidad del modulo 6 esta en `analisis.txt`.