"""
Modelo EOQ (Economic Order Quantity) y Punto de Pedido (Reorder Point)
Ámbito: Ingeniería en Organización Industrial - Gestión de Operaciones y Logística
Autor: Adrián Martín
"""

import math
from dataclasses import dataclass


@dataclass
class EOQResult:
    q_opt: float               # Lote económico óptimo (unidades)
    annual_holding_cost: float # Coste anual de almacenamiento/posesión (€)
    annual_ordering_cost: float# Coste anual de emisión/lanzamiento (€)
    total_inventory_cost: float# Coste total de gestión de inventario (€)
    orders_per_year: float     # Número de pedidos al año (N)
    cycle_time_days: float     # Tiempo entre pedidos en días (T)
    daily_demand: float        # Demanda diaria (d)
    reorder_point: float       # Punto de pedido (ROP) en unidades


class InventoryOptimizer:
    """
    Optimizador de inventarios basado en el modelo clásico de Wilson / Harris (EOQ).
    
    Parámetros:
    -----------
    annual_demand : float
        Demanda anual prevista (D) en unidades/año.
    order_cost : float
        Coste de preparación o lanzamiento por pedido (S) en €/pedido.
    holding_cost : float
        Coste unitario de posesión/almacenamiento anual (H) en €/unidad·año.
    lead_time_days : float
        Plazo de entrega del proveedor (L) en días laborables.
    safety_stock : float
        Stock de seguridad (SS) para amortiguar variabilidad en unidades.
    working_days : int
        Días laborables operativos al año (por defecto 250 días).
    """

    def __init__(
        self,
        annual_demand: float,
        order_cost: float,
        holding_cost: float,
        lead_time_days: float = 5.0,
        safety_stock: float = 0.0,
        working_days: int = 250,
    ):
        if annual_demand <= 0 or order_cost <= 0 or holding_cost <= 0:
            raise ValueError("Demanda, coste de emisión y posesión deben ser estrictamente positivos.")

        self.D = float(annual_demand)
        self.S = float(order_cost)
        self.H = float(holding_cost)
        self.L = float(lead_time_days)
        self.SS = float(safety_stock)
        self.working_days = working_days

    def calculate(self) -> EOQResult:
        """Calcula el lote económico, costes asociados y punto de reposición."""
        # 1. Lote Económico Óptimo (Fórmula de Wilson)
        q_opt = math.sqrt((2.0 * self.D * self.S) / self.H)

        # 2. Desglose de costes anuales
        ordering_cost = (self.D / q_opt) * self.S
        holding_cost = (q_opt / 2.0) * self.H
        total_cost = ordering_cost + holding_cost

        # 3. Frecuencia y tiempos de ciclo
        n_orders = self.D / q_opt
        cycle_time = self.working_days / n_orders

        # 4. Demanda media diaria y Punto de Pedido (ROP)
        daily_demand = self.D / self.working_days
        rop = (daily_demand * self.L) + self.SS

        return EOQResult(
            q_opt=q_opt,
            annual_holding_cost=holding_cost,
            annual_ordering_cost=ordering_cost,
            total_inventory_cost=total_cost,
            orders_per_year=n_orders,
            cycle_time_days=cycle_time,
            daily_demand=daily_demand,
            reorder_point=rop,
        )

    def print_report(self, product_name: str = "Componente Industrial"):
        """Genera un informe formateado por terminal."""
        res = self.calculate()
        print("=" * 65)
        print(f" INFORME DE OPTIMIZACIÓN DE INVENTARIO: {product_name.upper()}")
        print("=" * 65)
        print(" Parámetros de Entrada:")
        print(f"  • Demanda Anual (D):             {self.D:,.0f} uds/año")
        print(f"  • Coste de Lanzamiento (S):      {self.S:,.2f} €/pedido")
        print(f"  • Coste de Almacenamiento (H):   {self.H:,.2f} €/ud·año")
        print(f"  • Plazo de Entrega (Lead Time):  {self.L:.1f} días laborables")
        print(f"  • Stock de Seguridad (SS):       {self.SS:,.0f} uds")
        print("-" * 65)
        print(" Resultados Óptimos:")
        print(f"  ★ Lote Económico Óptimo (Q*):    {res.q_opt:,.1f} uds/pedido")
        print(f"  ★ Punto de Pedido (ROP):         {res.reorder_point:,.1f} uds")
        print(f"  • Frecuencia de Pedidos (N):     {res.orders_per_year:.2f} pedidos/año")
        print(f"  • Tiempo de Ciclo (T):           cada {res.cycle_time_days:.1f} días laborables")
        print("-" * 65)
        print(" Desglose de Costes Anuales:")
        print(f"  • Coste de Pedidos:              {res.annual_ordering_cost:,.2f} €/año")
        print(f"  • Coste de Almacenamiento:       {res.annual_holding_cost:,.2f} €/año")
        print(f"  ★ COSTE TOTAL ANUAL INVENTARIO:  {res.total_inventory_cost:,.2f} €/año")
        print("=" * 65)


if __name__ == "__main__":
    # Caso de Estudio: Gestión de inventario de rodamientos industriales en planta de montaje
    optimizer = InventoryOptimizer(
        annual_demand=12000,   # 12.000 rodamientos al año
        order_cost=45.0,       # 45 € por gestión de pedido y portes
        holding_cost=3.5,      # 3.50 €/unidad·año (coste financiero + espacio)
        lead_time_days=4.0,    # 4 días laborables de entrega
        safety_stock=100.0,    # 100 unidades de colchón de seguridad
        working_days=250       # 250 días hábiles
    )
    optimizer.print_report("Rodamiento de Precisión SKF-6205")
