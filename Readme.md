 #Simulador de Autômatos Finitos

Um autômato finito tem um conjunto de estados, alguns dos quais são denominados estados finais. À medida que caracteres da string de entrada são lidos, o controle da máquina passa de um estado a outro, segundo um conjunto de regras de transição especificadas para o autômato. Se após o último caractere o autômato encontra-se em um dos estados finais, a string foi reconhecida (ou seja, pertence à linguagem). Caso contrário, a string não pertence à linguagem aceita pelo autômato.

## Funcionalidades

- **Definição de Autômatos**: Permite a criação e configuração de autômatos finitos determinísticos (AFD) com estados, alfabeto, transições, estado inicial e estados finais.
- **Simulação de Cadeias**: Permite simular a execução do autômato sobre uma cadeia de entrada para verificar se é aceita ou rejeitada.
- **Visualização Gráfica**: Gera diagramas de estados dos autômatos para uma melhor compreensão e visualização.
- **Minimização de Autômatos**: Implementa algoritmos para minimizar o número de estados de um AFD mantendo a linguagem reconhecida.
- **Conversão de AFND para AFD**: Converte autômatos finitos não determinísticos (AFND) em autômatos finitos determinísticos (AFD).
- **Exportação e Importação**: Permite salvar autômatos em arquivos para posterior importação e reutilização.
- **Interface Interativa**: Interface de linha de comando (CLI) amigável para facilitar a interação com o simulador.

## Execução do programa

    É necessário dois arquivos para o programa funcionar: `ex1.json` e `testes.csv`.

### ex1.json

        {
        "initial": 0,
        "final" : [2],
        "transitions": [
            {
            "from": "0",
            "to": "0",
            "read": "a"
            },
            {
            "from": "2",
            "to": "2",
            "read": "a"
            },
            {
            "from": "1",
            "to": "1",
            "read": "b"
            },
            {
            "from": "1",
            "to": "2",
            "read": "a"
            },
            {
            "from": "0",
            "to": "1",
            "read": "b"
            }
        ]
        }

### testes.csv

        ba;1
        aaaabbbbbaaaaa;1
        abababab;0
        bbbbbbbb;0
        aaaaaaaaaaaa;0
        aaaaabaaaaa;1

### Arquivo de Resultados (resultados.csv)

    O programa gera esse arquivo:

        aa;1;0;0.00001520
        ab;1;0;0.00000690
        ba;1;0;0.00000420
        bb;0;0;0.00000330
        aaa;0;0;0.00000500
        bbb;0;0;0.00000390
