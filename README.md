# upbit warpper
API Wrapper for upbit

## Installation

```bash
pip install upbit-wrapper
```

## Import

```py
from upbit_wrapper import Upbit
```

## Usage

Upbit 객체 생성

```py
ub = Upbit('access_key','secret_key')
```

## EXCHANGE API

### 전체 계좌 조회

```py
>>> ub.accounts()
[{'currency': 'KRW', 'balance': '0000.0000', 'locked': '0.0', 'avg_buy_price': '0', 'avg_buy_price_modified': True, 'unit_currency': 'KRW'}]
```

### 주문 가능 정보

```py
>>> ub.order_chance(market="KRW-BTC")
{'bid_fee': '0.0005', 'ask_fee': '0.0005', 'maker_bid_fee': '0.0005', 'maker_ask_fee': '0.0005', 'market': {'id': 'KRW-BTC', 'name': 'BTC/KRW', 'order_types': ['limit'], 'order_sides': ['ask', 'bid'], 'bid': {'currency': 'KRW', 'price_unit': None, 'min_total': '5000.0'}, 'ask': {'currency': 'BTC', 'price_unit': None, 'min_total': '5000.0'}, 'max_total': '1000000000.0', 'state': 'active'}, 'bid_account': {'currency': 'KRW', 'balance': '0000.0000', 'locked': '0.0', 'avg_buy_price': '0', 'avg_buy_price_modified': True, 'unit_currency': 'KRW'}, 'ask_account': {'currency': 'BTC', 'balance': '0.0', 'locked': '0.0', 'avg_buy_price': '55699000', 'avg_buy_price_modified': False, 'unit_currency': 'KRW'}}
```

### 개별 주문 조회

```py
>>> ub.orders(uuid='9ca023a5-851b-4fec-9f0a-48cd83c2eaae')
{'uuid': '9ca023a5-851b-4fec-9f0a-48cd83c2eaae', 'side': 'ask', 'ord_type': 'limit', 'price': '4280000.0', 'state': 'done', 'market': 'KRW-BTC', 'created_at': '2019-01-04T13:48:09+09:00', 'volume': '1.0', 'remaining_volume': '0.0', 'reserved_fee': '0.0', 'remaining_fee': '0.0', 'paid_fee': '2140.0', 'locked': '0.0', 'executed_volume': '1.0', 'trades_count': 1, 'trades': [{'market': 'KRW-BTC', 'uuid': '9e8f8eba-7050-4837-8969-cfc272cbe083', 'price': '4280000.0', 'volume': '1.0', 'funds': '4280000.0', 'side': 'ask'}]}
```

### 주문 리스트 조회

