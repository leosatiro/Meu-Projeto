import csv
import os

culturas = []  # Lista para armazenar culturas

# ---------- Funções de Cálculo ----------
def area_retangulo(comprimento, largura):
    return comprimento * largura

def area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area(cultura):
    if cultura["forma_area"] == "retangulo":
        return area_retangulo(cultura["comprimento"], cultura["largura"])
    else:
        return area_triangulo(cultura["base"], cultura["altura"])

def calcular_insumos(cultura):
    area_total = calcular_area(cultura)
    print(f"\nÁrea total da cultura {cultura['nome']}: {area_total} m²")
    for insumo in cultura["insumos"]:
        quantidade_total = insumo["quantidade_por_metro"] * area_total * cultura["ruas"]
        print(f"{insumo['produto']}: {quantidade_total} {insumo['unidade']}")

# ---------- Função Entrada de Dados ----------
def entrada_dados():
    while True:
        print("\nEscolha a cultura (ou digite 'menu' para retornar ao menu principal):")
        print("1. Milho")
        print("2. Feijão")
        escolha_cultura = input("Digite 1 ou 2: ").strip().lower()
        if escolha_cultura == "menu":
            return
        if escolha_cultura == "1":
            nome = "Milho"
        elif escolha_cultura == "2":
            nome = "Feijão"
        else:
            print("Opção inválida! Digite novamente.")
            continue

        # Escolha da forma
        while True:
            print("\nEscolha a forma da área (ou digite 'voltar' para escolher a cultura novamente):")
            print("0 - Retângulo")
            print("1 - Triângulo")
            forma_input = input("Digite 0 ou 1: ").strip().lower()
            if forma_input == "voltar":
                break
            if forma_input not in ["0", "1"]:
                print("Opção inválida! Digite novamente.")
                continue

            if forma_input == "0":
                forma = "retangulo"
                # Comprimento
                while True:
                    comprimento = input("Comprimento (m) ou 'voltar': ").strip().lower()
                    if comprimento == "voltar":
                        break
                    try:
                        comprimento = float(comprimento)
                        if comprimento > 0:
                            break
                        else:
                            print("Digite um valor maior que zero.")
                    except ValueError:
                        print("Digite um valor numérico válido.")
                if comprimento == "voltar":
                    continue

                # Largura
                while True:
                    largura = input("Largura (m) ou 'voltar': ").strip().lower()
                    if largura == "voltar":
                        break
                    try:
                        largura = float(largura)
                        if largura > 0:
                            break
                        else:
                            print("Digite um valor maior que zero.")
                    except ValueError:
                        print("Digite um valor numérico válido.")
                if largura == "voltar":
                    continue

                cultura = {"nome": nome, "forma_area": forma, "comprimento": comprimento, "largura": largura}
                break

            elif forma_input == "1":
                forma = "triangulo"
                while True:
                    base = input("Base (m) ou 'voltar': ").strip().lower()
                    if base == "voltar":
                        break
                    try:
                        base = float(base)
                        if base > 0:
                            break
                        else:
                            print("Digite um valor maior que zero.")
                    except ValueError:
                        print("Digite um valor numérico válido.")
                if base == "voltar":
                    continue

                while True:
                    altura = input("Altura (m) ou 'voltar': ").strip().lower()
                    if altura == "voltar":
                        break
                    try:
                        altura = float(altura)
                        if altura > 0:
                            break
                        else:
                            print("Digite um valor maior que zero.")
                    except ValueError:
                        print("Digite um número válido.")
                if altura == "voltar":
                    continue

                cultura = {"nome": nome, "forma_area": forma, "base": base, "altura": altura}
                break
        else:
            continue

        # Número de ruas
        while True:
            ruas = input("Número de ruas ou 'voltar': ").strip().lower()
            if ruas == "voltar":
                return entrada_dados()
            try:
                ruas = int(ruas)
                if ruas > 0:
                    cultura["ruas"] = ruas
                    break
                else:
                    print("Digite um valor maior que zero.")
            except ValueError:
                print("Digite um número válido.")

        # Insumos
        insumos = []
        while True:
            produto = input("Nome do insumo (ou 'fim' para terminar / 'voltar'): ").strip()
            if produto.lower() == "fim":
                break
            if produto.lower() == "voltar":
                return entrada_dados()

            while True:
                quantidade = input(f"Quantidade por metro de {produto} ou 'voltar': ").strip().lower()
                if quantidade == "voltar":
                    break
                try:
                    quantidade = float(quantidade)
                    if quantidade > 0:
                        break
                    else:
                        print("Digite um valor maior que zero.")
                except ValueError:
                    print("Digite um número válido.")
            if quantidade == "voltar":
                continue

            while True:
                print("Escolha a unidade do insumo:")
                print("0 - Unidade")
                print("1 - KG")
                print("2 - Litros")
                unidade_input = input("Digite 0,1,2 ou 'voltar': ").strip().lower()
                if unidade_input == "voltar":
                    break
                if unidade_input == "0":
                    unidade = "Unidade"
                    break
                elif unidade_input == "1":
                    unidade = "KG"
                    break
                elif unidade_input == "2":
                    unidade = "Litros"
                    break
                else:
                    print("Opção inválida!")
            if unidade_input == "voltar":
                continue

            insumos.append({"produto": produto, "quantidade_por_metro": quantidade, "unidade": unidade})

        cultura["insumos"] = insumos
        culturas.append(cultura)
        print(f"\nCultura {nome} adicionada com sucesso!")
        return

