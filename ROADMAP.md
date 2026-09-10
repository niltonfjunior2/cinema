# 🗺️ Roadmap de Desenvolvimento - CineVision

Documento de rastreamento do ciclo de vida, marcos implementados, decisões de engenharia e planejamento de futuras versões do **CineVision**.

---

## 📌 Visão Geral do Produto

O **CineVision** nasceu como uma aplicação educacional para demonstrar o controle de estado e a manipulação de matrizes bidimensionais no paradigma procedural puro utilizando Python e Tkinter. O roadmap a seguir delineia a transição de um protótipo didático para um sistema de gestão de bilheteria mais completo.

---

## 🚀 Status do Projeto

```text
[v1.0.0] - Concluído ✅  -->  [v1.1.0] - Planejado ⏳  -->  [v2.0.0] - Futuro 🔮
```

---

## 📅 Histórico de Versões e Entregas

### ✅ Versão 1.0.0 — Fundação Procedural e Mapa de Assentos (Concluída)
*Foco: Atendimento estrito às restrições pedagógicas e regras de negócio essenciais.*

- [x] **Arquitetura & Paradigma**:
  - [x] Implementação estrita em **Paradigma Procedural** (sem criação de classes).
  - [x] Estruturação do fluxo baseada no Teorema de Böhm-Jacopini (Sequência, Seleção e Repetição).
  - [x] Inclusão de comentários didáticos detalhando o funcionamento de métodos nativos/atalhos (`sum()`, `chr()`, etc.).
- [x] **Modelo de Dados**:
  - [x] Matriz bidimensional de assentos ($6 \times 8 = 48$ lugares).
  - [x] Representação binária de estado (`0 = Disponível`, `1 = Ocupada`).
- [x] **Interface Gráfica (Tkinter / ttk)**:
  - [x] Grid interativo de botões coloridos (`#2dce89` verde para livre, `#f5365c` vermelho para ocupado).
  - [x] Identificação de fileiras (`A` a `F`) e colunas (`1` a `8`).
  - [x] Indicador visual da tela de projeção do cinema.
  - [x] Dashboard em tempo real com contadores (Disponíveis, Ocupadas e % de Ocupação).
- [x] **Regras de Negócio e Ações**:
  - [x] Alternância de estado do assento via clique único ($0 \leftrightarrow 1$).
  - [x] Botão de reset com confirmação para liberar todas as cadeiras.
  - [x] Encerramento da sessão com relatório final via `messagebox` (incluindo interceptação do botão 'X' da janela).
- [x] **Documentação**:
  - [x] `README.md` completo para apresentação no GitHub.
  - [x] `ROADMAP.md` para governança e planejamento.

---

## 🔮 Planejamento de Próximas Versões

### ⏳ Versão 1.1.0 — Gestão Financeira e Tipos de Ingresso (Próxima Etapa)
*Foco: Adicionar cálculo financeiro sem quebrar o paradigma procedural.*

- [ ] **Diferenciação de Ingressos**:
  - [ ] Opção de selecionar entre **Inteira** e **Meia-Entrada** ao ocupar uma cadeira.
  - [ ] Representação de valores adicionais na matriz ou matrizes paralelas (ex: `0`: Livre, `1`: Inteira, `2`: Meia).
- [ ] **Métricas Financeiras**:
  - [ ] Definição de valor base do ingresso (ex.: R$ 30,00 inteira / R$ 15,00 meia).
  - [ ] Exibição da receita bruta acumulada no dashboard em tempo real.
- [ ] **Melhorias de Usabilidade**:
  - [ ] Tooltip ou legenda com o valor arrecadado por fileira.
  - [ ] Atalhos de teclado (ex.: `Ctrl + R` para resetar, `Esc` para encerrar).

---

### ⏳ Versão 1.2.0 — Persistência e Exportação de Relatórios
*Foco: Armazenamento do histórico de sessões e geração de arquivos.*

- [ ] **Persistência de Dados**:
  - [ ] Salvar o estado da sala em arquivos locais (`JSON` ou `CSV`).
  - [ ] Função para carregar uma sessão previamente salva.
- [ ] **Exportação de Relatórios**:
  - [ ] Geração de arquivo `.txt` ou `.csv` contendo o resumo da sessão ao encerrar.
  - [ ] Registro de log de auditoria (horário em que cada cadeira foi ocupada/liberada).

---

### 🔮 Versão 2.0.0 — Múltiplas Sessões e Customização de Sala
*Foco: Escalabilidade e parametrização do cinema.*

- [ ] **Suporte a Múltiplas Sessões/Filmes**:
  - [ ] Seletor de filmes em cartaz e horários de exibição com matrizes independentes.
- [ ] **Configurador de Sala**:
  - [ ] Modal inicial para o usuário definir a quantidade customizada de linhas e colunas antes de abrir a sala.
  - [ ] Marcação de assentos especiais (Cadeirantes, Obesos, VIP).
- [ ] **Módulo Opcional de Orientação a Objetos (Refatoração Didática)**:
  - [ ] Branch comparativo demonstrando como a mesma aplicação ficaria estruturada sob o paradigma de POO (`class Sala`, `class Assento`, `class Sessao`).

---

## 🛠️ Critérios de Aceite para Novas Contribuições

1. Todo código novo deve manter conformidade com a convenção **PEP 8**.
2. Funções devem manter responsabilidade única e documentação clara (*docstrings* e comentários pedagógicos).
3. Qualquer alteração em estruturas de controle deve manter compatibilidade com o fluxo de eventos do Tkinter sem bloquear a thread principal.
