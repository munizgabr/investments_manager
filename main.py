import sqlite3
from portfolio import add_asset, view_portfolio

# Conectar ao banco de dados (será criado se não existir)
DB_NAME = "portfolio.db"

def create_tables():
    """Cria as tabelas necessárias no banco de dados."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            quantity REAL NOT NULL,
            purchase_price REAL NOT NULL
        )
        """)
        conn.commit()

def main():
    """Menu principal do sistema."""
    create_tables()
    
    while True:
        print("\n=== Sistema de Gestão de Carteira ===")
        print("1. Adicionar ativo")
        print("2. Visualizar carteira")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            add_asset(DB_NAME)
        elif choice == "2":
            view_portfolio(DB_NAME)
        elif choice == "3":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
