from crypto_data import get_coins, Coin
import time

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top:
                print(coin, '!!TRIGGER!! --- The crypto coin is higher than top threshold!')
            elif coin.current_price < bottom:
                print(coin, '!!TRIGGER!! --- The crypto coin is lower than bottom threshold!')
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    while True:
        alert('btc', bottom=20_00, top=30_00, coins_list=coins)
        alert('eth', bottom=1800, top=3000, coins_list=coins)
        alert('bnb', bottom=500, top=600, coins_list=coins)
        time.sleep(35)