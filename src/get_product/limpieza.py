"""Módulo de limpieza de registros de crédito."""

from dataclasses import dataclass


@dataclass
class Credito:
    """Un registro de crédito."""
    cliente: str
    monto: float
    estado: str


def normalizar_texto(texto: str) -> str:
    """Quita espacios sobrantes y pasa a minúsculas."""
    return texto.strip().lower()


def es_valido(registro: Credito) -> bool:
    """Un registro es válido si el monto es positivo y tiene cliente."""
    return registro.monto > 0 and registro.cliente.strip() != ""


def limpiar(registros: list[Credito]) -> list[Credito]:
    """Devuelve solo los registros válidos, con texto normalizado."""
    limpios: list[Credito] = []
    for r in registros:
        if es_valido(r):
            limpios.append(
                Credito(
                    cliente=normalizar_texto(r.cliente),
                    monto=r.monto,
                    estado=normalizar_texto(r.estado),
                )
            )
    return limpios


def total_por_estado(registros: list[Credito]) -> dict[str, float]:
    """Suma los montos agrupados por estado."""
    totales: dict[str, float] = {}
    for r in registros:
        totales[r.estado] = totales.get(r.estado, 0.0) + r.monto
    return totales