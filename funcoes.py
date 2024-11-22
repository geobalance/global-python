import os

# Lista que vai armazenar as configurações do ambiente
configuracao_ambiente = []


# Função para limpar o console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para configurar um ambiente
def configurar_ambiente():
    cls()
    print("Configure o ambiente que será utilizado para os cálculos")
    
    # Entrada de valores do ambiente com validação
    while True:
        try:      
                 
            # Altura
            while True:
                try:
                    altura = float(input("\nAltura em metros: "))
                    if altura <= 0:
                        print("\nErro: a altura deve ser um valor positivo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("\nErro: valor inválido. Por favor, insira um número válido para a altura.")
            
            # Comprimento
            while True:
                try:
                    comprimento = float(input("Comprimento em metros: "))
                    if comprimento <= 0:
                        print("\nErro: o comprimento deve ser um valor positivo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("\nErro: valor inválido. Por favor, insira um número válido para o comprimento.")
            
            areaMQ = altura * comprimento # Definindo a área em m²

            # Quantidade de pessoas
            while True:
                try:
                    qtdPessoas = int(input("\nQuantidade média de pessoas que habitam: "))
                    if qtdPessoas < 0:
                        print("\nErro: a quantidade de pessoas não pode ser negativa. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("\nErro: valor inválido. Por favor, insira um número válido para a quantidade de pessoas.")
            
            # Quantidade de eletrônicos
            while True:
                try:
                    qtdEletronicos = int(input("Quantidade média de eletrônicos: "))
                    if qtdEletronicos < 0:
                        print("\nErro: a quantidade de eletrônicos não pode ser negativa. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("\nErro: valor inválido. Por favor, insira um número válido para a quantidade de eletrônicos.")
            
            # Incidência do sol            
            while True:
                exposicaoAoSol = input("O ambiente tem alta exposição de luz solar? (S/N): ").strip().lower()
                if exposicaoAoSol not in ['s', 'n']:
                    print("\nErro: insira 'S' para sim ou 'N' para não.")
                else:
                    break

            # Cálculo do BTU ideal
            if areaMQ < 10:
                btuIdeal = 5000
            elif 10 <= areaMQ < 15:
                btuIdeal = 7000
            elif 15 <= areaMQ < 20:
                btuIdeal = 9000
            elif 20 <= areaMQ < 25:
                btuIdeal = 12000
            elif 25 <= areaMQ < 30:
                btuIdeal = 14000
            elif 30 <= areaMQ < 35:
                btuIdeal = 16000
            elif 35 <= areaMQ < 40:
                btuIdeal = 18000
            elif 40 <= areaMQ < 45:
                btuIdeal = 20000
            else:
                btuIdeal = 22000

            btuIdeal += (qtdPessoas * 600) # Adicionando 600 BTU para cada pessoa no ambiente
            btuIdeal += (qtdEletronicos * 200) # Adicionando 200 BTU para cada eletrônico no ambiente

            # Caso haja alta incidência do sol, aumenta o BTU ideal em 15%
            if exposicaoAoSol == 's':
                btuIdeal *= 1.15

            
            configuracao_ambiente.clear() # Limpar configuração anterior para evitar acúmulo de dados
            configuracao_ambiente.extend([areaMQ, qtdPessoas, qtdEletronicos, exposicaoAoSol, btuIdeal]) # Adicionar os dados ao ambiente configurado
 
            cls()
            print("Configuração realizada com sucesso!")
            print(f"Área: {areaMQ:.2f}m²\nBTU Ideal: {btuIdeal:.2f}")
            input("\nPressione ENTER para retornar ao menu.")
            break  # Sai do loop e retorna ao menu após configuração bem-sucedida
        
        except ValueError:
            print(f"\nErro: entrada inválida. Tente novamente.")
            input("\nPressione ENTER para tentar novamente.")
            cls()  # Limpa a tela antes de permitir nova tentativa


# Função para mostrar as configurações do ambiente
def mostrar_configuracoes():

    # Mensagem de erro caso não haja um ambiente configurado
    if len(configuracao_ambiente) < 5:
        print("Erro: o ambiente não foi configurado corretamente.")
        return input("\nPressione ENTER para tentar novamente.")


    # Pegando as informações de ambiente da lista 
    areaMQ = configuracao_ambiente[0]
    qtdPessoas = configuracao_ambiente[1]
    qtdEletronicos = configuracao_ambiente[2]
    exposicaoAoSol = configuracao_ambiente[3]
    btuIdeal = configuracao_ambiente[4]

    cls()
    print("Configuração do Ambiente:\n")
    print(f"Área: {areaMQ:.2f} m²")
    print(f"Quantidade de pessoas: {qtdPessoas}")
    print(f"Quantidade de eletrônicos: {qtdEletronicos}")
    print(f"Exposição ao sol: {'Alta' if exposicaoAoSol == 's' else 'Baixa'}")
    print(f"BTU Ideal: {btuIdeal:.2f}")
    
    input("\nPressione ENTER para voltar ao Menu Inicial.")


# Função para calcular o consumo do ventilador do Poço Canadense
def calcular_consumo_ventilador(consumo_ventilador_watts):
    
    # Mensagem de erro caso não haja um ambiente configurado
    if len(configuracao_ambiente) < 5:
        print("Erro: o ambiente não foi configurado corretamente.")
        return input("\nPressione ENTER para tentar novamente.")

    horas_por_dia = 24  # Uso constante, 24/7
    dias_no_mes = 30 # Levando em conta um mês de 30 dias
    preco_kwh = 0.85  # Preço médio de 1kWh em real (São Paulo)

    # Cálculo do consumo mensal do ventilador
    consumo_mensal = (consumo_ventilador_watts / 1000) * horas_por_dia * dias_no_mes * preco_kwh

    return consumo_mensal



# Função para calcular o consumo do ar-condicionado
def calculo_consumo_ar():    
    
    # Mensagem de erro caso não haja um ambiente configurado
    if len(configuracao_ambiente) < 5:
        print("Erro: o ambiente não foi configurado corretamente.")
        return input("\nPressione ENTER para voltar ao Menu Inicial.")
    
    btu = configuracao_ambiente[4]
    consumo_kwh = (btu / 1000) * 0.1  # Consumo médio por hora em kWh
    preco_kwh = 0.85  # Preço médio do kWh em reais (São Paulo)
        
    # Tempo de uso do ar condicionado
    while True:
        try:
            horas_dia = float(input("Horas de uso do ar-condicionado por dia: "))
            if horas_dia < 0:
                input("a quantidade de horas não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            input("valor inválido. Por favor, insira um número válido para as horas.")
    
    consumo_mensal = consumo_kwh * horas_dia * 30 * preco_kwh # Considerando um mês de 30 dias
    return consumo_mensal


# Função para comparar os sistemas quando utilizados em conjunto
def comparar_sistemas_em_conjunto():
    
    # Mensagem de erro caso não haja um ambiente configurado
    if len(configuracao_ambiente) < 5:
        print("Erro: o ambiente não foi configurado corretamente.")
        return input("\nPressione ENTER para voltar ao Menu Inicial.")
    
    cls()
    print("Comparando Ar-condicionado e Poço Canadense em conjunto:")

    # Dados do Poço Canadense
    potencia_ventilador = 50  # Potência fixa do ventilador em Watts, usando 50 como referência média 

    # Cálculo do consumo mensal do Poço Canadense (ventilador)
    consumo_mensal_poco = calcular_consumo_ventilador(potencia_ventilador)

    # Cálculo para o consumo mensal do ar-condicionado
    consumo_mensal_ar = calculo_consumo_ar()

    # Considerando que o poço canadense ajuda a reduzir a carga do ar-condicionado em 45%
    consumo_mensal_ar_reduzido = consumo_mensal_ar * 0.55

    # Exibindo resultados
    cls()
    print("Resultados da Comparação:")
    print("\nAr Condicionado:")
    print(f"- Consumo mensal: R$ {consumo_mensal_ar:.2f}")
        
    print(f"\nPoço Canadense:")
    print(f"- Consumo mensal aproximado (50w): R$ {consumo_mensal_poco:.2f}")
    
    print(f"\nTotal:")
    print(f"- Soma dos valores dos dois sistemas: R$ {(consumo_mensal_ar_reduzido + consumo_mensal_poco):.2f}")
    
    print(f"O ar-condicionado com auxílio do poço canadense consome até 45% menos energia, diminuindo o custo para R$ {consumo_mensal_ar_reduzido:.2f}")
    print(f"\nA economia em relação ao uso exclusivo do ar-condicionado: R$ {(consumo_mensal_ar - consumo_mensal_ar_reduzido):.2f}")
    print("")

    input("\nPressione ENTER para retornar ao Menu Inicial.")


def redirecionar_website():
    cls()
    print('Confira nosso website em: https://geobalance.github.io/geo-balance/index.html')
    
    input("\nPressione ENTER para retornar ao Menu Inicial.")
    