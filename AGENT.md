# AGENT.md — Claim Deck's Randomizer

> Documento de referencia para IAs generativas. Describe la arquitectura, lógica de dominio, convenciones y patrones del proyecto para facilitar la comprensión, el mantenimiento y la extensión del código.

---

## 1. Visión general del proyecto

**Claim Deck's Randomizer** es una herramienta de consola escrita en **Python** que genera mazos aleatorios para el juego de cartas **Claim** (distribuido por SD Games). Su propósito es ayudar a los jugadores a crear combinaciones de facciones de forma rápida y equilibrada, respetando las reglas del juego sobre facciones emparejadas y no emparejadas.

- **Lenguaje**: Python 100%
- **Interfaz**: Consola/terminal (CLI)
- **Dependencias externas**: ninguna (solo librería estándar: `random`, `time`)
- **Repositorio**: `https://github.com/darchery/Claim-deck-s-randomizer`

---

## 2. Estructura del repositorio

```
Claim-deck-s-randomizer/
├── src/               # Código fuente principal
├── installer/         # Scripts o recursos de instalación
├── resources/         # Recursos adicionales (datos, assets, etc.)
└── README.md          # Documentación del proyecto
```

> **Nota para la IA**: El archivo principal de lógica se encuentra en `src/`. Toda modificación de lógica de negocio debe realizarse allí.

---

## 3. Dominio del problema — El juego Claim

### 3.1 Concepto clave: tipos de facciones

El juego Claim distingue dos tipos de facciones que determinan cómo se construye un mazo:

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Paired (emparejadas)** | Dos facciones que siempre van juntas en el mazo | Goblins + Knights |
| **Unpaired (no emparejadas)** | Facciones independientes que se añaden individualmente | Dwarves, Undeads |

### 3.2 Catálogo completo de facciones

#### Base: Claim I
- **Emparejadas**: `Goblins` ↔ `Knights`
- **No emparejadas**: `Doppelgangers`, `Dwarves`, `Undeads`

#### Base: Claim II
- **Emparejadas**: `Giants` ↔ `Gnomes`
- **No emparejadas**: `Dragons`, `Seers`, `Trolls`

#### Base: Claim V (Edición Aniversario)
- **Emparejadas**: `Royalty` ↔ `Peasants`
- **No emparejadas**: `Automatons`, `Bards`, `Raccoons`, `Vikings`, `Griffins`

#### Expansión: Fear
- **No emparejadas**: `Shadows`, `Vampires`, `Werewolves`, `Zombies`

#### Expansión: Frost
- **Emparejadas**: `Ice Queen` ↔ `King`
- **No emparejadas**: `Yetis`, `Ice Beasts`

#### Expansión: Maps
- **Emparejadas**: `Basilisks` ↔ `Unicorns`
- **No emparejadas**: `Phoenixes`

#### Expansión: Mercenaries
- **Emparejadas**: `Orcs` ↔ `Elves` (y su variante `Elves and Orcs`)
- **No emparejadas**: `Cyclops`

#### Expansión: Magic
- **No emparejadas**: `Druids`, `Shape shifters`, `Wizards`

#### Expansión: Fire
- **No emparejadas**: `Demons`, `Fire Elementals`, `Poisoners`, `Tricksters`

---

## 4. Arquitectura del código

### 4.1 Variables globales de estado

Estas cuatro variables representan el estado completo del programa en tiempo de ejecución. **Toda la lógica las modifica o consulta**:

```python
globalListOfPairedFactions    # list — facciones emparejadas actualmente en el pool
globalListOfNonPairedFactions # list — facciones no emparejadas en el pool
expansionsNotAdded            # list — expansiones disponibles aún no añadidas
expansionsAdded               # list — expansiones que el usuario ha activado
```

> **Patrón de estado**: El programa es stateful dentro de la sesión. No hay persistencia a disco: al salir, el estado se pierde.

### 4.2 Mapa de funciones

```
FLUJO PRINCIPAL
└── main loop
    ├── printLogo()                          # Muestra logo ASCII decorativo
    ├── printGeneralOptions()                # Muestra menú principal
    └── deploySelectOptionsAndTakeInput()    # Lee opción del usuario
        ├── [opción: gestionar expansiones]
        │   ├── printAddDeleteOptions()
        │   └── delployAddDeleteOptionsAndTakeInput()
        │       ├── showExpansionsAndFactions()     # Ver estado actual
        │       ├── addExpansionInput()             # Añadir expansión concreta
        │       │   └── addAnExpansion(inputAdd)
        │       ├── removeExpansionInput()          # Quitar expansión
        │       │   └── removeAnExpansion(inputDelete)
        │       ├── addAllExpansionsToPool()        # Añadir todas
        │       │   └── addEveryFaction()
        │       └── cleanPool()                     # Resetear todo
        │
        └── [opción: generar mazo]
            ├── takeNumberOfPlayersInput()          # Validar nº jugadores
            ├── chooseNumberOfFactions()            # Calcular cuántas facciones
            └── generateRandomDeck()               # Selección aleatoria final
```

