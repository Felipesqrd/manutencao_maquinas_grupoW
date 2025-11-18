# --- 1. DADOS DAS MÁQUINAS (Sua lista personalizada) ---
maquinas = [
    ["Fresadora", "operando", 65.0, "04/11/2025"],
    ["Torno Convencional", "parada", 25.5, "02/11/2025"],
    ["Milling Machine", "operando", 60.0, "06/11/2025"],
    ["Serra de Fita", "parada", 18.0, "03/11/2025"]
]

# --- 2. HISTÓRICO DE MANUTENÇÃO ---
# Precisamos criar o dicionário 'historico' vazio para começar.
# A função 'adicionar_manutencao' vai preencher isso automaticamente.
historico = {} 

# --- 3. FUNÇÕES DO SISTEMA ---

def adicionar_manutencao(nome_maquina, descricao):
    """
    Adiciona uma nova manutenção ao histórico da máquina.
    Se a máquina não tiver histórico, cria uma nova lista para ela.
    """
    if nome_maquina not in historico:
        historico[nome_maquina] = []
    
    historico[nome_maquina].append(descricao)
    print(f"--> [SUCESSO] Manutenção registrada para '{nome_maquina}': {descricao}")

# --- 4. EXECUÇÃO PRINCIPAL (TESTES) ---
if __name__ == "__main__":
    print("\n--- INICIANDO SISTEMA DE MANUTENÇÃO ---\n")

    # Passo A: Mostrar as máquinas (O código que você pediu)
    print("ESTADO ATUAL DAS MÁQUINAS:")
    for m in maquinas:
        print("Nome:", m[0], "| Status:", m[1], "| Temp:", m[2], "| Última:", m[3])
    
    print("-" * 50)

    # Passo B: Testar a função de adicionar manutenção
    print("\nTESTANDO ADIÇÃO DE MANUTENÇÃO...")
    adicionar_manutencao("Fresadora", "Troca de fluido refrigerante - HOJE")
    adicionar_manutencao("Serra de Fita", "Ajuste de tensão da lâmina - HOJE")

    # Passo C: Mostrar o histórico para ver se guardou
    print("\nHISTÓRICO DO SISTEMA:")
    print(historico)
# (Célula 5)
def registrar_medicao(linha):
    """
    Processa uma linha de texto (nome, temp, status) e atualiza 
    os dados na lista 'maquinas'.
    """
    global maquinas # Indicamos que vamos modificar a lista global 'maquinas'
    
    try:
        # 1. Quebra a linha em partes e remove espaços
        partes = linha.split(",")
        nome = partes[0].strip()
        temperatura = float(partes[1].strip())
        status = partes[2].strip()
    except IndexError:
        print(f"--> [ERRO] Formato de linha incorreto: {linha}")
        return

    # 2. Procura a máquina na lista e atualiza
    encontrada = False
    for i, m in enumerate(maquinas):
        if m[0] == nome:
            maquinas[i][1] = status       # Atualiza Status
            maquinas[i][2] = temperatura  # Atualiza Temperatura
            encontrada = True
            
            # ⚠️ DESAFIO (Para o futuro):
            # O professor pediu: se status for "em manutenção", atualizar a data da última manutenção.
            # if status == "em manutenção":
            #    maquinas[i][3] = DATA_DE_HOJE
            
            print(f"--> [SUCESSO] Dados de '{nome}' atualizados para Status: {status}, Temp: {temperatura}")
            break
            
    if not encontrada:
        print(f"--> [AVISO] Máquina '{nome}' não encontrada no cadastro.")
