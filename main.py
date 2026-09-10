# ==============================================================================
# SISTEMA DE CONTROLE DE OCUPAÇÃO DE CADEIRAS DE CINEMA
# Paradigma: Programação Estruturada / Procedural Pura (Sem classes)
# Interface Gráfica: Tkinter e ttk
# ==============================================================================

import tkinter as tk
from tkinter import messagebox, ttk

# ==============================================================================
# 1. CONSTANTES E VARIÁVEIS DE ESTADO GLOBAL (DADOS DO PROGRAMA)
# ==============================================================================

# Definição das dimensões da sala de cinema (Matriz 6x8)
# Estrutura: Sequência de definições de constantes globais
NUM_LINHAS = 6
NUM_COLUNAS = 8

# Convenções de estado de ocupação na matriz
CADEIRA_DISPONIVEL = 0
CADEIRA_OCUPADA = 1

# Paleta de cores para estilização visual dos botões e interface (Tema Claro)
COR_FUNDO = "#f0f4f8"        # Fundo claro suave para a janela principal
COR_PAINEL = "#ffffff"       # Fundo dos cartões e painel da sala (Branco)
COR_TEXTO = "#1e293b"        # Texto principal escuro (Slate/Grafite) para alto contraste
COR_TEXTO_SECUNDARIO = "#64748b"  # Texto secundário (Cinza médio)
COR_DISPONIVEL = "#10b981"   # Verde esmeralda (livre)
COR_OCUPADA = "#ef4444"      # Vermelho vivo (ocupado)
COR_TELA = "#2563eb"         # Azul royal para representação da tela do cinema
COR_BOTAO_SAIR = "#dc2626"   # Vermelho de ação para encerrar
COR_BOTAO_RESET = "#0284c7"  # Azul ciano para reiniciar

# Variáveis de estado global (armazenamento de dados e referências de widgets)
matriz_cadeiras = []        # Matriz bidimensional de inteiros (0 e 1)
matriz_botoes = []          # Matriz correspondente de referências aos botões da UI
label_disponiveis = None    # Referência do widget de texto para cadeiras livres
label_ocupadas = None       # Referência do widget de texto para cadeiras ocupadas
label_taxa_ocupacao = None  # Referência do widget de texto para porcentagem
janela_principal = None     # Referência da janela raiz do Tkinter


# ==============================================================================
# 2. FUNÇÕES DE PROCESSAMENTO LÓGICO E MANIPULAÇÃO DA MATRIZ
# ==============================================================================

def inicializar_matriz():
    """
    Cria e inicializa a matriz de assentos com o valor 0 (Disponível).
    
    ESTRUTURA DE BÖHM-JACOPINI: Repetição Aninhada (Loops 'for').
    - O loop externo itera pelas linhas da sala.
    - O loop interno itera pelas colunas de cada linha.
    """
    global matriz_cadeiras
    matriz_cadeiras = []
    
    # [ESTRUTURA DE REPETIÇÃO]: Percorre cada linha da matriz
    for i in range(NUM_LINHAS):
        linha = []
        # [ESTRUTURA DE REPETIÇÃO]: Percorre cada coluna da linha atual
        for j in range(NUM_COLUNAS):
            # [ESTRUTURA DE SEQUÊNCIA]: Adiciona o valor 0 (livre) à lista da linha
            linha.append(CADEIRA_DISPONIVEL)
        # [ESTRUTURA DE SEQUÊNCIA]: Adiciona a linha preenchida à matriz principal
        matriz_cadeiras.append(linha)


def calcular_estatisticas():
    """
    Calcula a contagem de cadeiras ocupadas, disponíveis e o total.
    
    EXPLICAÇÃO PEDAGÓGICA SOBRE ATALHOS E FUNÇÕES NATIVAS:
    - Abaixo utilizamos a função nativa 'sum()' combinada com compreensão de lista.
    - O QUE FAZ 'POR DEBAIXO DOS PANOS':
      A função sum() itera sequencialmente sobre a coleção gerada, mantendo um 
      acumulador numérico interno inicializado em zero e somando elemento por elemento
      (acumulador += item).
    - ALGORITMO TRADICIONAL EQUIVALENTE SUBSTITUÍDO:
      total_ocupadas = 0
      for linha in matriz_cadeiras:
          for assento in linha:
              if assento == 1:
                  total_ocupadas += 1
    """
    # Total de cadeiras = multiplicação simples de linhas por colunas
    total_cadeiras = NUM_LINHAS * NUM_COLUNAS
    
    # Usa sum() para totalizar os valores 1 da matriz (acumulação manual simplificada)
    total_ocupadas = sum(sum(linha) for linha in matriz_cadeiras)
    
    # Cálculo por subtração aritmética direta
    total_disponiveis = total_cadeiras - total_ocupadas
    
    # [ESTRUTURA DE SELEÇÃO]: Evita divisão por zero caso as dimensões sejam zeradas
    if total_cadeiras > 0:
        percentual = (total_ocupadas / total_cadeiras) * 100.0
    else:
        percentual = 0.0
        
    return total_ocupadas, total_disponiveis, total_cadeiras, percentual


