# Script que CONSOME o módulo (funções não foram copiadas).
from relatorio_clientes import (
    contar_clientes,
    contar_ativos,
    contar_segmento,
    contar_ativos_segmento,
    contar_inativos,
)

# Os dados ficam no script que usa o módulo.
clientes = [
    {"nome": "mercado central", "segmento": "alimentacao", "situacao": "ativo"},
    {"nome": "oficina progresso", "segmento": "automotivo", "situacao": "ativo"},
    {"nome": "farmacia vida", "segmento": "saude", "situacao": "inativo"},
    {"nome": "padaria pao quente", "segmento": "alimentacao", "situacao": "inativo"},
]

print("Total de clientes:", contar_clientes(clientes))
print("Clientes ativos:", contar_ativos(clientes))
print("Clientes do segmento alimentacao:", contar_segmento(clientes, "alimentacao"))
print("Clientes do segmento saude:", contar_segmento(clientes, "saude"))
print("Ativos do segmento alimentacao:", contar_ativos_segmento(clientes, "alimentacao"))
print("Clientes inativos:", contar_inativos(clientes))