### 4.3 Lógica de generación del mazo

La función `generateRandomDeck()` sigue este algoritmo:

1. Llama a `chooseNumberOfFactions()` para determinar `N` (número de facciones según jugadores).
2. Selecciona aleatoriamente pares de `globalListOfPairedFactions` usando `random`.
3. Completa el mazo con facciones de `globalListOfNonPairedFactions` hasta alcanzar `N`.
4. Imprime el mazo resultante en consola.

> **Regla de dominio crítica**: Las facciones emparejadas deben tratarse como una unidad. Si se selecciona una, la otra entra automáticamente. Esto implica que cada entrada en `globalListOfPairedFactions` representa un *par completo*, no una facción individual.

### 4.4 Funciones de utilidad

```python
printSpace()       # Salto de línea para formato visual
goodByeMessage()   # Mensaje de despedida + time.sleep() antes de cerrar
printLogo()        # Logo ASCII art del programa
```

---

## 5. Flujo de usuario (UX de consola)

```
Inicio
  │
  ▼
[Menú principal]
  ├── 1. Añadir/Quitar expansiones  →  [Submenú expansiones]
  │       ├── Ver expansiones activas
  │       ├── Añadir expansión específica
  │       ├── Quitar expansión específica
  │       ├── Añadir todas las expansiones
  │       └── Limpiar todo el pool
  │
  ├── 2. Generar mazo aleatorio
  │       ├── Input: número de jugadores (validado)
  │       ├── Cálculo de facciones necesarias
  │       └── Output: mazo impreso en consola
  │
  └── 3. Salir  →  goodByeMessage()  →  Fin
```

---

## 6. Convenciones y patrones del proyecto

| Aspecto | Convención |
|---------|------------|
| **Idioma del código** | Inglés (nombres de funciones, variables, comentarios) |
| **Idioma del juego** | Inglés (nombres de facciones y expansiones) |
| **Estilo de nombres** | `camelCase` para funciones y variables |
| **Interacción** | Todo via `input()` e `print()` en consola |
| **Validación de input** | La función `takeNumberOfPlayersInput()` valida explícitamente |
| **Pausas visuales** | `time.sleep()` para dar feedback temporal al usuario |
| **Sin frameworks** | Solo stdlib de Python, sin dependencias externas |

---

## 7. Guía para modificaciones frecuentes

### Añadir una nueva expansión

1. Definir sus facciones emparejadas y no emparejadas como listas/tuplas.
2. Añadir la expansión a `expansionsNotAdded` en la inicialización.
3. Implementar su caso en `addAnExpansion()` y `removeAnExpansion()`.
4. Actualizar `addEveryFaction()` para incluir las nuevas facciones.

### Cambiar la tabla de facciones por número de jugadores

Modificar la función `chooseNumberOfFactions()`. Actualmente mapea `nº de jugadores → nº de facciones` según las reglas oficiales de Claim.

### Añadir persistencia de estado

El proyecto no tiene persistencia. Para añadirla, se debería serializar `expansionsAdded` (e.g., en JSON) y cargarlo al inicio del programa, antes de mostrar el menú principal.

### Migrar a interfaz gráfica o web

El estado reside en variables globales. Para migrar, encapsular el estado en una clase (e.g., `DeckSession`) y exponer sus métodos como API. Las funciones de visualización (`print*`) deberían separarse de la lógica de negocio.

---

## 8. Limitaciones conocidas

- **Sin tests automatizados**: No hay suite de tests en el repositorio.
- **Estado global mutable**: Dificulta el testing unitario y la concurrencia.
- **Sin persistencia**: El usuario debe reconfigurar las expansiones en cada ejecución.
- **Sin internacionalización**: Las facciones están hardcoded en inglés.

---

## 9. Referencia rápida para la IA

| Pregunta | Respuesta |
|----------|-----------|
| ¿En qué lenguaje está? | Python (stdlib únicamente) |
| ¿Dónde está la lógica principal? | `src/` |
| ¿Cómo se representa el estado? | Variables globales (`globalListOf*`, `expansions*`) |
| ¿Cómo se genera el mazo? | `generateRandomDeck()` con `random` |
| ¿Qué distingue facciones? | Paired vs Unpaired (emparejadas vs independientes) |
| ¿Hay base de datos? | No, todo es en memoria durante la sesión |
| ¿Hay tests? | No hay tests en el repositorio actualmente |
| ¿Interfaz? | Exclusivamente consola/CLI |

---

*Generado automáticamente a partir del análisis del repositorio `darchery/Claim-deck-s-randomizer`.*
