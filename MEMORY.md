# 🧠 MEMORY.md - Memória de Trabalho e Contexto Arquitetural

Este arquivo serve como **registro de contexto durável e base de conhecimento** para agentes de IA e desenvolvedores continuarem o desenvolvimento deste projeto sem perda de contexto ou desvio das premissas arquiteturais.

---

## 🏛️ 1. Identidade e Propósito do Projeto

- **Nome do Projeto**: CineVision (Controle de Ocupação de Cadeiras de Cinema)
- **Natureza**: Acadêmica / Didática (Foco no ensino de Lógica de Programação e Estruturas de Dados Básicas).
- **Domínio**: Gestão em tempo real da ocupação de assentos em uma sala de cinema.

---

## 📐 2. Diretrizes Inegociáveis (Restrições Pedagógicas)

Qualquer agente de IA que atuar neste repositório **DEVE** respeitar as seguintes regras:

1. **Paradigma Procedural Puro**:
   - **É terminantemente PROIBIDO o uso da palavra-chave `class`** ou a criação de instâncias de classes personalizadas.
   - Toda a lógica de negócio, interface e controle de estado deve ser implementada via **funções (`def`)**, variáveis globais ou parâmetros.
2. **Estruturas de Böhm-Jacopini**:
   - O fluxo do código deve evidenciar didaticamente:
     - **Sequência**: Passos de inicialização e montagem linear.
     - **Seleção**: Estruturas condicionais (`if` / `elif` / `else`).
     - **Repetição**: Laços de iteração (`for` / `while`).
3. **Didática de Funções Nativas e Atalhos**:
   - É permitido o uso de utilitários embutidos de Python (ex.: `sum()`, `max()`, `min()`, `chr()`, *list comprehensions*).
   - **OBRIGATÓRIO**: Todo atalho utilizado deve ser precedido ou acompanhado de um comentário explicando o que ocorre "por debaixo dos panos" e qual algoritmo tradicional (ex: loop de acumulação) ele substitui.

---

## 🧩 3. Modelo de Dados e Estrutura de Estado

### 3.1. Dimensões da Sala
```python
NUM_LINHAS = 6   # Fileiras identificadas de A até F via chr(65 + i)
NUM_COLUNAS = 8  # Colunas numeradas de 1 até 8
# Total: 48 assentos
```

### 3.2. Representação de Estado (Convenção Numérica)
- `CADEIRA_DISPONIVEL = 0` (Estado inicial padrão)
- `CADEIRA_OCUPADA = 1`

### 3.3. Principais Variáveis Globais de Estado
- `matriz_cadeiras`: Lista de listas (matriz bidimensional `6x8`) contendo apenas inteiros (`0` ou `1`).
- `matriz_botoes`: Matriz espelho contendo as instâncias de `tk.Button` para manipulação de estilos e textos.
- `label_disponiveis`, `label_ocupadas`, `label_taxa_ocupacao`: Referências aos widgets de texto do dashboard.
- `janela_principal`: Objeto raiz `tk.Tk()`.

---

## 🎨 4. Design System e Interface Gráfica

- **Frameworks**: `tkinter` + `tkinter.ttk` (com tema `clam`).
- **Paleta de Cores (Tema Claro)**:
  - Fundo geral: `#f0f4f8` (Light Blue/Grey)
  - Fundo dos painéis/cartões: `#ffffff` (Branco)
  - Texto Principal: `#1e293b` (Slate/Grafite)
  - Assento Disponível: `#10b981` (Verde esmeralda)
  - Assento Ocupado: `#ef4444` (Vermelho vivo)
  - Destaque/Tela: `#2563eb` (Azul Royal)
  - Botão Encerrar: `#dc2626` (Vermelho)
  - Botão Reset: `#0284c7` (Azul Ciano)

---

## 🔄 5. Mapeamento de Funções do `main.py`

| Função | Responsabilidade | Dependências / Efeitos |
| :--- | :--- | :--- |
| `inicializar_matriz()` | Cria a matriz $6 \times 8$ preenchida com zeros (`0`). | Modifica a global `matriz_cadeiras`. |
| `calcular_estatisticas()` | Retorna `(ocupadas, disponiveis, total, percentual)`. | Usa `sum()` iterativo na matriz. |
| `alternar_ocupacao(l, c)` | Inverte o valor de `matriz_cadeiras[l][c]` entre $0$ e $1$. | Dispara `atualizar_interface_grafica()`. |
| `resetar_todas_cadeiras()` | Zera todas as posições da matriz após confirmação do usuário. | Exibe `messagebox.askyesno`. |
| `atualizar_interface_grafica()` | Sincroniza cores, textos e números dos widgets com a matriz. | Atualiza botões e cartões da UI. |
| `encerrar_sistema()` | Exibe relatório consolidado via `messagebox` e finaliza a janela. | Acionado pelo botão e pelo evento `WM_DELETE_WINDOW`. |
| `criar_interface()` | Instancia toda a árvore de widgets da janela principal. | Define layout com `pack` e `grid`. |
| `main()` | Ponto de entrada procedural que orquestra o fluxo de inicialização. | Inicia `janela_principal.mainloop()`. |

---

## ⚠️ 6. Armadilhas Conhecidas e Cuidados para Próximos Agentes

1. **Captura de variáveis em funções anônimas (Closures no loop do Tkinter)**:
   - Ao vincular o clique de cada botão com `lambda`, **sempre utilize parâmetros padrão** para fixar as variáveis no escopo léxico:
     ```python
     command=lambda l=i, c=j: alternar_ocupacao(l, c)
     ```
   - Não passar `lambda: alternar_ocupacao(i, j)` diretamente, pois isso causa o problema de escopo tardio (*late binding*), fazendo todos os botões clicarem na última coordenada do loop.
2. **Não introduzir classes nem POO**:
   - Mesmo em expansões complexas (ex.: adicionar persistência de arquivos ou cálculo de ingressos), mantenha o código orientado a funções e módulos.
3. **Compatibilidade do Launcher Windows**:
   - Em ambientes Windows com aliases de execução do Python, utilize o launcher `py main.py` ou especifique o caminho completo do executável.

---

## 📚 7. Relação de Arquivos do Projeto

- `main.py`: Código-fonte funcional da aplicação.
- `README.md`: Documentação pública de apresentação do repositório.
- `ROADMAP.md`: Planejamento de releases e novas funcionalidades.
- `MEMORY.md`: Este documento de contexto para desenvolvimento contínuo.
- `ia/Prompt Python.md`: Prompt de especificação original do projeto.
