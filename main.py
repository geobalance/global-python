from funcoes import *

# Menu
def menu():
    while True:
        cls()
        print("Calculadora Geo Balance\n")
        print("1. Configurar Ambiente")
        print("2. Ver configuração")
        print("3. Comparar Custos de Climatização")
        print("4. Acessar website")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        # Opção 1 do Menu
        if opcao == '1':
            configurar_ambiente()
            
        # Opção 2 do Menu
        elif opcao == '2':
            mostrar_configuracoes()
            
        # Opção 3 do Menu
        elif opcao == '3':
            comparar_sistemas_em_conjunto()
            
            
        # Opção 4 do Menu 
        elif opcao == '4':
            redirecionar_website()
        
        
        # Opção 5 do Menu   
        elif opcao == '5':
            cls()
            print("Encerrando...")
            break
        
        # Erros de opção inválida
        else:
            cls()
            print("Opção inválida!")
            input("\nPressione ENTER para voltar ao Menu Inicial.")

# Executar menu
if __name__ == "__main__":
    menu()