```py
>>> ub.lists_orders(state='done')
[{'uuid': 'fc7bc9e6-ecd8-4d2d-8f0b-868018cc71a2', 'side': 'ask', 'ord_type': 'limit', 'price': '55800000.0', 'state': 'done', 'market': 'KRW-BTC', 'created_at': '2021-02-17T15:12:39+09:00', 'volume': '0.00023995', 'remaining_volume': '0.0', 'reserved_fee': '0.0', 'remaining_fee': '0.0', 'paid_fee': '6.694605', 'locked': '0.0', 'executed_volume': '0.00023995', 'trades_count': 1}, {'uuid': 'd17fb771-ebba-4947-8428-ad5fd0b4caf5', 'side': 'bid', 'ord_type': 'limit', 'price': '55699000.0', 'state': 'done', 'market': 'KRW-BTC', 'created_at': '2021-02-17T15:11:56+09:00', 'volume': '0.00023995', 'remaining_volume': '0.0', 'reserved_fee': '6.682487525', 'remaining_fee': '0.0', 'paid_fee': '6.682487525', 'locked': '0.0', 'executed_volume': '0.00023995', 'trades_count': 1}, {'uuid': '0daef921-4ee9-4479-9a8a-91961aceea41', 'side': 'ask', 'ord_type': 'limit', 'price': '54353000.0', 'state': 'done', 'market': 'KRW-BTC', 'created_at': '2021-02-17T00:13:27+09:00', 'volume': '0.00024608', 'remaining_volume': '0.0', 'reserved_fee': '0.0', 'remaining_fee': '0.0', 'paid_fee': '6.68759312', 'locked': '0.0', 'executed_volume': '0.00024608', 'trades_count': 1}, {'uuid': 'b4a88739-4071-4111-a399-c27714583455', 'side': 'bid', 'ord_type': 'limit', 'price': '54352000.0', 'state': 'done', 'market': 'KRW-BTC', 'created_at': '2021-02-17T00:06:21+09:00', 'volume': '0.00024608', 'remaining_volume': '0.0', 'reserved_fee': '6.68747008', 'remaining_fee': '0.00159952', 'paid_fee': '6.68587056', 'locked': '3.20063952', 'executed_volume': '0.00024608', 'trades_count': 1}, {'uuid': '8eee6789-f92f-434f-84fa-98041a7e1a35', 'side': 'ask', 'ord_type': 'limit', 'price': '53769000.0', 'state': 'done', 'market': 'KRW-BTC', 'created_at': '2021-02-16T14:55:12+09:00', 'volume': '0.000249', 'remaining_volume': '0.0', 'reserved_fee': '0.0', 'remaining_fee': '0.0', 'paid_fee': '6.6942405', 'locked': '0.0', 'executed_volume': '0.000249', 'trades_count': 1}, {'uuid': 'deec4616-fbdf-4e4d-9068-01983ef72301', 'side': 'bid', 'ord_type': 'limit', 'price': '54053000.0', 'state': 'done', 'market': 'KRW-BTC', 'created_at': '2021-02-16T14:08:32+09:00', 'volume': '0.000249', 'remaining_volume': '0.0', 'reserved_fee': '6.7295985', 'remaining_fee': '0.0', 'paid_fee': '6.7295985', 'locked': '0.0', 'executed_volume': '0.000249', 'trades_count': 1}, {'uuid': '698ce1bb-dbc0-4c3f-bcba-4089dfeee23c', 'side': 'ask', 'ord_type': 'limit', 'price': '51808000.0', 'state': 'done', 'market': 'KRW-BTC', 'created_at': '2021-02-15T20:04:06+09:00', 'volume': '0.00026', 'remaining_volume': '0.0', 'reserved_fee': '0.0', 'remaining_fee': '0.0', 'paid_fee': '6.73673', 'locked': '0.0', 'executed_volume': '0.00026', 'trades_count': 1}]
```

### 주문 취소 접수

```py
>>> ub.cancel_order(uuid='cdd92199-2897-4e14-9448-f923320408ad')
{'uuid': 'cdd92199-2897-4e14-9448-f923320408ad', 'side': 'bid', 'ord_type': 'limit', 'price': '100.0', 'state': 'wait', 'market': 'KRW-BTC', 'created_at': '2018-04-10T15:42:23+09:00', 'volume': '0.01', 'remaining_volume': '0.01', 'reserved_fee': '0.0015', 'remaining_fee': '0.0015', 'paid_fee': '0.0', 'locked': '1.0015', 'executed_volume': '0.0', 'trades_count': 0}
```

### 주문하기

```py
>>> ub.orders(market = 'KRW-BTC', side ='bid', volume = '0.01', price = '100.0',ord_type = 'limit')
{'uuid': 'cdd92199-2897-4e14-9448-f923320408ad', 'side': 'bid', 'ord_type': 'limit', 'price': '100.0', 'avg_price': '0.0', 'state': 'wait', 'market': 'KRW-BTC', 'created_at': '2018-04-10T15:42:23+09:00', 'volume': '0.01', 'remaining_volume': '0.01', 'reserved_fee': '0.0015', 'remaining_fee': '0.0015', 'paid_fee': '0.0', 'locked': '1.0015', 'executed_volume': '0.0', 'trades_count': 0}
```

### 출금 리스트 조회

```py
>>> ub.withdraws(currency= 'XRP',state='done')
[{'type': 'withdraw', 'uuid': '35a4f1dc-1db5-4d6b-89b5-7ec137875956', 'currency': 'XRP', 'txid': '98c15999f0bdc4ae0e8a-ed35868bb0c204fe6ec29e4058a3451e-88636d1040f4baddf943274ce37cf9cc', 'state': 'DONE', 'created_at': '2019-02-28T15:17:51+09:00', 'done_at': '2019-02-28T15:22:12+09:00', 'amount': '1.00', 'fee': '0.0', 'transaction_type': 'default'}]
```

### 개별 출금 조회

