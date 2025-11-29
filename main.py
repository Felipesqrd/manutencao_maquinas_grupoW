
from datetime import datetime

# LISTA DE MÁQUINAS
maquinas = [
    ["Fresadora", "operando", 65.0, "04/11/2025"],
    ["Torno Convencional", "parada", 25.5, "02/11/2025"],
    ["Milling Machine", "operando", 60.0, "06/11/2025"],
    ["Serra de Fita", "parada", 18.0, "03/11/2025"],
    ["Torno CNC", "parada", 20.0, "01/11/2025"]
]

# HISTÓRICO
historico_manutencao = {
    "Fresadora": ["Troca de correia - 20/10/2025", "Lubrificação geral - 01/11/2025"],
    "Torno Convencional": ["Ajuste de folga da bucha - 15/10/2025", "Troca de óleo - 30/10/2025"],
    "Milling Machine": ["Inspeção elétrica - 22/10/2025", "Limpeza de guias - 05/11/2025"],
    "Serra de Fita": ["Troca da lâmina - 10/10/2025", "Aperto da estrutura - 01/11/2025"]
}

# CUSTOS
custos = {
    "troca de óleo": 120.0,
    "limpeza": 60.0,
    "troca de rolamento": 300.0
}

custos_por_maquina = {}

# FUNÇÕES DO SISTEMA

def registrar_medicao(linha):
    partes = linha.split(",")
    if len(partes) != 3:
        print("Formato inválido. Use: nome, temperatura, status")
        return
    nome = partes[0].strip()
    try:
        temperatura = float(partes[1].strip())
    except ValueError:
        print("Temperatura inválida")
        return
    status = partes[2].strip()

    for m in maquinas:
        if m[0].lower() == nome.lower():
            m[1] = status
            m[2] = temperatura
            if status.lower() == "em manutenção":
                m[3] = datetime.now().strftime("%d/%m/%Y")
            print(f"Medição registrada para {nome}")
            return
    print(f"Máquina '{nome}' não encontrada.")

def adicionar_manutencao(nome_maquina, descricao):
    # Histórico
    if nome_maquina not in historico_manutencao:
        historico_manutencao[nome_maquina] = []
    historico_manutencao[nome_maquina].append(descricao)

    # Custos
    descricao_lower = descricao.lower()
    for chave, valor in custos.items():
        if chave in descricao_lower:
            if nome_maquina not in custos_por_maquina:
                custos_por_maquina[nome_maquina] = 0.0
            custos_por_maquina[nome_maquina] += valor

    print(f"Manutenção adicionada para {nome_maquina}")

def salvar_dados_maquinas(nome_arquivo="dados_maquinas.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        for m in maquinas:
            arq.write(f"{m[0]};{m[1]};{m[2]};{m[3]}\n")
    print(f"Dados salvos em {nome_arquivo}")

def carregar_dados_maquinas(nome_arquivo="dados_maquinas.txt"):
    maquinas_lidas = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) != 4:
                    continue
                nome, status, temp, data = partes
                maquinas_lidas.append([nome, status, float(temp), data])
        print(f"Dados carregados de {nome_arquivo}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Salve os dados primeiro.")
    return maquinas_lidas

def gerar_relatorio(nome_arquivo="relatorio_final.txt"):
    if not maquinas:
        print("Nenhuma máquina cadastrada.")
        return

    maquina_quente = max(maquinas, key=lambda x: x[2])

    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        arq.write("RELATÓRIO DE MÁQUINAS\n\n")
        arq.write(f"Máquina mais quente: {maquina_quente[0]} ({maquina_quente[2]} °C)\n\n")
        arq.write("Máquinas em manutenção ou paradas:\n")
        for m in maquinas:
            if m[1].lower() in ["em manutenção", "parada"]:
                arq.write(f"- {m[0]} (última manutenção: {m[3]})\n")

        arq.write("\nQuantidade de manutenções registradas:\n")
        for nome, eventos in historico_manutencao.items():
            arq.write(f"- {nome}: {len(eventos)} registro(s)\n")

    print(f"Relatório gerado em {nome_arquivo}")

def gerar_relatorio_custos(nome_arquivo="custos_manutencao.txt"):
    total_geral = sum(custos_por_maquina.values())

    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        arq.write("RELATÓRIO DE CUSTOS DE MANUTENÇÃO\n\n")
        for maquina, valor in custos_por_maquina.items():
            arq.write(f"- {maquina}: R$ {valor:.2f}\n")
        arq.write(f"\nTOTAL GERAL: R$ {total_geral:.2f}\n")

    print(f"Relatório de custos gerado em {nome_arquivo}")

def mostrar_relatorio(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arq:
            print(arq.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# MENU PRINCIPAL

def main():
    while True:
        print("\n=== Sistema de Manutenção de Máquinas ===")
        print("1 - Registrar medição")
        print("2 - Adicionar manutenção")
        print("3 - Salvar dados")
        print("4 - Carregar dados")
        print("5 - Gerar relatório geral")
        print("6 - Gerar relatório de custos")
        print("7 - Mostrar relatório geral")
        print("8 - Mostrar relatório de custos")
        print("9 - Sair")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            linha = input("Digite: nome, temperatura, status: ")
            registrar_medicao(linha)
        elif opc == "2":
            nome = input("Nome da máquina: ")
            desc = input("Descrição da manutenção: ")
            adicionar_manutencao(nome, desc)
        elif opc == "3":
            salvar_dados_maquinas()
        elif opc == "4":
            global maquinas
            maquinas = carregar_dados_maquinas()
        elif opc == "5":
            gerar_relatorio()
        elif opc == "6":
            gerar_relatorio_custos()
        elif opc == "7":
            mostrar_relatorio("relatorio_final.txt")
        elif opc == "8":
            mostrar_relatorio("custos_manutencao.txt")
        elif opc == "9":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# EXECUTAR O MENU
if __name__ == "__main__":
    main()
