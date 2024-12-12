import requests

def fetch_crypto_prices(crypto_ids):
    """Obtém os preços atuais de criptomoedas usando a API da CoinGecko.

    Args:
        crypto_ids (list): Lista de IDs das criptomoedas (ex.: ["bitcoin", "ethereum"]).

    Returns:
        dict: Um dicionário com os preços atuais das criptomoedas.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(crypto_ids),
        "vs_currencies": "usd"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar preços: {e}")
        return {}

# Exemplo de uso:
if __name__ == "__main__":
    crypto_ids = ["bitcoin", "ethereum", "polkadot"]
    prices = fetch_crypto_prices(crypto_ids)
    print("Preços atuais:")
    for crypto, data in prices.items():
        print(f"{crypto.capitalize()}: ${data['usd']}")
