# ==========================
# PROJETO COMPLETO: ENGENHARIA MECÂNICA
# ==========================

from datetime import datetime

# ==========================
# 1. LISTA DE MÁQUINAS
# ==========================
maquinas = [
    ["Fresadora", "operando", 65.0, "04/11/2025"],
    ["Torno Convencional", "parada", 25.5, "02/11/2025"],
    ["Milling Machine", "operando", 60.0, "06/11/2025"],
    ["Serra de Fita", "parada", 18.0, "03/11/2025"],
    ["Torno CNC", "parada", 20.0, "01/11/2025"]
]

# ==========================
# 2. DICIONÁRIO DE HISTÓRICO DE MANUTENÇÃO
# ==========================
historico_manutencao = {
    "Fresadora": ["Troca de correia - 20/10/2025", "Lubrificação geral - 01/11/2025"],
    "Torno Convencional": ["Ajuste de folga da bucha - 15/10/2025", "Troca de óleo - 30/10/2025"],
    "Milling Machine": ["Inspeção elétrica - 22/10/2025", "Limpeza de guias - 05/11/2025"],
    "Serra de Fita": ["Troca da lâmina - 10/10/2025", "Aperto da estrutura - 01/11/2025"]
}

# ==========================
# 3. DICIONÁRIO DE CUSTOS
# ==========================
custos = {
    "troca de óleo": 120.0,
    "limpeza": 60.0,
    "troca de rolamento": 300.0
}

custos_por_maquina = {}

# ==========================
# 4. FUNÇÕES
# ==========================

# Registrar medição (STRING -> lista)
def registrar_medicao(linha):
    partes = linha.split(",")
    nome = partes[0].strip()
    temperatura = float(partes[1].strip())
    status = partes[2].strip()

    for m in maquinas:
        if m[0] == nome:
            m[1] = status
            m[2] = temperatura
            if status.lower() == "em manutenção":
                m[3] = datetime.now().strftime("%d/%m/%Y")
            break
    else:
        print(f"Máquina '{nome}' não encontrada.")

# Adicionar manutenção
def adicionar_manutencao(nome_maquina, descricao):
    # Atualiza histórico
    if nome_maquina not in historico_manutencao:
        historico_manutencao[nome_maquina] = []
    historico_manutencao[nome_maquina].append(descricao)

    # Atualiza custos
    descricao_lower = descricao.lower()
    for chave, valor in custos.items():
        if chave in descricao_lower:
            if nome_maquina not in custos_por_maquina:
                custos_por_maquina[nome_maquina] = 0.0
            custos_por_maquina[nome_maquina] += valor

# Salvar dados das máquinas em arquivo
def salvar_dados_maquinas(nome_arquivo="dados_maquinas.txt"):
    with open(nome_arquivo, "w") as arq:
        for m in maquinas:
            arq.write(f"{m[0]};{m[1]};{m[2]};{m[3]}\n")
    print(f"Dados salvos em {nome_arquivo}")

# Carregar dados das máquinas de arquivo
def carregar_dados_maquinas(nome_arquivo="dados_maquinas.txt"):
    maquinas_lidas = []
    try:
        with open(nome_arquivo, "r") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) != 4:
                    continue
                nome, status, temp, data = partes
                maquinas_lidas.append([nome, status, float(temp), data])
    except FileNotFoundError:
        print("Arquivo não encontrado. Salve primeiro.")
    return maquinas_lidas

# Gerar relatório geral
def gerar_relatorio(nome_arquivo="relatorio_final.txt"):
    if not maquinas:
        print("Nenhuma máquina cadastrada.")
        return

    maquina_quente = max(maquinas, key=lambda x: x[2])

    with open(nome_arquivo, "w") as arq:
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

# Gerar relatório de custos
def gerar_relatorio_custos(nome_arquivo="custos_manutencao.txt"):
    total_geral = sum(custos_por_maquina.values())

    with open(nome_arquivo, "w") as arq:
        arq.write("RELATÓRIO DE CUSTOS DE MANUTENÇÃO\n\n")
        for maquina, valor in custos_por_maquina.items():
            arq.write(f"- {maquina}: R$ {valor:.2f}\n")
        arq.write(f"\nTOTAL GERAL: R$ {total_geral:.2f}\n")

    print(f"Relatório de custos gerado em {nome_arquivo}")

# Mostrar relatório no terminal
def mostrar_relatorio(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arq:
            print(arq.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# ==========================
# 5. EXEMPLO DE USO
# ==========================

if __name__ == "__main__":
    # Registrar algumas medições
    registrar_medicao("Torno CNC, 78.5, operando")
    registrar_medicao("Fresadora, 70.0, em manutenção")

    # Adicionar manutenções
    adicionar_manutencao("Fresadora", "Troca de óleo - 07/11/2025")
    adicionar_manutencao("Torno Convencional", "Troca de rolamento - 09/11/2025")
    adicionar_manutencao("Milling Machine", "Limpeza - 10/11/2025")

    # Salvar dados
    salvar_dados_maquinas()

    # Gerar relatórios
    gerar_relatorio()
    gerar_relatorio_custos()

    # Mostrar relatórios
    mostrar_relatorio("relatorio_final.txt")
    mostrar_relatorio("custos_manutencao.txt")
