import sqlite3
import requests
from data_fetcher import fetch_crypto_prices

def add_asset(db_name):
    """Adiciona um ativo à carteira."""
    name = input("Nome do ativo (ex.: BTC, AAPL): ")
    asset_type = input("Tipo do ativo (ex.: Criptomoeda, Ação): ")
    try:
        quantity = float(input("Quantidade: "))
        purchase_price = float(input("Preço de compra por unidade: "))
    except ValueError:
        print("Erro: Quantidade e preço devem ser números.")
        return

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO assets (name, type, quantity, purchase_price)
        VALUES (?, ?, ?, ?)
        """, (name, asset_type, quantity, purchase_price))
        conn.commit()
    print(f"Ativo {name} adicionado com sucesso!")

def view_portfolio(db_name):
    """Exibe a carteira de investimentos com preços em tempo real."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, type, quantity, purchase_price FROM assets")
        assets = cursor.fetchall()

    if not assets:
        print("\nSua carteira está vazia.")
        return

    # Obtendo preços em tempo real para criptomoedas
    crypto_ids = [asset[0].lower() for asset in assets if asset[1].lower() == "criptomoeda"]
    prices = fetch_crypto_prices(crypto_ids)

    print("\n=== Sua Carteira ===")
    print(f"{'Ativo':<10}{'Tipo':<15}{'Quantidade':<12}{'Preço Compra':<15}{'Preço Atual':<15}{'Valor Total':<15}")
    print("-" * 80)

    total_portfolio_value = 0
    for name, asset_type, quantity, purchase_price in assets:
        current_price = prices.get(name.lower(), {}).get('usd', 0) if asset_type.lower() == "criptomoeda" else 0
        total_value = quantity * current_price if current_price else 0
        total_portfolio_value += total_value
        print(f"{name:<10}{asset_type:<15}{quantity:<12}{purchase_price:<15}{current_price:<15}{total_value:<15}")

    print("-" * 80)
    print(f"Valor Total da Carteira: ${total_portfolio_value:.2f}")