def alternar_ocupacao(linha, coluna):
    """
    Alterna o estado de uma cadeira específica entre 0 (Disponível) e 1 (Ocupada).
    
    ESTRUTURA DE BÖHM-JACOPINI: Seleção Simples (if/else).
    - Se a cadeira for 0 (livre), ela se torna 1 (ocupada).
    - Se a cadeira for 1 (ocupada), ela se torna 0 (livre).
    """
    global matriz_cadeiras
    
    # [ESTRUTURA DE SELEÇÃO]: Decisão baseada no valor atual da célula da matriz
    if matriz_cadeiras[linha][coluna] == CADEIRA_DISPONIVEL:
        # [ESTRUTURA DE SEQUÊNCIA]: Atualiza a matriz para ocupado
        matriz_cadeiras[linha][coluna] = CADEIRA_OCUPADA
    else:
        # [ESTRUTURA DE SEQUÊNCIA]: Atualiza a matriz para disponível
        matriz_cadeiras[linha][coluna] = CADEIRA_DISPONIVEL
        
    # [ESTRUTURA DE SEQUÊNCIA]: Dispara a atualização visual da interface
    atualizar_interface_grafica()


def resetar_todas_cadeiras():
    """
    Redefine todos os assentos da sala para o estado 0 (Disponível) com confirmação.
    """
    # [ESTRUTURA DE SELEÇÃO]: Diálogo de confirmação para ação destrutiva
    resposta = messagebox.askyesno(
        "Reiniciar Sala", 
        "Deseja realmente liberar todas as cadeiras da sala?",
        parent=janela_principal
    )
    
    if resposta:
        # [ESTRUTURA DE REPETIÇÃO]: Itera por todas as células da matriz
        for i in range(NUM_LINHAS):
            for j in range(NUM_COLUNAS):
                matriz_cadeiras[i][j] = CADEIRA_DISPONIVEL
        
        # [ESTRUTURA DE SEQUÊNCIA]: Atualiza os componentes da UI
        atualizar_interface_grafica()
        messagebox.showinfo("Sucesso", "Todas as cadeiras foram liberadas!", parent=janela_principal)


# ==============================================================================
# 3. ATUALIZAÇÃO DOS ELEMENTOS GRÁFICOS (UI EM TEMPO REAL)
# ==============================================================================

def atualizar_interface_grafica():
    """
    Sincroniza o estado da matriz de dados com os componentes visuais da tela.
    
    ESTRUTURA DE BÖHM-JACOPINI:
    - Repetição: Percorre a matriz de botões para aplicar cores e textos corretos.
    - Seleção: Aplica estilo verde/vermelho dependendo se o valor é 0 ou 1.
    - Sequência: Atualiza os rótulos de contadores estatísticos em tempo real.
    """
    # [ESTRUTURA DE REPETIÇÃO]: Percorre cada posição de botão correspondente à matriz
    for i in range(NUM_LINHAS):
        for j in range(NUM_COLUNAS):
            valor = matriz_cadeiras[i][j]
            botao = matriz_botoes[i][j]
            
            # Identificador do assento (ex: A1, B4, C6)
            # EXPLICAÇÃO PEDAGÓGICA: 'chr(65 + i)' converte o índice numérico para caractere ASCII
            # 65 = 'A', 66 = 'B', 67 = 'C', etc. Substitui uma tabela de mapeamento estática.
            codigo_assento = f"{chr(65 + i)}{j + 1}"
            
            # [ESTRUTURA DE SELEÇÃO]: Define o visual conforme o estado na matriz
            if valor == CADEIRA_DISPONIVEL:
                botao.config(
                    text=f"{codigo_assento}\nLivre",
                    bg=COR_DISPONIVEL,
                    fg="#ffffff",
                    activebackground="#26af74",
                    relief="raised"
                )
            else:
                botao.config(
                    text=f"{codigo_assento}\nOcupada",
                    bg=COR_OCUPADA,
                    fg="#ffffff",
                    activebackground="#d42d4e",
                    relief="sunken"
                )
                
    # [ESTRUTURA DE SEQUÊNCIA]: Obtém as estatísticas atualizadas
    ocupadas, disponiveis, total, percentual = calcular_estatisticas()
    
    # Atualiza o texto dos cartões informativos na interface
    label_disponiveis.config(text=f"{disponiveis}")
    label_ocupadas.config(text=f"{ocupadas}")
    label_taxa_ocupacao.config(text=f"{percentual:.1f}%")