```py
>>> ub.withdraw(uuid='d17fb771-ebba-4947-8428-ad5fd0b4caf5')
{'type': 'withdraw', 'uuid': '9f432943-54e0-40b7-825f-b6fec8b42b79', 'currency': 'BTC', 'txid': 'null', 'state': 'processing', 'created_at': '2018-04-13T11:24:01+09:00', 'done_at': 'null', 'amount': '0.01', 'fee': '0.0', 'transaction_type': 'default'}
```

### 출금 가능 정보

```py
>>> ub.withdraws_chance(currency='BTC')
{'member_level': {'security_level': 5, 'fee_level': 0, 'email_verified': True, 'identity_auth_verified': True, 'bank_account_verified': True, 'kakao_pay_auth_verified': True, 'locked': False, 'wallet_locked': False}, 'currency': {'code': 'BTC', 'withdraw_fee': '0.0009', 'is_coin': True, 'wallet_state': 'working', 'wallet_support': ['deposit', 'withdraw']}, 'account': {'currency': 'BTC', 'balance': '0.0', 'locked': '0.0', 'avg_buy_price': '55699000', 'avg_buy_price_modified': False, 'unit_currency': 'KRW'}, 'withdraw_limit': {'currency': 'BTC', 'onetime': '50.0', 'daily': None, 'remaining_daily': '0.0', 'remaining_daily_fiat': '1000000000.0', 'fiat_currency': 'KRW', 'minimum': '0.001', 'fixed': 8, 'withdraw_delayed_fiat': '0.0', 'can_withdraw': True, 'remaining_daily_krw': '1000000000.0'}}
```

### 코인 출금하기

```py
>>> ub.withdraws_coin(currency='BTC',amount= '0.01',address='3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD')
{'type': 'withdraw', 'uuid': '9f432943-54e0-40b7-825f-b6fec8b42b79', 'currency': 'BTC', 'txid': 'ebe6937b-130e-4066-8ac6-4b0e67f28adc', 'state': 'processing', 'created_at': '2018-04-13T11:24:01+09:00', 'done_at': None, 'amount': '0.01', 'fee': '0.0', 'krw_amount': '80420.0', 'transaction_type': 'default'}
```

### 원화 출금하기

```py
>>> ub.withdraws_krw(amount='10000')
{'type': 'withdraw', 'uuid': 'cbf65cb4-4794-4060-a052-3cab3ed975aa', 'currency': 'KRW', 'txid': None, 'holder': None, 'confirmations': 0, 'blockchain_url': None, 'state': 'processing', 'state_i18n': '출금진행중', 'created_at': '2021-02-21T12:55:51+09:00', 'done_at': None, 'amount': '10000.0', 'fee': '1000.0', 'krw_amount': '10000.0', 'fiat_amount': '10000.0', 'fiat_currency': 'KRW', 'transaction_type': 'default', 'bank': None, 'address': None, 'memo': None, 'cancelable': False}
```

### 입금 리스트 조회

```py
>>> ub.deposits(currency='KRW')
[{'type': 'deposit', 'uuid': '044550fd-87e2-4784-b9ca-2e44d560532e', 'currency': 'KRW', 'txid': 'BKD-2021-02-21-d56b45539c3d0eb25b8d48221f', 'state': 'REJECTED', 'created_at': '2021-02-21T11:56:47+09:00', 'done_at': None, 'amount': '5000.0', 'fee': '0.0', 'transaction_type': 'default'}]
```

### 개별 입금 조회

```py
>>> ub.deposit(uuid='044550fd-87e2-4784-b9ca-2e44d560532e')
{'type': 'deposit', 'uuid': '044550fd-87e2-4784-b9ca-2e44d560532e', 'currency': 'KRW', 'txid': 'BKD-2021-02-21-d56b45539c3d0eb25b8d48221f', 'state': 'REJECTED', 'created_at': '2021-02-21T11:56:47+09:00', 'done_at': None, 'amount': '5000.0', 'fee': '0.0', 'transaction_type': 'default'}
```

### 입금 주소 생성 요청

```py
>>> ub.deposits_generate_coin_address(currency='BTC')
{'currency': 'BTC', 'deposit_address': '---', 'secondary_address': None}
```

### 전체 입금 주소 조회

```py
>>> ub.deposits_coin_addresses()
[{'currency': 'BTC', 'deposit_address': '---', 'secondary_address': None}]
```

### 개별 입금 주소 조회

```py
>>> ub.deposits_coin_address(currency='BTC')
{'currency': 'BTC', 'deposit_address': '---', 'secondary_address': None}
```

