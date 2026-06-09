import random
import time
from datetime import datetime

# ─────────────────────────────────────────────
# CORES NO TERMINAL
# ─────────────────────────────────────────────
class Cor:
    VERMELHO  = "\033[91m"
    AMARELO   = "\033[93m"
    VERDE     = "\033[92m"
    CIANO     = "\033[96m"
    BRANCO    = "\033[97m"
    NEGRITO   = "\033[1m"
    RESET     = "\033[0m"

# ─────────────────────────────────────────────
# HISTÓRICO DE LEITURAS
# ─────────────────────────────────────────────
historico = []  # lista (vetor) que armazena todas as leituras

# ─────────────────────────────────────────────
# FUNÇÕES DO SISTEMA
# ─────────────────────────────────────────────

def cabecalho():
    print(f"\n{Cor.CIANO}{Cor.NEGRITO}{'═' * 50}")
    print("   🚀 MISSION CONTROL — NAVE FIAP-1")
    print(f"{'═' * 50}{Cor.RESET}")


def inserir_dados():
    """Permite ao usuário digitar os dados manualmente."""
    print(f"\n{Cor.CIANO}{'─' * 50}")
    print("  📥 INSERIR DADOS DOS SENSORES")
    print(f"{'─' * 50}{Cor.RESET}")

    try:
        temperatura  = float(input("  🌡️  Temperatura (°C): "))
        energia      = float(input("  ⚡  Energia (%): "))
        comunicacao  = int(input("  📡  Comunicação (1 = ok / 0 = falha): "))

        leitura = {
            "timestamp"   : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "temperatura" : temperatura,
            "energia"     : energia,
            "comunicacao" : comunicacao,
            "origem"      : "manual"
        }

        historico.append(leitura)
        print(f"\n{Cor.VERDE}  ✅ Dados registrados com sucesso!{Cor.RESET}")

    except ValueError:
        print(f"\n{Cor.VERMELHO}  ❌ Entrada inválida. Tente novamente.{Cor.RESET}")


def simular_dados():
    """Gera uma leitura automática com valores aleatórios."""
    leitura = {
        "timestamp"   : datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "temperatura" : round(random.uniform(10, 120), 1),
        "energia"     : round(random.uniform(5, 100), 1),
        "comunicacao" : random.choice([0, 1, 1, 1]),
        "origem"      : "simulado"
    }
    historico.append(leitura)
    return leitura


def verificar_alertas(leitura):
    """
    Analisa os dados e retorna lista de alertas.
    Estrutura condicional para cada parâmetro.
    """
    alertas = []

    # Condição 1: Temperatura
    if leitura["temperatura"] > 80:
        alertas.append((Cor.VERMELHO, "🔴 ALERTA: Superaquecimento — temperatura acima de 80°C!"))
    elif leitura["temperatura"] > 60:
        alertas.append((Cor.AMARELO, "🟡 ATENÇÃO: Temperatura elevada."))

    # Condição 2: Energia
    if leitura["energia"] < 20:
        alertas.append((Cor.VERMELHO, "🔴 ALERTA: Energia crítica — modo de economia ativado!"))
    elif leitura["energia"] < 40:
        alertas.append((Cor.AMARELO, "🟡 ATENÇÃO: Nível de energia baixo."))

    # Condição 3: Comunicação
    if leitura["comunicacao"] == 0:
        alertas.append((Cor.VERMELHO, "🔴 ALERTA: Falha de comunicação detectada!"))

    if not alertas:
        alertas.append((Cor.VERDE, "✅ Todos os sistemas operando normalmente."))

    return alertas


def exibir_status(leitura):
    """Exibe o painel de status de uma leitura."""
    alertas = verificar_alertas(leitura)

    print(f"\n{Cor.CIANO}{'─' * 50}{Cor.RESET}")
    print(f"  🛰️  {leitura['timestamp']}  |  origem: {leitura['origem']}")
    print(f"{Cor.CIANO}{'─' * 50}{Cor.RESET}")
    print(f"  🌡️  Temperatura  : {leitura['temperatura']}°C")
    print(f"  ⚡  Energia      : {leitura['energia']}%")
    com_texto = "✅ ok" if leitura["comunicacao"] == 1 else "❌ falha"
    print(f"  📡  Comunicação  : {com_texto}")

    print(f"\n  ⚠️  STATUS:")
    for cor, msg in alertas:
        print(f"  {cor}{msg}{Cor.RESET}")


def visualizar_status():
    """Mostra o status da leitura mais recente."""
    print(f"\n{Cor.CIANO}{'─' * 50}")
    print("  📊 STATUS ATUAL")
    print(f"{'─' * 50}{Cor.RESET}")

    if not historico:
        print(f"  {Cor.AMARELO}Nenhuma leitura registrada ainda.{Cor.RESET}")
        return

    exibir_status(historico[-1])