def encerrar_sistema():
    """
    Apresenta o relatório final com o total de cadeiras ocupadas e disponíveis,
    e finaliza o programa após a confirmação do usuário.
    """
    ocupadas, disponiveis, total, percentual = calcular_estatisticas()
    
    mensagem = (
        "====================================\n"
        "      RELATÓRIO DE OCUPAÇÃO DA SALA\n"
        "====================================\n\n"
        f"• Total de Cadeiras na Sala: {total}\n"
        f"• Cadeiras Ocupadas: {ocupadas} ({percentual:.1f}%)\n"
        f"• Cadeiras Disponíveis: {disponiveis} ({100 - percentual:.1f}%)\n\n"
        "Deseja encerrar o sistema agora?"
    )
    
    # [ESTRUTURA DE SELEÇÃO]: Pergunta se o usuário deseja fechar
    confirmacao = messagebox.askyesno(
        "Resumo Final da Sessão", 
        mensagem,
        parent=janela_principal
    )
    
    if confirmacao:
        # [ESTRUTURA DE SEQUÊNCIA]: Destrói a janela e finaliza a execução
        janela_principal.destroy()


# ==============================================================================
# 4. CONSTRUÇÃO DA INTERFACE GRÁFICA (LAYOUT E WIDGETS)
# ==============================================================================

