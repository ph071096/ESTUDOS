import cowsay

tarefas = [] # Dicionario de tarefas

# Funções
def adicionar_tarefa(nome: str, categoria: str, descricao: str, prioridade: int): # Função para add a tarefa
    nova_tarefa = {
        'nome': nome,
        'descricao': descricao,
        'categoria': categoria,
        'prioridade': prioridade,
        'realizado': False
    }
    tarefas.append(nova_tarefa) # Salvando a nova tarefa no final da lista
    print(f'Tarefa: {nome} adicionada com sucesso!')

def input_adicionar_tarefa(): # Função do input das infos das tarefas
    nome = input('Nome: ')
    categoria = input('Categoria: ')
    descricao = input('Descrição: ')
    prioridade = int(input('Prioridade: '))
    adicionar_tarefa(nome, categoria, descricao, prioridade)

def listar_tarefas(): # Função para listar as tarefas
    for task in tarefas:
        print(f'Nome: {task["nome"]}')
        print(f'Descrição: {task["descricao"]}')
        print(f'Categoria: {task["categoria"]}')
        print(f'Prioridade: {task["prioridade"]}')
        print(f'Realizado: {task["realizado"]}')
        print('-'*100)

def listar_prioridade(prioridade: int): # Função para listar as tarefas por ondem de prioridade
    if len(tarefas) == 0:
        print('A lista está vazia.')
        return
    for task in tarefas:
        if task['prioridade'] == prioridade:
            print(f'Nome: {task["nome"]}')
            print(f'Descrição: {task["descricao"]}')
            print(f'Categoria: {task["categoria"]}')
            print(f'Prioridade: {task["prioridade"]}')
            print(f'Realizado: {task["realizado"]}')
            print('-'*100)

def input_listar_prioridade():
    prioridade = int(input('Informe a prioridade que deseja buscar: '))
    listar_prioridade(prioridade)

def concluir_tarefa(nome: str): # Função para alterar o status de realizado
    if len(tarefas) == 0:
        print('A lista de tarefas está vazia.')
        return
    for task in tarefas:
        if task["nome"].lower() == nome.lower():
            task["realizado"] = True
            print('Sua tarefa foi concluída.')
            return
    print('Tarefa não encontrada!')

def input_concluir_tarefa(): # Função do input para concluir a tarefa digitada via nome
    nome = input('Digite o nome da tarefa: ')
    concluir_tarefa(nome)

def menu(): # Função: Menu da aplicação
    while True:
        print('---- WELCOME ----')
        print('1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Listar tarefas por prioridade')
        print('4 - Concluir tarefa')
        print('0 - Sair')
        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            input_adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            input_listar_prioridade()
        elif opcao == '4':
            input_concluir_tarefa()
        elif opcao == '0':
            print('Exiting...')
            break

# Comandos
menu()
cowsay.tux(tarefas)