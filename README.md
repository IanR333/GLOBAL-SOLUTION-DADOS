# Explicação da Lógica — Mission Control AI
## GS2026.1 — Data Structures and Algorithms | FIAP

**Integrantes:**
- Ian Rodrigues Martins — RM: 570540
- Patrick Fernandes Martins — RM: 572899
- Gabriel Del Pizzo Pintor — RM: 570436

**Linguagem:** Python 3

---

## 1. Estruturas de Dados Utilizadas

### Lista (vetor) — `historico`
```python
historico = []
```
A variável `historico` é uma **lista Python** que funciona como vetor dinâmico.
Cada leitura de sensores é um dicionário (registro) com 6 campos, e é
adicionada ao vetor com `historico.append(leitura)`.

Exemplo de um registro salvo:
```python
{
    "timestamp"   : "09/06/2026 14:32:01",
    "temperatura" : 92.4,
    "energia"     : 17.3,
    "comunicacao" : 0,
    "origem"      : "simulado"
}
```

---

## 2. Estruturas Condicionais

Usadas na função `verificar_alertas()` para analisar cada parâmetro:

```python
if dados["temperatura"] > 80:
    # alerta crítico
elif dados["temperatura"] > 60:
    # atenção

if dados["energia"] < 20:
    # alerta crítico
elif dados["energia"] < 40:
    # atenção

if dados["comunicacao"] == 0:
    # falha de comunicação
```

Cada condição gera uma mensagem de alerta com cor correspondente:
- 🔴 Vermelho = crítico
- 🟡 Amarelo = atenção
- ✅ Verde = normal

---

## 3. Laços de Repetição

### Loop principal do menu (while)
```python
while True:
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        break   # encerra o sistema
    # executa a função correspondente
```
O sistema continua rodando até o usuário escolher a opção 0.

### Loop de análise do histórico (for)
```python
for leitura in historico:
    temp_media += leitura["temperatura"]
    # acumula estatísticas...
```
Percorre todo o vetor `historico` para calcular médias e contagens.

### Loop de simulação contínua (for com range)
```python
for ciclo in range(1, 6):
    dados = simular_dados()
    exibir_status(dados)
    time.sleep(2)
```
Executa 5 ciclos automaticamente com pausa de 2 segundos entre cada leitura.

---

## 4. Funções Implementadas

| Função | Responsabilidade |
|---|---|
| `inserir_dados()` | Lê dados digitados pelo usuário e salva no histórico |
| `simular_dados()` | Gera valores aleatórios e salva no histórico |
| `verificar_alertas(leitura)` | Aplica as condições e retorna lista de alertas |
| `tomada_de_decisao(dados)` | Define ações automáticas para parâmetros críticos |
| `exibir_status(leitura)` | Imprime o painel formatado no terminal |
| `visualizar_status()` | Exibe a leitura mais recente do histórico |
| `executar_analise()` | Percorre o histórico e calcula estatísticas gerais |
| `ver_historico()` | Lista todas as leituras registradas com cores |
| `simulacao_continua()` | Executa 5 leituras automáticas em sequência |
| `menu()` | Loop principal com todas as opções do sistema |

---

## 5. Decisões de Projeto

**Cores no terminal:** Usamos códigos ANSI (`\033[91m` etc.) encapsulados
na classe `Cor`, o que facilita reutilização e manutenção sem bibliotecas externas.

**Separação de responsabilidades:** Cada função faz apenas uma coisa.
`verificar_alertas()` só analisa — não imprime. `exibir_status()` só imprime
— não analisa. Isso facilita testar e reutilizar cada parte.

**Vetor de histórico global:** A lista `historico` é compartilhada entre
todas as funções, permitindo que análises e o histórico reflitam todas as
leituras feitas na sessão, independente de como foram geradas (manual ou simulado).

---

## 6. Como Executar

```bash
python mission_control.py
```

Requer Python 3.6+. Sem dependências externas.
