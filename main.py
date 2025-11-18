# --- DADOS INICIAIS (A Base) ---
maquinas = [
    ["Torno CNC", "operando", 72.5, "05/11/2025"],
    ["Prensa Hidráulica", "parada", 30.0, "01/11/2025"],
    ["Compressor de Ar", "operando", 45.0, "04/11/2025"],
    ["Retífica", "operando", 60.0, "02/11/2025"]
]

historico = {
    "Torno CNC": ["Troca de óleo - 01/11/2025", "Limpeza - 03/11/2025"],
    "Prensa Hidráulica": ["Troca de mangueira - 02/11/2025"]
}

# --- FUNÇÕES ---

# Função 1: Adicionar Manutenção
def adicionar_manutencao(nome_maquina, descricao):
    if nome_maquina not in historico:
        historico[nome_maquina] = []
    historico[nome_maquina].append(descricao)
    print(f"--> Sucesso: Manutenção registrada para '{nome_maquina}'")

# --- TESTE RÁPIDO ---
if __name__ == "__main__":
    print("--- Iniciando Sistema de Manutenção ---")
    
    # Testando a função
    adicionar_manutencao("Compressor de Ar", "Troca de filtro - HOJE")
    
    # Mostrando como ficou o histórico
    print("\nHistórico atualizado:")
    print(historico)
def registrar_medicao(linha):
    partes = linha.split(",")
    nome = partes[0].strip()
    temperatura = float(partes[1].strip())
    status = partes[2].strip()

    for m in maquinas:
        if m[0] == nome:
            m[1] = status
            m[2] = temperatura
            # desafio: se status for "em manutenção", atualizar data
            break

registrar_medicao("Torno CNC, 78.5, operando")
maquinas