# ---------- Função Saída ----------
def saida_dados():
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return
    for i, cultura in enumerate(culturas):
        print(f"\nCultura {i}: {cultura['nome']}")
        print(f"Forma: {cultura['forma_area']}")
        print(f"Ruas: {cultura['ruas']}")
        print("Insumos:")
        for j, insumo in enumerate(cultura["insumos"]):
            print(f"[{j}] {insumo['produto']} - {insumo['quantidade_por_metro']} {insumo['unidade']}")
        calcular_insumos(cultura)

# ---------- Função Atualização ----------
def atualizar_dados():
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return
    saida_dados()

    while True:
        idx = input("Índice da cultura para atualizar ou 'menu': ").strip().lower()
        if idx == "menu":
            return
        try:
            idx = int(idx)
            if 0 <= idx < len(culturas):
                cultura = culturas[idx]
                break
            else:
                print("Índice inválido!")
        except ValueError:
            print("Digite um número válido!")

    while True:
        print("O que deseja atualizar?")
        print("0 - Cultura")
        print("1 - Insumos")
        opcao = input("Digite 0 ou 1 (ou 'voltar'): ").strip().lower()
        if opcao == "voltar":
            return atualizar_dados()
        if opcao == "0":
            print("Atualize os dados da cultura selecionada:")
            entrada_dados()
            culturas[idx] = culturas.pop(-1)  # Substitui a cultura antiga
            return
        elif opcao == "1":
            if not cultura["insumos"]:
                print("Não há insumos.")
                return
            print("Insumos:")
            for j, insumo in enumerate(cultura["insumos"]):
                print(f"[{j}] {insumo['produto']} - {insumo['quantidade_por_metro']} {insumo['unidade']}")
            while True:
                insumo_idx = input("Índice do insumo ou 'voltar': ").strip().lower()
                if insumo_idx == "voltar":
                    return atualizar_dados()
                try:
                    insumo_idx = int(insumo_idx)
                    if 0 <= insumo_idx < len(cultura["insumos"]):
                        break
                    else:
                        print("Índice inválido!")
                except ValueError:
                    print("Digite um número válido!")

            produto = input("Novo nome do insumo (ou 'voltar'): ").strip()
            if produto.lower() == "voltar":
                return atualizar_dados()

            while True:
                quantidade = input(f"Nova quantidade por metro de {produto} ou 'voltar': ").strip().lower()
                if quantidade == "voltar":
                    return atualizar_dados()
                try:
                    quantidade = float(quantidade)
                    if quantidade > 0:
                        break
                    else:
                        print("Digite um valor maior que zero.")
                except ValueError:
                    print("Digite um número válido.")

            while True:
                print("Escolha unidade:")
                print("0 - Unidade")
                print("1 - KG")
                print("2 - Litros")
                unidade_input = input("Digite 0,1,2 ou 'voltar': ").strip().lower()
                if unidade_input == "voltar":
                    return atualizar_dados()
                if unidade_input == "0":
                    unidade = "Unidade"
                    break
                elif unidade_input == "1":
                    unidade = "KG"
                    break
                elif unidade_input == "2":
                    unidade = "Litros"
                    break
                else:
                    print("Opção inválida!")

            cultura["insumos"][insumo_idx] = {"produto": produto, "quantidade_por_metro": quantidade, "unidade": unidade}
            print("Insumo atualizado!")
            return
        else:
            print("Opção inválida!")