def criar_interface():
    """
    Constrói todos os elementos da interface visual utilizando Tkinter e ttk.
    Utiliza o gerenciador de geometria 'grid' e 'pack' de forma organizada e modular.
    """
    global janela_principal, matriz_botoes
    global label_disponiveis, label_ocupadas, label_taxa_ocupacao
    
    # 1. Janela Principal
    janela_principal = tk.Tk()
    janela_principal.title("CineVision - Controle de Ocupação da Sala")
    janela_principal.geometry("900x720")
    janela_principal.minsize(800, 650)
    janela_principal.configure(bg=COR_FUNDO)
    
    # 2. Configuração do Estilo ttk
    estilo = ttk.Style()
    estilo.theme_use("clam")
    
    # Estilo geral para rótulos e frames ttk
    estilo.configure("TFrame", background=COR_FUNDO)
    estilo.configure("Card.TFrame", background=COR_PAINEL, relief="flat")
    estilo.configure("Titulo.TLabel", background=COR_FUNDO, foreground=COR_TEXTO, font=("Segoe UI", 18, "bold"))
    estilo.configure("Subtitulo.TLabel", background=COR_FUNDO, foreground=COR_TEXTO_SECUNDARIO, font=("Segoe UI", 10))
    estilo.configure("CardNum.TLabel", background=COR_PAINEL, foreground=COR_TEXTO, font=("Segoe UI", 20, "bold"))
    estilo.configure("CardTit.TLabel", background=COR_PAINEL, foreground=COR_TEXTO_SECUNDARIO, font=("Segoe UI", 9))
    
    # --- CABEÇALHO ---
    frame_cabecalho = ttk.Frame(janela_principal, padding=(20, 15, 20, 10))
    frame_cabecalho.pack(fill="x")
    
    label_titulo = ttk.Label(frame_cabecalho, text="🎬 Sistema de Ocupação de Cadeiras - Cinema", style="Titulo.TLabel")
    label_titulo.pack(anchor="center")
    
    label_sub = ttk.Label(
        frame_cabecalho, 
        text="Clique em uma cadeira para alternar seu estado (Disponível ↔ Ocupada)", 
        style="Subtitulo.TLabel"
    )
    label_sub.pack(anchor="center", pady=(3, 0))
    
    # --- PAINEL DE ESTATÍSTICAS (DASHBOARD EM TEMPO REAL) ---
    frame_dashboard = ttk.Frame(janela_principal, padding=(20, 5, 20, 15))
    frame_dashboard.pack(fill="x")
    
    # Grid interno do dashboard (3 colunas iguais)
    frame_dashboard.columnconfigure(0, weight=1)
    frame_dashboard.columnconfigure(1, weight=1)
    frame_dashboard.columnconfigure(2, weight=1)
    
    # Cartão 1: Disponíveis
    card_disp = ttk.Frame(frame_dashboard, style="Card.TFrame", padding=10)
    card_disp.grid(row=0, column=0, padx=8, sticky="nsew")
    ttk.Label(card_disp, text="CADEIRAS DISPONÍVEIS", style="CardTit.TLabel").pack()
    label_disponiveis = ttk.Label(card_disp, text="0", style="CardNum.TLabel", foreground=COR_DISPONIVEL)
    label_disponiveis.pack(pady=(4, 0))
    
    # Cartão 2: Ocupadas
    card_ocup = ttk.Frame(frame_dashboard, style="Card.TFrame", padding=10)
    card_ocup.grid(row=0, column=1, padx=8, sticky="nsew")
    ttk.Label(card_ocup, text="CADEIRAS OCUPADAS", style="CardTit.TLabel").pack()
    label_ocupadas = ttk.Label(card_ocup, text="0", style="CardNum.TLabel", foreground=COR_OCUPADA)
    label_ocupadas.pack(pady=(4, 0))
    
    # Cartão 3: Taxa de Ocupação
    card_taxa = ttk.Frame(frame_dashboard, style="Card.TFrame", padding=10)
    card_taxa.grid(row=0, column=2, padx=8, sticky="nsew")
    ttk.Label(card_taxa, text="TAXA DE OCUPAÇÃO", style="CardTit.TLabel").pack()
    label_taxa_ocupacao = ttk.Label(card_taxa, text="0.0%", style="CardNum.TLabel", foreground=COR_TEXTO)
    label_taxa_ocupacao.pack(pady=(4, 0))
    
    # --- ÁREA CENTRAL: SALA DE CINEMA E GRID DE ASSENTOS ---
    frame_sala = tk.Frame(janela_principal, bg=COR_PAINEL, bd=0, highlightthickness=1, highlightbackground="#3d405b")
    frame_sala.pack(fill="both", expand=True, padx=25, pady=5)
    
    # Simulação da Tela do Cinema
    label_tela = tk.Label(
        frame_sala, 
        text="══════════════════════  TELA DE PROJEÇÃO  ══════════════════════",
        font=("Segoe UI", 10, "bold"),
        bg="#1e1e2f",
        fg=COR_TELA,
        pady=6
    )
    label_tela.pack(fill="x", padx=40, pady=(15, 20))
    
    # Container para o grid de botões
    frame_grid_assentos = tk.Frame(frame_sala, bg=COR_PAINEL)
    frame_grid_assentos.pack(expand=True, pady=(0, 15))
    
    # [ESTRUTURA DE REPETIÇÃO]: Criação dos botões representando a matriz
    matriz_botoes = []
    
    for i in range(NUM_LINHAS):
        linha_botoes = []
        letra_linha = chr(65 + i)  # Letras A, B, C, D, E, F
        
        # Rótulo indicador da fileira à esquerda
        lbl_fileira_esq = tk.Label(
            frame_grid_assentos, 
            text=letra_linha, 
            font=("Segoe UI", 11, "bold"),
            bg=COR_PAINEL, 
            fg=COR_TEXTO_SECUNDARIO,
            width=2
        )
        lbl_fileira_esq.grid(row=i, column=0, padx=(0, 8), pady=4)
        
        for j in range(NUM_COLUNAS):
            # Função de fechamento léxico (closure) com valores padrão para fixar 'i' e 'j'
            # EXPLICAÇÃO PEDAGÓGICA: 'lambda l=i, c=j: alternar_ocupacao(l, c)' cria uma função anônima
            # que captura o valor exato dos índices naquele momento do loop.
            botao_assento = tk.Button(
                frame_grid_assentos,
                font=("Segoe UI", 9, "bold"),
                width=7,
                height=2,
                cursor="hand2",
                bd=1,
                command=lambda l=i, c=j: alternar_ocupacao(l, c)
            )
            botao_assento.grid(row=i, column=j + 1, padx=4, pady=4)
            linha_botoes.append(botao_assento)
            
        # Rótulo indicador da fileira à direita
        lbl_fileira_dir = tk.Label(
            frame_grid_assentos, 
            text=letra_linha, 
            font=("Segoe UI", 11, "bold"),
            bg=COR_PAINEL, 
            fg=COR_TEXTO_SECUNDARIO,
            width=2
        )
        lbl_fileira_dir.grid(row=i, column=NUM_COLUNAS + 1, padx=(8, 0), pady=4)
        
        matriz_botoes.append(linha_botoes)
        
    # --- LEGENDA DE CORES ---
    frame_legenda = tk.Frame(frame_sala, bg=COR_PAINEL)
    frame_legenda.pack(pady=(0, 10))
    
    # Amostra Disponível
    canvas_livre = tk.Canvas(frame_legenda, width=14, height=14, bg=COR_DISPONIVEL, highlightthickness=0)
    canvas_livre.pack(side="left", padx=(0, 4))
    tk.Label(frame_legenda, text="Disponível (0)", font=("Segoe UI", 9), bg=COR_PAINEL, fg=COR_TEXTO).pack(side="left", padx=(0, 20))
    
    # Amostra Ocupada
    canvas_ocupado = tk.Canvas(frame_legenda, width=14, height=14, bg=COR_OCUPADA, highlightthickness=0)
    canvas_ocupado.pack(side="left", padx=(0, 4))
    tk.Label(frame_legenda, text="Ocupada (1)", font=("Segoe UI", 9), bg=COR_PAINEL, fg=COR_TEXTO).pack(side="left")
    
    # --- RODAPÉ E BOTÕES DE AÇÃO ---
    frame_rodape = ttk.Frame(janela_principal, padding=(25, 10, 25, 15))
    frame_rodape.pack(fill="x")
    
    # Botão para Reiniciar Sala
    btn_reset = tk.Button(
        frame_rodape,
        text="🔄 Liberar Todas as Cadeiras",
        font=("Segoe UI", 10, "bold"),
        bg=COR_PAINEL,
        fg=COR_BOTAO_RESET,
        activebackground="#32354a",
        activeforeground=COR_BOTAO_RESET,
        bd=1,
        padx=15,
        pady=8,
        cursor="hand2",
        command=resetar_todas_cadeiras
    )
    btn_reset.pack(side="left")
    
    # Botão para Encerrar Sessão
    btn_encerrar = tk.Button(
        frame_rodape,
        text="🚪 Encerrar e Exibir Relatório",
        font=("Segoe UI", 10, "bold"),
        bg=COR_BOTAO_SAIR,
        fg="#ffffff",
        activebackground="#e04e2b",
        activeforeground="#ffffff",
        bd=0,
        padx=20,
        pady=8,
        cursor="hand2",
        command=encerrar_sistema
    )
    btn_encerrar.pack(side="right")
    
    # Intercepta o evento de clique no 'X' da janela para exibir o relatório
    janela_principal.protocol("WM_DELETE_WINDOW", encerrar_sistema)


# ==============================================================================
# 5. FLUXO DE EXECUÇÃO PRINCIPAL (PONTO DE ENTRADA PROCEDURAL)
# ==============================================================================

def main():
    """
    Função controladora principal do fluxo do programa.
    
    ESTRUTURA DE BÖHM-JACOPINI: Sequência linear de inicialização e controle.
    1. Inicializa os dados em memória (Matriz de zeros).
    2. Constrói a interface visual.
    3. Atualiza o estado inicial dos componentes gráficos.
    4. Inicia o loop de eventos da interface.
    """
    # 1. Sequência: Inicialização da matriz com valor 0
    inicializar_matriz()
    
    # 2. Sequência: Construção da janela e widgets
    criar_interface()
    
    # 3. Sequência: Aplicação do estado inicial na interface gráfica
    atualizar_interface_grafica()
    
    # 4. Sequência: Início do loop de escuta de eventos do Tkinter
    janela_principal.mainloop()


# Execução do programa quando chamado diretamente
if __name__ == "__main__":
    main()
