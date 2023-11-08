from typing import Dict

class __StartForm:
    def __init__(self) -> None:
        self.__cache_data = None

    def load_info(self, data: Dict) -> None:
        self.__cache_data = data

    def get_info(self, key: str) -> str:
        if key in self.__cache_data:
            return self.__cache_data[key]
        return None

start_form = __StartForm()