# ---------- Função Deletar ----------
def deletar_dados():
    if not culturas:
        print("Nenhuma cultura cadastrada.")
        return
    saida_dados()
    while True:
        idx = input("Índice da cultura para deletar ou 'menu': ").strip().lower()
        if idx == "menu":
            return
        try:
            idx = int(idx)
            if 0 <= idx < len(culturas):
                confirm = input(f"Confirmar exclusão de {culturas[idx]['nome']}? (s/n): ").strip().lower()
                if confirm == "s":
                    culturas.pop(idx)
                    print("Cultura excluída!")
                return
            else:
                print("Índice inválido!")
        except ValueError:
            print("Digite um número válido!")

# ---------- Função Exportar CSV Detalhado ----------
def exportar_csv_detalhado():
    if not culturas:
        print("Nenhuma cultura para exportar.")
        return

    # Pasta 'data' dentro do diretório atual
    pasta = os.path.join(os.getcwd(), "data")
    os.makedirs(pasta, exist_ok=True)

    arquivo = os.path.join(pasta, "culturas_detalhado.csv")

    try:
        with open(arquivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Nome_Cultura", "Forma", "Ruas", "Insumo",
                "Quantidade_por_metro", "Unidade",
                "Comprimento", "Largura", "Base", "Altura", "Area_total", "Quantidade_total"
            ])

            for c in culturas:
                area_total = calcular_area(c)
                for insumo in c["insumos"]:
                    quantidade_total = insumo["quantidade_por_metro"] * area_total * c["ruas"]
                    writer.writerow([
                        c["nome"], c["forma_area"], c["ruas"], insumo["produto"],
                        insumo["quantidade_por_metro"], insumo["unidade"],
                        c.get("comprimento", ""), c.get("largura", ""),
                        c.get("base", ""), c.get("altura", ""),
                        area_total, quantidade_total
                    ])
        print(f"Exportação detalhada concluída! Arquivo criado em: {arquivo}")
    except Exception as e:
        print(f"Erro ao exportar CSV detalhado: {e}")

# ---------- Menu Principal ----------
def menu():
    while True:
        print("\n=== Menu Agricultura Digital ===")
        print("1. Entrada de dados")
        print("2. Saída de dados")
        print("3. Atualizar dados")
        print("4. Deletar dados")
        print("5. Exportar CSV Detalhado")
        print("6. Sair")
        escolha = input("Escolha uma opção: ").strip().lower()

        if escolha == "1":
            entrada_dados()
        elif escolha == "2":
            saida_dados()
        elif escolha == "3":
            atualizar_dados()
        elif escolha == "4":
            deletar_dados()
        elif escolha == "5":
            exportar_csv_detalhado()
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
