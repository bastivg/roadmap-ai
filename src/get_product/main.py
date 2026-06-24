"""Punto de entrada: prueba la limpieza con datos de ejemplo."""

from mi_paquete.limpieza import Credito, limpiar, total_por_estado


def main() -> None:
    datos = [
        Credito(cliente="  Ana Pérez ", monto=1500.0, estado="Aprobado"),
        Credito(cliente="Juan Soto", monto=-200.0, estado="Rechazado"),  # monto inválido
        Credito(cliente="", monto=900.0, estado="Aprobado"),             # sin cliente
        Credito(cliente="María Díaz", monto=3000.0, estado="aprobado "),
    ]

    limpios = limpiar(datos)
    print(f"Registros válidos: {len(limpios)}")
    for r in limpios:
        print(f"  {r.cliente} | {r.monto} | {r.estado}")

    print("Totales por estado:", total_por_estado(limpios))


if __name__ == "__main__":
    main()