# 📦 Optimización de Inventarios: Modelo EOQ & Punto de Pedido (ROP)

Modelo cuantitativo en Python para la optimización de inventarios y gestión de stocks en entornos industriales y de producción, desarrollado en el marco de la **Ingeniería en Organización Industrial** (UPV/EHU).

---

## 🎯 Objetivos del Proyecto

En logística y gestión de operaciones, mantener inventario conlleva costes contrapuestos:
1. **Coste de emisión/lanzamiento ($S$):** Coste administrativo y de preparación de cada pedido (aumenta cuanto más pedidos pequeños se hagan).
2. **Coste de posesión/almacenamiento ($H$):** Espacio en almacén, coste de oportunidad de capital, mermas y seguros (aumenta cuanto mayor sea el lote pedido).

El objetivo del **Lote Económico de Pedido (EOQ - *Economic Order Quantity*)** es determinar el tamaño de lote ($Q^*$) que minimiza el **Coste Total Anual de Inventario ($TC$)**.

---

## 📐 Formulación Matemática

### 1. Lote Económico Óptimo ($Q^*$)
Derivado del equilibrio entre costes de lanzamiento y posesión:
$$Q^* = \sqrt{\frac{2 \cdot D \cdot S}{H}}$$

Donde:
* $D$: Demanda anual prevista (unidades/año).
* $S$: Coste de emisión o preparación por pedido (€/pedido).
* $H$: Coste unitario anual de almacenamiento (€/unidad·año).

### 2. Punto de Pedido o Reorder Point ($ROP$)
Nivel de stock en el cual debe emitirse un nuevo pedido para no incurrir en rotura durante el tiempo de suministro (*Lead Time*):
$$ROP = (d \cdot L) + SS$$

Donde:
* $d$: Demanda diaria media ($d = \frac{D}{\text{días operativos}}$).
* $L$: Plazo de entrega del proveedor (*Lead Time*) en días laborables.
* $SS$: Stock de seguridad (*Safety Stock*) en unidades.

### 3. Frecuencia y Tiempo de Ciclo
* **Número de pedidos al año ($N$):** $N = \frac{D}{Q^*}$
* **Tiempo entre pedidos ($T$):** $T = \frac{\text{días operativos}}{N}$

---

## 🚀 Ejecución y Uso

Requisitos: Python 3.10+ (o mediante el gestor ultrarrápido `uv`).

```bash
# Ejecución directa con Python
python eoq_model.py

# O bien mediante uv
uv run python eoq_model.py
```

### Ejemplo de Salida

```text
=================================================================
 INFORME DE OPTIMIZACIÓN DE INVENTARIO: RODAMIENTO DE PRECISIÓN SKF-6205
=================================================================
 Parámetros de Entrada:
  • Demanda Anual (D):             12,000 uds/año
  • Coste de Lanzamiento (S):      45.00 €/pedido
  • Coste de Almacenamiento (H):   3.50 €/ud·año
  • Plazo de Entrega (Lead Time):  4.0 días laborables
  • Stock de Seguridad (SS):       100 uds
-----------------------------------------------------------------
 Resultados Óptimos:
  ★ Lote Económico Óptimo (Q*):    555.5 uds/pedido
  ★ Punto de Pedido (ROP):         292.0 uds
  • Frecuencia de Pedidos (N):     21.60 pedidos/año
  • Tiempo de Ciclo (T):           cada 11.6 días laborables
-----------------------------------------------------------------
 Desglose de Costes Anuales:
  • Coste de Pedidos:              972.11 €/año
  • Coste de Almacenamiento:       972.11 €/año
  ★ COSTE TOTAL ANUAL INVENTARIO:  1,944.22 €/año
=================================================================
```

---

## 👤 Autor

* **Adrián Martín**
* Grado en Ingeniería en Organización Industrial
* Universidad del País Vasco (UPV/EHU) – Escuela de Ingeniería de Bilbao