### 원화 입금하기

```py
>>> ub.deposits_krw(amount='5000')
{'type': 'deposit', 'uuid': '0071878b-f9c8-4183-a3b1-bc2d2b3e6ed4', 'currency': 'KRW', 'txid': 'BKD-2021-02-21-115c8dd441f08582d46d0f4aa4', 'state': 'PROCESSING', 'created_at': '2021-02-21T13:00:07+09:00', 'done_at': None, 'amount': '5000.0', 'fee': '0.0', 'transaction_type': 'default'}
```

### 입출금 현황

```py
>>> ub.status_wallet()
[{'currency': 'BTC', 'wallet_state': 'working', 'block_state': 'normal', 'block_height': 671508, 'block_updated_at': '2021-02-21T03:51:16.963+00:00', 'block_elapsed_minutes': 9}, {'currency': 'POWR', 'wallet_state': 'working', 'block_state': 'normal', 'block_height': 11897978, 'block_updated_at': '2021-02-21T03:58:26.948+00:00', 'block_elapsed_minutes': 1}, 
...
```

### API 키 리스트 조회

```py
>>> ub.api_keys()
[{'access_key': '---', 'expire_at': '2022-02-21T09:42:08+09:00'}]
```

## QUOTATION API

### 마켓 코드 조회

```py
>>> ub.market_all(istDetails='false')
[{'market': 'KRW-BTC', 'korean_name': '비트코인', 'english_name': 'Bitcoin'}, {'market': 'KRW-ETH', 'korean_name': '이더리움', 'english_name': 'Ethereum'}, {'market': 'BTC-ETH', 'korean_name': '이더리움', 'english_name': 'Ethereum'}, {'market': 'BTC-LTC', 'korean_name': '라이트코인', 'english_name': 'Litecoin'}, {'market': 'BTC-XRP', 'korean_name': '리플', 'english_name': 'Ripple'}, {'market': 'BTC-ETC', 'korean_name': '이더리움클래식', 'english_name': 'Ethereum Classic'}, {'market': 'BTC-OMG', 'korean_name': '오미세고', 'english_name': 'OmiseGo'}, ...
```

### 분(Minute) 캔들

```py
>>> ub.candles_minutes(unit='1',market='KRW-BTC',count='1')
[{'market': 'KRW-BTC', 'candle_date_time_utc': '2021-02-21T04:03:00', 'candle_date_time_kst': '2021-02-21T13:03:00', 'opening_price': 65260000.0, 'high_price': 65260000.0, 'low_price': 65230000.0, 'trade_price': 65243000.0, 'timestamp': 1613880231821, 'candle_acc_trade_price': 241967530.04604, 'candle_acc_trade_volume': 3.70857716, 'unit': 1}]
```

### 일(Day) 캔들

```py
>>> ub.candles_days(market='KRW-BTC',count='1')
[{'market': 'KRW-BTC', 'candle_date_time_utc': '2021-02-21T00:00:00', 'candle_date_time_kst': '2021-02-21T09:00:00', 'opening_price': 64260000.0, 'high_price': 65500000.0, 'low_price': 63381000.0, 'trade_price': 65240000.0, 'timestamp': 1613880239791, 'candle_acc_trade_price': 163367985163.01437, 'candle_acc_trade_volume': 2527.65449771, 'prev_closing_price': 64251000.0, 'change_price': 989000.0, 'change_rate': 0.0153927565}]
```

### 주(Week) 캔들

```py
>>> ub.candles_weeks(market='KRW-BTC',count='1')
[{'market': 'KRW-BTC', 'candle_date_time_utc': '2021-02-15T00:00:00', 'candle_date_time_kst': '2021-02-15T09:00:00', 'opening_price': 52711000.0, 'high_price': 65985000.0, 'low_price': 50313000.0, 'trade_price': 65217000.0, 'timestamp': 1613880252579, 'candle_acc_trade_price': 4233869799876.2603, 'candle_acc_trade_volume': 72651.85312333, 'first_day_of_period': '2021-02-15'}]
```

### 월(Month) 캔들

