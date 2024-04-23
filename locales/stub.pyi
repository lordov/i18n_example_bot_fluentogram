from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    button: Button
    no: No


class Hello:
    @staticmethod
    def user(*, username) -> Literal["""Hello { $username }. Click on the button"""]: ...


class Button:
    @staticmethod
    def button() -> Literal["""Button"""]: ...

    @staticmethod
    def pressed() -> Literal["""You pressed the button"""]: ...


class No:
    @staticmethod
    def copy() -> Literal["""This type of update is not supported by the send_copy method"""]: ...

