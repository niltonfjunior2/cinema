# 🎬 CineVision - Sistema de Controle de Ocupação de Cinema

Sistema didático e interativo desenvolvido em **Python** com interface gráfica **Tkinter / ttk**, projetado para exemplificar os conceitos fundamentais da **Programação Estruturada / Procedural** e a manipulação de matrizes bidimensionais na gestão de assentos de uma sala de cinema.

---

## 📌 Sobre o Projeto

O objetivo da aplicação é gerenciar o mapa de assentos de uma sala de cinema em tempo real. Cada cadeira é mapeada em uma matriz lógica bidimensional ($6 \times 8$), onde os estados são representados numericamente em uma interface de **Tema Claro** para melhor contraste:

- **`0`**: Cadeira Disponível (Verde Esmeralda)
- **`1`**: Cadeira Ocupada (Vermelho Vivo)

A interface gráfica sincroniza dinamicamente as ações do usuário com a matriz de dados, oferecendo visualização instantânea de métricas, cálculo de ocupação e emissão de relatório ao encerrar.

---

## 🎯 Abordagem Pedagógica e Arquitetural

Este projeto foi construído sob **estritas diretrizes acadêmicas de lógica e programação procedural**:

1. **Paradigma Procedural Puro**:
   - Desenvolvido exclusivamente através de funções (`def`), variáveis globais de estado e controle de escopo.
   - **Sem uso de Orientação a Objetos** (ausência da palavra-chave `class`).
2. **Teorema da Estruturação de Böhm-Jacopini**:
   - **Sequência**: Fluxo linear de inicialização e montagem modular da interface.
   - **Seleção (`if/else`)**: Alternância de estados e tratamento de confirmações de diálogo.
   - **Repetição (`for`)**: Varredura e sincronização bidimensional da matriz de assentos.
3. **Didática do Código**:
   - Funções nativas e atalhos de alto nível (ex.: `sum()`, `chr()`, *list comprehensions*) contam com comentários explicativos sobre o comportamento interno ("por debaixo dos panos") e o algoritmo de iteração manual equivalente.

---

## ✨ Funcionalidades

- **Mapa de Assentos Interativo ($6 \times 8$)**: 48 assentos identificados por fileiras (`A` a `F`) e números (`1` a `8`).
- **Alternância com 1 Clique**: Clique em uma cadeira livre para ocupá-la ou em uma ocupada para liberá-la.
- **Dashboard em Tempo Real**:
  - Total de cadeiras disponíveis.
  - Total de cadeiras ocupadas.
  - Taxa percentual de ocupação calculada dinamicamente.
- **Ações Rápidas**:
  - 🔄 **Liberar Todas as Cadeiras**: Reinicializa a sala com diálogo de confirmação.
  - 🚪 **Encerrar e Exibir Relatório**: Exibe o balanço final da sessão e fecha o sistema.
- **Interceptação de Fechamento**: Clicar no botão `X` da janela também aciona o relatório de encerramento.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: [Python 3.x](https://www.python.org/)
- **Interface Gráfica**: `tkinter` e `tkinter.ttk` (bibliotecas nativas do Python)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python instalado em seu computador (versão 3.8 ou superior recomendada).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/cinema.git
   cd cinema
   ```

2. **Execute o programa:**
   - No **Windows**:
     ```powershell
     py main.py
     ```
     *ou*
     ```powershell
     python main.py
     ```
   - No **Linux / macOS**:
     ```bash
     python3 main.py
     ```

---

## 📁 Estrutura de Arquivos

```text
cinema/
├── ia/
│   └── Prompt Python.md    # Especificação pedagógica e diretrizes do projeto
├── main.py                 # Código-fonte principal (procedural + Tkinter)
└── README.md               # Documentação do repositório
```

---

## 📊 Regras de Negócio Implementadas

| Cenário / Ação | Condição da Matriz | Reflexo Visual na Interface |
| :--- | :--- | :--- |
| **Inicialização** | Todas as posições recebem `0` | Todos os botões ficam verdes ("Livre") |
| **Clique em cadeira disponível** | Posição muda de `0` para `1` | Botão passa a vermelho ("Ocupada") |
| **Clique em cadeira ocupada** | Posição muda de `1` para `0` | Botão volta a verde ("Livre") |
| **Atualização de Estado** | Recálculo com base na matriz | Painel atualiza números e percentual |
| **Encerrar Sessão** | Leitura consolidada da matriz | Janela modal (`messagebox`) com relatório final |

---

## 👨‍💻 Autor

Desenvolvido para fins acadêmicos e estudo de estruturas de dados e lógica de programação procedural.
