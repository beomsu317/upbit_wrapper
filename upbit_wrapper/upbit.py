# https://docs.upbit.com/reference

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
        self.access_key = "3WgvdXznDQzIJGhREHJiC64coZbdAfDCIOyXpyB1"
        self.secret_key = "ncaJMITyeSt0AQxGdQcj1x8a8FV9nKDLGmsFmKcs"
        self.auth_token = None

    def __connect(self,method,api_path, **kwargs):
        """
        request 
        """
        url = urljoin(self.server_url,api_path)
        self.logger.debug(f"connect to {url}")
        res = requests.request(method=method, url=url, **kwargs)
        if(res.status_code == 200):
            self.logger.debug("successfule connection")
            return res
        else:
            self.logger.error(f"failed connection: {res.json()}")
            return False

    def __make_headers(self,payload):
        """
        make authorize_token and headers
        """
        jwt_token = jwt.encode(payload, self.secret_key).decode('utf-8')
        authorize_token = 'Bearer {}'.format(jwt_token)
        headers = {"Authorization": authorize_token}
        return headers

    def __make_query_hash(self,query):
        """
        make query hash
        """
        query_string = urlencode(query).encode()

        m = hashlib.sha512()
        m.update(query_string)
        return m.hexdigest()

    def accounts(self):
        """
        [Description]
        내가 보유한 자산 리스트를 보여준다.

        [Usage]
        accounts()
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
            self.logger.error("accounts failed")
            return False

    def order_chance(self,**kwargs):
        """
        [Description]
        마켓 별 주문 가능 정보를 확인한다.

        [Params]
        market(string) : Market ID

        [Usage]
        order_chance(market="KRW-BTC")
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("order chance failed")
            return False

    
    def order(self,**kwargs):
        """
        [Description]
        주문 UUID 를 통해 개별 주문건을 조회한다.

        [Params]
        uuid(string) : 주문 UUID
        identifier(string) : 조회용 사용자 지정 값

        [Usage]
        orders(uuid='uuid')

        [Warning]
        uuid 혹은 identifier 둘 중 하나의 값이 반드시 포함되어야 함
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]

        query_hash = self.__make_query_hash(query)

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
            self.logger.error("indivisual order failed")
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
        lists_orders(state='done')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("list orders failed")
            return False

    def cancel_order(self, **kwargs):
        """
        [Description]
        주문 UUID를 통해 해당 주문에 대한 취소 접수를 한다.

        [Params]
        uuid(string) : 주문 UUID
        identifier(string) : 조회용 사용자 지정 값

        [Usage]
        cancel_order(uuid='uuid')

        [Warning]
        uuid 혹은 identifier 둘 중 하나의 값이 반드시 포함되어야 함
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("cancel order failed")
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
        orders(market = 'KRW-BTC', side ='bid', volume = '0.01', price = '100.0',ord_type = 'limit')

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
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("orders failed")
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
        withdraws(currency= 'XRP',state='done')
        """

        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("withdraws failed")
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
        withdraw(uuid='d17fb771-ebba-4947-8428-ad5fd0b4caf5'))
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("withdraw failed")
            return False

    def withdraws_chance(self,**kwargs):
        """
        [Description]
        해당 통화의 가능한 출금 정보를 확인한다.
        
        [Params]
        currency(string) : Currency symbol

        [Usage]
        withdraws_chance(currency='BTC')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("withdraws chance failed")
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
        withdraws_coin(currency='BTC',amount= '0.01',address='3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD')
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("withdraws coin failed")
            return False

    def withdraws_krw(self,**kwargs):
        """
        [Description]
        원화 출금을 요청한다. 등록된 출금 계좌로 출금된다.

        [Params]
        amount(string) : 출금 원화 수량

        [Usage]
        withdraws_krw()
        """
        query = {}
        for item in kwargs.items():
            query[item[0]] = item[1]
        
        query_hash = self.__make_query_hash(query)

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
            self.logger.error("withdraws krw failed")
            return False