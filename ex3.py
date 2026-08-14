estoque = [
   {"nome": "Arroz", "qtd": 12, "preco": 24.90},
   {"nome": "Sal", "qtd": 3, "preco": 2.30},
   { "nome": "Café", "qtd": 40, "preco": 19.50},
]

print("--- REPOSIÇÃO ---")
for p in sorted (estoque, key=lambda p: p["qtd"]):
    print(f"{p['nome'): <8} {p['qtd']: >3} un")

