# BStorage

Sistema de Gestão de Estoques simples e eficiente para controle de empréstimos de itens.

## Descrição

BStorage é um sistema de gerenciamento de estoques desenvolvido em Python que permite controlar empréstimos e devoluções de itens, registrando automaticamente datas e horários das operações. O sistema armazena os dados em arquivos de texto, tornando-o leve e fácil de usar.

## Funcionalidades

- Registro de empréstimos com:
  - Nome do item
  - Nome da pessoa
  - Data e hora automática do empréstimo
- Registro de devoluções com:
  - Seleção do item a ser devolvido
  - Data e hora automática da devolução
- Visualização dos últimos 5 itens emprestados
- Visualização dos últimos 5 itens devolvidos
- Interface de linha de comando intuitiva

## Estrutura de Arquivos

- `main.py`: Arquivo principal do programa
- `emprestados.txt`: Armazena os itens atualmente emprestados
- `devolvidos.txt`: Armazena o histórico de itens devolvidos

## Formato dos Dados

### Arquivo emprestados.txt
Cada linha contém: `"item";"pessoa";"data_emprestimo"`

### Arquivo devolvidos.txt
Cada linha contém: `"item";"pessoa";"data_emprestimo";"data_devolucao"`

## Como Usar

1. Execute o arquivo `main.py`
2. Escolha uma das opções:
   - 0: Sair do programa
   - 1: Registrar novo empréstimo
   - 2: Registrar nova devolução

## Histórico de Versões

### Versão alfa 0.0.2 (Atual)
- Implementado método para separar linhas dos arquivos em listas
- Melhorada a visualização dos dados com formatação em tabela

### Versão alfa 0.0.1
- Implementação inicial com salvamento em arquivos de texto
- Registro automático de datas de empréstimo e devolução
- Funcionalidades básicas de empréstimo e devolução