```py
>>> ub.candles_months(market='KRW-BTC',count='1')
[{'market': 'KRW-BTC', 'candle_date_time_utc': '2021-02-01T00:00:00', 'candle_date_time_kst': '2021-02-01T09:00:00', 'opening_price': 36408000.0, 'high_price': 65985000.0, 'low_price': 35907000.0, 'trade_price': 65217000.0, 'timestamp': 1613880263664, 'candle_acc_trade_price': 11922764738629.232, 'candle_acc_trade_volume': 244435.09490025, 'first_day_of_period': '2021-02-01'}]
```

### 최근 체결 내역

```py
>>> ub.trades_ticks(market='KRW-BTC',count='1')
[{'market': 'KRW-BTC', 'trade_date_utc': '2021-02-21', 'trade_time_utc': '04:04:35', 'timestamp': 1613880275000, 'trade_price': 65198000.0, 'trade_volume': 0.03073775, 'prev_closing_price': 64251000.0, 'change_price': 947000.0, 'ask_bid': 'BID', 'sequential_id': 1613880275000001}]
```

### 현재가 정보

```py
>>> ub.ticker(markets='KRW-BTC')
[{'market': 'KRW-BTC', 'trade_date': '20210221', 'trade_time': '040446', 'trade_date_kst': '20210221', 'trade_time_kst': '130446', 'trade_timestamp': 1613880286000, 'opening_price': 64260000.0, 'high_price': 65500000.0, 'low_price': 63381000.0, 'trade_price': 65197000.0, 'prev_closing_price': 64251000.0, 'change': 'RISE', 'change_price': 946000.0, 'change_rate': 0.0147235062, 'signed_change_price': 946000.0, 'signed_change_rate': 0.0147235062, 'trade_volume': 0.00013587, 'acc_trade_price': 163506728111.08755, 'acc_trade_price_24h': 883453500622.5804, 'acc_trade_volume': 2529.77814776, 'acc_trade_volume_24h': 13683.34452421, 'highest_52_week_price': 65985000.0, 'highest_52_week_date': '2021-02-20', 'lowest_52_week_price': 5489000.0, 'lowest_52_week_date': '2020-03-13', 'timestamp': 1613880286709}]
```

### 호가 정보 조회

```py
>>> ub.orderbook(markets='KRW-BTC')
[{'market': 'KRW-BTC', 'timestamp': 1613880297302, 'total_ask_size': 5.59100856, 'total_bid_size': 0.60542686, 'orderbook_units': [{'ask_price': 65198000.0, 'bid_price': 65188000.0, 'ask_size': 0.79993456, 'bid_size': 0.19022283}, {'ask_price': 65215000.0, 'bid_price': 65180000.0, 'ask_size': 0.01210965, 'bid_size': 0.19190695}, {'ask_price': 65217000.0, 'bid_price': 65179000.0, 'ask_size': 0.00662995, 'bid_size': 0.00306838}, {'ask_price': 65222000.0, 'bid_price': 65174000.0, 'ask_size': 0.18458195, 'bid_size': 0.00038358}, {'ask_price': 65233000.0, 'bid_price': 65172000.0, 'ask_size': 0.1845092, 'bid_size': 0.00244774}, {'ask_price': 65240000.0, 'bid_price': 65168000.0, 'ask_size': 0.01096209, 'bid_size': 0.00179135}, {'ask_price': 65243000.0, 'bid_price': 65167000.0, 'ask_size': 0.00611065, 'bid_size': 0.0166231}, {'ask_price': 65244000.0, 'bid_price': 65165000.0, 'ask_size': 0.00160961, 'bid_size': 0.00625076}, {'ask_price': 65245000.0, 'bid_price': 65163000.0, 'ask_size': 0.06076505, 'bid_size': 0.00183329}, {'ask_price': 65246000.0, 'bid_price': 65162000.0, 'ask_size': 0.25989433, 'bid_size': 0.00884131}, {'ask_price': 65247000.0, 'bid_price': 65158000.0, 'ask_size': 0.00381342, 'bid_size': 0.00015347}, {'ask_price': 65248000.0, 'bid_price': 65157000.0, 'ask_size': 0.00081938, 'bid_size': 0.02671611}, {'ask_price': 65250000.0, 'bid_price': 65155000.0, 'ask_size': 3.45347451, 'bid_size': 0.10969465}, {'ask_price': 65255000.0, 'bid_price': 65153000.0, 'ask_size': 0.00443507, 'bid_size': 0.00024143}, {'ask_price': 65259000.0, 'bid_price': 65150000.0, 'ask_size': 0.60135914, 'bid_size': 0.04525191}]}]
```