def executar_analise():
    """Analisa todas as leituras do histórico e exibe um resumo."""
    print(f"\n{Cor.CIANO}{'─' * 50}")
    print("  🔍 ANÁLISE COMPLETA DO HISTÓRICO")
    print(f"{'─' * 50}{Cor.RESET}")

    if not historico:
        print(f"  {Cor.AMARELO}Nenhuma leitura para analisar.{Cor.RESET}")
        return

    total = len(historico)

    # Usa laço de repetição para percorrer o vetor de leituras
    temp_media  = sum(l["temperatura"] for l in historico) / total
    energia_media = sum(l["energia"] for l in historico) / total
    falhas_com  = sum(1 for l in historico if l["comunicacao"] == 0)
    alertas_temp = sum(1 for l in historico if l["temperatura"] > 80)
    alertas_energia = sum(1 for l in historico if l["energia"] < 20)

    print(f"\n  📈 Total de leituras   : {total}")
    print(f"  🌡️  Temp. média         : {round(temp_media, 1)}°C")
    print(f"  ⚡  Energia média       : {round(energia_media, 1)}%")
    print(f"  📡  Falhas de comunicação: {falhas_com}")
    print(f"  🔴  Alertas de temp.    : {alertas_temp}")
    print(f"  🔴  Alertas de energia  : {alertas_energia}")

    # Avaliação geral
    print(f"\n  📋 AVALIAÇÃO GERAL:")
    if alertas_temp > total * 0.5:
        print(f"  {Cor.VERMELHO}⚠️  Superaquecimento frequente — verificar sistema de resfriamento.{Cor.RESET}")
    if alertas_energia > total * 0.5:
        print(f"  {Cor.VERMELHO}⚠️  Energia crítica recorrente — verificar painéis solares.{Cor.RESET}")
    if falhas_com > 0:
        print(f"  {Cor.AMARELO}⚠️  {falhas_com} falha(s) de comunicação registrada(s).{Cor.RESET}")
    if alertas_temp == 0 and alertas_energia == 0 and falhas_com == 0:
        print(f"  {Cor.VERDE}✅ Missão operando dentro dos parâmetros normais.{Cor.RESET}")


def ver_historico():
    """Exibe todas as leituras registradas."""
    print(f"\n{Cor.CIANO}{'─' * 50}")
    print("  📜 HISTÓRICO DE LEITURAS")
    print(f"{'─' * 50}{Cor.RESET}")

    if not historico:
        print(f"  {Cor.AMARELO}Histórico vazio.{Cor.RESET}")
        return

    # Laço de repetição percorrendo o vetor histórico
    for i, leitura in enumerate(historico, 1):
        com_texto = "ok" if leitura["comunicacao"] == 1 else "FALHA"
        temp_cor  = Cor.VERMELHO if leitura["temperatura"] > 80 else (Cor.AMARELO if leitura["temperatura"] > 60 else Cor.VERDE)
        en_cor    = Cor.VERMELHO if leitura["energia"] < 20 else (Cor.AMARELO if leitura["energia"] < 40 else Cor.VERDE)

        print(f"\n  [{i}] {leitura['timestamp']} ({leitura['origem']})")
        print(f"       Temp: {temp_cor}{leitura['temperatura']}°C{Cor.RESET} | "
              f"Energia: {en_cor}{leitura['energia']}%{Cor.RESET} | "
              f"Comm: {com_texto}")


def simulacao_continua():
    """Executa 5 leituras automáticas em sequência, simulando monitoramento real."""
    print(f"\n{Cor.CIANO}{'─' * 50}")
    print("  🔄 SIMULAÇÃO CONTÍNUA — 5 ciclos")
    print(f"{'─' * 50}{Cor.RESET}")

    for i in range(1, 6):
        print(f"\n  {Cor.NEGRITO}▶ Ciclo {i}/5{Cor.RESET}")
        leitura = simular_dados()
        exibir_status(leitura)
        if i < 5:
            print(f"  {Cor.CIANO}⏳ Próxima leitura em 2 segundos...{Cor.RESET}")
            time.sleep(2)

    print(f"\n{Cor.VERDE}  ✅ Simulação concluída.{Cor.RESET}")


# ─────────────────────────────────────────────
# MENU PRINCIPAL
# ─────────────────────────────────────────────

def menu():
    while True:
        cabecalho()
        print(f"\n{Cor.BRANCO}  1 → Inserir dados manualmente")
        print("  2 → Simular leitura dos sensores")
        print("  3 → Visualizar status atual")
        print("  4 → Executar análise do histórico")
        print("  5 → Ver histórico de leituras")
        print("  6 → Simulação contínua (5 ciclos)")
        print(f"  0 → Encerrar sistema{Cor.RESET}")

        opcao = input(f"\n{Cor.CIANO}  Escolha uma opção: {Cor.RESET}").strip()

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            leitura = simular_dados()
            print(f"\n{Cor.VERDE}  ✅ Leitura simulada gerada!{Cor.RESET}")
            exibir_status(leitura)
        elif opcao == "3":
            visualizar_status()
        elif opcao == "4":
            executar_analise()
        elif opcao == "5":
            ver_historico()
        elif opcao == "6":
            simulacao_continua()
        elif opcao == "0":
            print(f"\n{Cor.CIANO}  🚀 Encerrando Mission Control. Até a próxima missão!{Cor.RESET}\n")
            break
        else:
            print(f"\n{Cor.AMARELO}  ⚠️  Opção inválida. Tente novamente.{Cor.RESET}")

        input(f"\n{Cor.CIANO}  Pressione Enter para continuar...{Cor.RESET}")


# ─────────────────────────────────────────────
# INICIALIZAÇÃO
# ─────────────────────────────────────────────
if __name__ == "__main__":
    menu()
