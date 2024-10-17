# coding:utf-8

from base64 import b64encode
from datetime import datetime
import os
from typing import Dict
from typing import Optional
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse

from requests import Response
from requests import Session


class page:
    def __init__(self, url: str, session: Optional[Session] = None):
        self.__url: str = url
        self.__session: Session = session or Session()

    @property
    def url(self) -> str:
        return self.__url

    @property
    def label(self) -> str:
        encode: bytes = self.url.encode(encoding="utf-8")
        decode: str = b64encode(encode).decode(encoding="utf-8").rstrip("=")
        return f"{datetime.now().strftime(f'%Y%m%d%H%M%S')}-{decode}"

    @property
    def session(self) -> Session:
        return self.__session

    def save(self, path: Optional[str] = None) -> str:
        file: str = self.label if path is None else os.path.join(path, self.label) if os.path.isdir(path) else path  # noqa:E501
        with open(file=file, mode="w") as hdl:
            hdl.write(self.fetch())
        return file

    def fetch(self) -> str:
        response = self.session.get(self.url)
        response.raise_for_status()
        return response.text


class site:
    def __init__(self, base: str, session: Optional[Session] = None):
        # self.__base: str = base
        components = urlparse(url=base)
        self.__scheme: str = components.scheme or "https"
        self.__netloc: str = components.netloc or components.path
        self.__scheme_and_netloc: str = urlunparse((self.scheme, self.netloc, '', '', '', ''))  # noqa:E501
        self.__session: Session = session or Session()

    @property
    def scheme(self) -> str:
        return self.__scheme

    @property
    def netloc(self) -> str:
        return self.__netloc

    @property
    def scheme_and_netloc(self) -> str:
        return self.__scheme_and_netloc

    @property
    def session(self) -> Session:
        return self.__session

    def page(self, *path: str) -> page:
        url: str = urljoin(base=self.scheme_and_netloc, url="/".join(path))
        return page(url=url, session=self.session)

    def login(self, url: str, data: Dict[str, str]) -> Response:
        response = self.session.post(url=url, data=data)
        return response
