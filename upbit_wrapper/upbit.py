# https://docs.upbit.com/

import os
import sys
import logging
import jwt
import uuid
import hashlib
import requests
from urllib.parse import urlencode
from urllib.parse import urljoin

from requests.api import head

class Upbit:
    def __init__(self,access_key,secret_key):
        self.logger = logging.getLogger("Upbit")
        self.server_url = "https://api.upbit.com"
        self.access_key = access_key
        self.secret_key = secret_key
        self.auth_token = None

    def __connect(self,method,api_path, **kwargs):
        """
        [Description]
        내부에서 사용하는 request 요청
        """
        url = urljoin(self.server_url,api_path)
        res = requests.request(method=method, url=url, **kwargs)
        
        if(res.status_code >= 200 and res.status_code < 300):
            return res
        else:
            self.logger.error(f"connect failed reason : {res.content.decode()}")
            return False

    def __make_headers(self,payload):
        """
        [Description]
        make authorize_token and headers
        """
        jwt_token = jwt.encode(payload, self.secret_key).decode('utf-8')
        authorize_token = 'Bearer {}'.format(jwt_token)
        headers = {"Authorization": authorize_token}
        return headers

    def __make_query_hash(self,query_string):
        """
        [Description]
        make query hash
        """
        m = hashlib.sha512()
        m.update(query_string)
        return m.hexdigest()

    '''
    EXCHANGE API
    '''
    def accounts(self):
        """
        [Description]
        내가 보유한 자산 리스트를 보여준다.

        [Usage]
        ub.accounts()
        """
        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/accounts",headers=headers)

        if res:
            return res.json()
        else:
            self.logger.error("accounts() failed")
            return False

    def order_chance(self,**kwargs):
        """
        [Description]
        마켓 별 주문 가능 정보를 확인한다.

        [Params]
        market(string) : Market ID

        [Usage]
        ub.order_chance(market="KRW-BTC")
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
            
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/orders/chance",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("order_chance() failed")
            return False

    
    def order(self,**kwargs):
        """
        [Description]
        주문 UUID 를 통해 개별 주문건을 조회한다.

        [Params]
        uuid(string) : 주문 UUID
        identifier(string) : 조회용 사용자 지정 값

        [Usage]
        ub.orders(uuid='uuid')

        [Warning]
        uuid 혹은 identifier 둘 중 하나의 값이 반드시 포함되어야 함
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]

        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/order",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("order() failed")
            return False

    def lists_orders(self,**kwargs):
        """
        [Description]
        주문 리스트를 조회한다.

        [Params]
        market(string) : Market ID
        state(string) : 주문 상태
        states(array of strings) : 주문 상태 목록
        uuids(array of strings) : 주문 UUID의 목록
        identifiers(array of strings) : 주문 identifier의 목록
        page(int32) : 요청 페이지
        limit(int32) : 요청 개수 (1 ~ 100)
        order_by(string) : 정렬

        [Usage]
        ub.lists_orders(state='done')
        """

        query = {}
        array_of_strings_lists = []
        for item in kwargs.items():
            if type(item[1]) == list:
                array_of_strings_lists.append(item)
            else:
                query[item[0]] = item[1]
        
        query_string = urlencode(query)
        
        for array_of_string in array_of_strings_lists:
            query[f"{array_of_string[0]}[]"]=array_of_string[1]
            
            query_string = "{}&{}".format(query_string,'&'.join([f"{array_of_string[0]}[]={x}" for x in array_of_string[1]])) 

        query_string = query_string.encode()

        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/orders",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("list_orders() failed")
            return False

    def cancel_order(self, **kwargs):
        """
        [Description]
        주문 UUID를 통해 해당 주문에 대한 취소 접수를 한다.

        [Params]
        uuid(string) : 주문 UUID
        identifier(string) : 조회용 사용자 지정 값

        [Usage]
        ub.cancel_order(uuid='uuid')

        [Warning]
        uuid 혹은 identifier 둘 중 하나의 값이 반드시 포함되어야 함
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("DELETE","/v1/orders",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("cancel_order() failed")
            return False

    def orders(self,**kwargs):
        """
        [Description]
        주문 요청을 한다.

        [Params]
        market(string) : Market ID
        side(string) : 주문 종류
        volume(string) : 주문 수량
        price(string) : 유닛당 주문 가격
        ord_type(string) : 주문 타입
        identifier(string) : 조회용 사용자 지정 값

        [Usage]
        ub.orders(market = 'KRW-BTC', side ='bid', volume = '0.01', price = '100.0',ord_type = 'limit')

        [Warnings]
        원화 마켓 가격 단위를 확인하세요.
        원화 마켓에서 주문을 요청 할 경우, 원화 마켓 주문 가격 단위 를 확인하여 값을 입력해주세요.

        identifier 파라미터 사용
        identifier는 서비스에서 발급하는 uuid가 아닌 이용자가 직접 발급하는 키값으로, 주문을 조회하기 위해 할당하는 값입니다. 해당 값은 사용자의 전체 주문 내 유일한 값을 전달해야하며, 비록 주문 요청시 오류가 발생하더라도 같은 값으로 다시 요청을 보낼 수 없습니다.
        주문의 성공 / 실패 여부와 관계없이 중복해서 들어온 identifier 값에서는 중복 오류가 발생하니, 매 요청시 새로운 값을 생성해주세요.

        시장가 주문
        시장가 주문은 ord_type 필드를 price or market 으로 설정해야됩니다.
        매수 주문의 경우 ord_type을 price로 설정하고 volume을 null 혹은 제외해야됩니다.
        매도 주문의 경우 ord_type을 market로 설정하고 price을 null 혹은 제외해야됩니다.
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("POST","/v1/orders",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("orders() failed")
            return False

    def withdraws(self,**kwargs):
        """
        [Description]
        출금 리스트를 조회한다.

        [Params]
        currency(string) : Currency 코드
        state(string) : 출금 상태
        uuids(array of strings) : 출금 UUID의 목록  
        txids(array of strings) : 출금 TXID의 목록
        limit(int32) : 요청 개수 (1 ~ 100)
        page(int32) : 요청 페이지
        order_by(string) : 정렬

        [Usage]
        ub.withdraws(currency= 'XRP',state='done')
        """

        query = {}
        array_of_strings_lists = []
        for item in kwargs.items():
            if type(item[1]) == list:
                array_of_strings_lists.append(item)
            else:
                query[item[0]] = item[1]
        
        query_string = urlencode(query)
        
        for array_of_string in array_of_strings_lists:
            query[f"{array_of_string[0]}[]"]=array_of_string[1]
            
            query_string = "{}&{}".format(query_string,'&'.join([f"{array_of_string[0]}[]={x}" for x in array_of_string[1]])) 

        query_string = query_string.encode()

        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/withdraws",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("withdraws() failed")
            return False

    def withdraw(self,**kwargs):
        """
        [Description]
        출금 UUID를 통해 개별 출금 정보를 조회한다.
        
        [Params]
        uuid(string) : 출금 UUID
        txid(string) : 출금 TXID
        currency(string) : Currency 코드

        [Usage]
        ub.withdraw(uuid='d17fb771-ebba-4947-8428-ad5fd0b4caf5')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/withdraw",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("withdraw() failed")
            return False

    def withdraws_chance(self,**kwargs):
        """
        [Description]
        해당 통화의 가능한 출금 정보를 확인한다.
        
        [Params]
        currency(string) : Currency symbol

        [Usage]
        ub.withdraws_chance(currency='BTC')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/withdraws/chance",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("withdraws_chance() failed")
            return False

    def withdraws_coin(self,**kwargs):
        """
        [Description]
        코인 출금을 요청한다.

        [Params]
        currency(string) : Currency symbol
        amount(string) : 출금 코인 수량
        address(string) : 출금 지갑 주소 
        secondary_address(string) : 2차 출금주소 (필요한 코인에 한해서)
        transaction_type(string) : 출금 유형

        [Usage]
        ub.withdraws_coin(currency='BTC',amount= '0.01',address='3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("POST","/v1/withdraws/coin",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("withdraws_coin() failed")
            return False

    def withdraws_krw(self,**kwargs):
        """
        [Description]
        원화 출금을 요청한다. 등록된 출금 계좌로 출금된다.

        [Params]
        amount(string) : 출금 원화 수량

        [Usage]
        ub.withdraws_krw(amount='10000')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("POST","/v1/withdraws/krw",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("withdraws_krw() failed")
            return False

    def deposits(self,**kwargs):
        """
        [Description]
        입금을 리스트를 요청한다.

        [Params]
        currency(string) : Currency 코드
        state(string) : 입금 상태
        uuids(string) : 입금 UUID의 목록
        txids(array of strings) : 입금 TXID의 목록
        limit(int32) : 페이지 당 개수
        page(int32) : 페이지 번호
        order_by(string) : 정렬 방식

        [Usage]
        ub.deposits(currency='KRW')
        """
        query = {}
        array_of_strings_lists = []
        for item in kwargs.items():
            if type(item[1]) == list:
                array_of_strings_lists.append(item)
            else:
                query[item[0]] = item[1]
        
        query_string = urlencode(query)
        
        for array_of_string in array_of_strings_lists:
            query[f"{array_of_string[0]}[]"]=array_of_string[1]
            
            query_string = "{}&{}".format(query_string,'&'.join([f"{array_of_string[0]}[]={x}" for x in array_of_string[1]])) 

        query_string = query_string.encode()

        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/deposits",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("deposits() failed")
            return False


    def deposit(self,**kwargs):
        """
        [Description]
        개별 입금을 조회한다.

        [Params]
        uuids(string) : 개별 입금의 UUID
        txids(string) : 개별 입금의 TXID
        currency(string) : Currency 코드

        [Usage]
        ub.deposit(uuid='94332e99-3a87-4a35-ad98-28b0c969f830')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/deposit",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("deposit() failed")
            return False

    def deposits_generate_coin_address(self,**kwargs):
        """
        [Description]
        입금 주소 생성을 요청한다.

        [Params]
        currency(string) : Currency sysmbol

        [Usage]
        ub.deposits_generate_coin_address(currency='BTC')

        [Warnings]
        입금 주소 생성 요청 API 유의사항
        입금 주소의 생성은 서버에서 비동기적으로 이뤄집니다.
        비동기적 생성 특성상 요청과 동시에 입금 주소가 발급되지 않을 수 있습니다.
        주소 발급 요청 시 결과로 Response1이 반환되며 주소 발급 완료 이전까지 계속 Response1이 반환됩니다.
        주소가 발급된 이후부터는 새로운 주소가 발급되는 것이 아닌 이전에 발급된 주소가 Response2 형태로 반환됩니다.
        정상적으로 주소가 생성되지 않는다면 일정 시간 이후 해당 API를 다시 호출해주시길 부탁드립니다.
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("POST","/v1/deposits/generate_coin_address",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("deposits_generate_coin_address() failed")
            return False

    def deposits_coin_addresses(self):
        """
        [Description]
        전체 입금 주소를 조회한다.

        [Usage]
        ub.deposits_coin_addresses()
        """

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4())
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/deposits/coin_addresses",headers=headers)

        if res:
            return res.json()
        else:
            self.logger.error("deposits_generate_coin_address() failed")
            return False

    def deposits_coin_address(self,**kwargs):
        """
        [Description]
        개별 입금 주소를 조회한다.

        [Params]
        currency(string) : Currency symbol

        [Usage]
        ub.deposits_coin_address(currency='BTC')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/deposits/coin_address",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("deposits_coin_address() failed")
            return False

    def deposits_krw(self,**kwargs):
        """
        [Description]
        원화를 입금한다.

        [Params]
        amount(string) : 입금 원화 수량

        [Usage]
        ub.deposits_krw(amount='5000')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("POST","/v1/deposits/krw",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("deposits_krw() failed")
            return False

    def status_wallet(self):
        """
        [Description]
        입출금 현황 및 블록 상태를 조회합니다.

        [Usage]
        ub.status_wallet()
        """

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4())
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/status/wallet",headers=headers)

        if res:
            return res.json()
        else:
            self.logger.error("status_wallet() failed")
            return False

    def api_keys(self):
        """
        [Description]
        API 키 목록 및 만료 일자를 조회합니다.

        [Usage]
        ub.api_keys()
        """

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4())
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/api_keys",headers=headers)

        if res:
            return res.json()
        else:
            self.logger.error("api_keys() failed")
            return False

    '''
    QUOTATION API
    '''
    def market_all(self,**kwargs):
        """
        [Description]
        업비트에서 거래 가능한 마켓 목록

        [Params]
        isDetails(boolean) : 유의종목 필드과 같은 상세 정보 노출 여부(선택 파라미터)

        [Usage]
        ub.market_all(istDetails='false')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()
        query_hash = self.__make_query_hash(query_string)

        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512',
        }

        headers = self.__make_headers(payload = payload)

        res = self.__connect("GET","/v1/market/all",headers=headers,params=query)

        if res:
            return res.json()
        else:
            self.logger.error("market_all() failed")
            return False

    def candles_minutes(self,**kwargs):
        """
        [Description]
        분(Minute) 캔들

        [Path Params]
        unit(int32) : 분 단위. 가능한 값 : 1, 3, 5, 15, 10, 30, 60, 240

        [Query Params]
        market(string) : 마켓 코드 (ex. KRW-BTC)
        to(string) : 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        count(int32) : 캔들 개수(최대 200개까지 요청 가능)

        [Usage]
        ub.candles_minutes(unit='1',market='KRW-BTC',count='1')
        """
        query = {}
        unit = 1
        for item in kwargs.items():
            if item[0] == "unit":
                unit = item[1]
                continue
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()

        res = self.__connect("GET",f"/v1/candles/minutes/{unit}",params=query_string)

        if res:
            return res.json()
        else:
            self.logger.error("candles_minutes() failed")
            return False

    def candles_days(self,**kwargs):
        """
        [Description]
        일(day) 캔들

        [Query Params]
        market(string) : 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        to(string) : 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        count(int32) : 캔들 개수
        convertingPriceUnit(string) : 종가 환산 화폐 단위 (생략 가능, KRW로 명시할 시 원화 환산 가격을 반환.)

        [Usage]
        ub.candles_days(market='KRW-BTC',count='1')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()

        res = self.__connect("GET","/v1/candles/days",params=query_string)

        if res:
            return res.json()
        else:
            self.logger.error("candles_days() failed")
            return False

    def candles_weeks(self,**kwargs):
        """
        [Description]
        주(week) 캔들

        [Query Params]
        market(string) : 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        to(string) : 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        count(int32) : 캔들 개수

        [Usage]
        ub.candles_weeks(market='KRW-BTC',count='1')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()

        res = self.__connect("GET","/v1/candles/weeks",params=query_string)

        if res:
            return res.json()
        else:
            self.logger.error("candles_weeks() failed")
            return False


    def candles_months(self,**kwargs):
        """
        [Description]
        월(Month) 캔들

        [Query Params]
        market(string) : 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        to(string) : 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        count(int32) : 캔들 개수

        [Usage]
        ub.candles_months(market='KRW-BTC',count='1')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()

        res = self.__connect("GET","/v1/candles/months",params=query_string)

        if res:
            return res.json()
        else:
            self.logger.error("candles_months() failed")
            return False

    def trades_ticks(self,**kwargs):
        """
        [Description]
        최근 체결 내역

        [Query Params]
        market(string) : 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        to(string) : 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss. 비워서 요청시 가장 최근 캔들
        count(int32) : 체결 개수
        cursor(string) : 페이지네이션 커서 (sequentialId)
        daysAgo(int32) : 최근 체결 날짜 기준 7일 이내의 이전 데이터 조회 가능. 비워서 요청 시 가장 최근 체결 날짜 반환. (범위: 1 ~ 7))

        [Usage]
        ub.trades_ticks(market='KRW-BTC',count='1')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()

        res = self.__connect("GET","/v1/trades/ticks",params=query_string)

        if res:
            return res.json()
        else:
            self.logger.error("trades_ticks() failed")
            return False


    def ticker(self,**kwargs):
        """
        [Description]
        요청 당시 종목의 스냅샷을 반환한다.

        [Query Params]
        markets(string) : 반점으로 구분되는 마켓 코드 (ex. KRW-BTC, BTC-BCC)

        [Usage]
        ub.ticker(markets='KRW-BTC')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()

        res = self.__connect("GET","/v1/ticker",params=query_string)

        if res:
            return res.json()
        else:
            self.logger.error("ticker() failed")
            return False

    def orderbook(self,**kwargs):
        """
        [Description]
        호가 정보를 조회한다.

        [Query Params]
        markets(string) : 반점으로 구분되는 마켓 코드 (ex. KRW-BTC, BTC-BCC)

        [Usage]
        ub.orderbook(markets='KRW-BTC')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_string = urlencode(query).encode()

        res = self.__connect("GET","/v1/orderbook",params=query_string)

        if res:
            return res.json()
        else:
            self.logger.error("orderbook() failed")
            return False