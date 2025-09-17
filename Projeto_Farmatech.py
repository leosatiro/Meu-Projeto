# ===============================
# App Agricultura Digital - FarmTech
# ===============================

import csv

culturas = []  # Lista para armazenar todas as culturas

# ---------- Funções de Cálculo ----------
def area_retangulo(comprimento, largura):
    return comprimento * largura

def area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_insumos(cultura):
    # Calcula área
    if cultura["forma_area"] == "retangulo":
        area_total = area_retangulo(cultura["comprimento"], cultura["largura"])
    elif cultura["forma_area"] == "triangulo":
        area_total = area_triangulo(cultura["base"], cultura["altura"])
    else:
        area_total = 0

    print(f"\nÁrea total da cultura {cultura['nome']}: {area_total} m²")
    
    # Calcula insumos
    for insumo in cultura["insumos"]:
        quantidade_total = insumo["quantidade_por_metro"] * area_total * cultura["ruas"]
        print(f"{insumo['produto']}: {quantidade_total} {insumo['unidade']}")

# ---------- Funções de Menu ----------
def entrada_dados():
    nome = input("Nome da cultura: ")
    forma = input("Forma da área (retangulo/triangulo): ").lower()
    
    if forma == "retangulo":
        comprimento = float(input("Comprimento (m): "))
        largura = float(input("Largura (m): "))
        cultura = {
            "nome": nome,
            "forma_area": forma,
            "comprimento": comprimento,
            "largura": largura
        }
    elif forma == "triangulo":
        base = float(input("Base (m): "))
        altura = float(input("Altura (m): "))
        cultura = {
            "nome": nome,
            "forma_area": forma,
            "base": base,
            "altura": altura
        }
    else:
        print("Forma inválida!")
        return
    
    cultura["ruas"] = int(input("Número de ruas na lavoura: "))
    
    # Entrada de insumos
    insumos = []
    while True:
        produto = input("Nome do insumo (ou 'fim' para terminar): ")
        if produto.lower() == "fim":
            break
        quantidade = float(input(f"Quantidade por metro de {produto}: "))
        unidade = input("Unidade (ex: L, kg): ")
        insumos.append({
            "produto": produto,
            "quantidade_por_metro": quantidade,
            "unidade": unidade
        })
    cultura["insumos"] = insumos
    
    culturas.append(cultura)
    print("Cultura adicionada com sucesso!")

def saida_dados():
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return
    for i, cultura in enumerate(culturas):
        print(f"\nCultura {i}: {cultura['nome']}")
        print(f"Forma da área: {cultura['forma_area']}")
        print(f"Ruas: {cultura['ruas']}")
        print("Insumos:")
        for insumo in cultura["insumos"]:
            print(f" - {insumo['produto']} : {insumo['quantidade_por_metro']} {insumo['unidade']}")
        calcular_insumos(cultura)

def atualizar_dados():
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return
    saida_dados()
    idx = int(input("Digite o índice da cultura que deseja atualizar: "))
    if idx < 0 or idx >= len(culturas):
        print("Índice inválido!")
        return
    entrada_dados()  # Adiciona nova entrada
    culturas[idx] = culturas.pop()  # Substitui a cultura antiga

def deletar_dados():
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return
    saida_dados()
    idx = int(input("Digite o índice da cultura que deseja deletar: "))
    if idx < 0 or idx >= len(culturas):
        print("Índice inválido!")
        return
    culturas.pop(idx)
    print("Cultura deletada com sucesso!")

def exportar_csv():
    if not culturas:
        print("Nenhuma cultura para exportar.")
        return
    
    with open("culturas.csv", mode="w", newline="") as arquivo:
        campos = ["nome", "forma_area", "comprimento", "largura", "base", "altura", "ruas", "insumo_produto", "insumo_quantidade", "insumo_unidade"]
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        writer.writeheader()
        
        for cultura in culturas:
            for insumo in cultura["insumos"]:
                writer.writerow({
                    "nome": cultura.get("nome", ""),
                    "forma_area": cultura.get("forma_area", ""),
                    "comprimento": cultura.get("comprimento", ""),
                    "largura": cultura.get("largura", ""),
                    "base": cultura.get("base", ""),
                    "altura": cultura.get("altura", ""),
                    "ruas": cultura.get("ruas", ""),
                    "insumo_produto": insumo.get("produto", ""),
                    "insumo_quantidade": insumo.get("quantidade_por_metro", ""),
                    "insumo_unidade": insumo.get("unidade", "")
                })
    print("Dados exportados para culturas.csv com sucesso!")

# ---------- Menu Principal ----------
def menu():
    while True:
        print("\n=== Menu Agricultura Digital ===")
        print("1. Entrada de dados")
        print("2. Saída de dados")
        print("3. Atualizar dados")
        print("4. Deletar dados")
        print("5. Exportar dados para CSV")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            entrada_dados()
        elif escolha == "2":
            saida_dados()
        elif escolha == "3":
            atualizar_dados()
        elif escolha == "4":
            deletar_dados()
        elif escolha == "5":
            exportar_csv()
        elif escolha == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

# ---------- Execução ----------
menu()
