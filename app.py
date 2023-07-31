from abc import ABC, abstractmethod
from typing import List, Dict, Any
from data import PartsDB


class ComputerParts(ABC):
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.price = kwargs.get("price")

    @abstractmethod
    def get_name(self, search_name) -> List:
        pass

    @abstractmethod
    def get_price(self, search_price) -> List:
        pass


class CPU(ComputerParts):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.core_count = kwargs.get("core_count")
        self.perfomance_core_clock = kwargs.get("perfomance_core_clock")
        self.perfomance_boost_clock = kwargs.get("perfomance_boost_clock")
        self.tdp = kwargs.get("TDP")
        self.integrated_graphics = kwargs.get("integrated_graphics")
        self.smt = kwargs.get("SMT")

    @staticmethod
    def find_cpu_by_name(name: str):
        """Funkcija randa CPU dalį pagal pavadinimą"""
        for part_id, part_info in PartsDB.cpu.items():
            if part_info["name"] == name:
                return part_id, part_info
        return None

    # @staticmethod
    # def sorting_by_price() -> bool:
    #     return CPU.part_info["price"] > 100

    def get_name(self, search_name: str) -> List:
        """Function find info in dictionary by name"""
        names = []
        for _, part_info in PartsDB.cpu.items():
            if part_info["name"] == search_name:
                names.append(part_info)
        return names

    def get_price(self, search_price: float) -> List:
        """Function find info in dictionary by price"""
        prices = []
        for _, info in PartsDB.cpu.items():
            if search_price == info["price"]:
                prices.append(info)
        return prices

    def get_integrated_graphics(self, search_graphics: str) -> List:
        """Function find info in dictionary by integrate graphic"""
        graphics = []
        for _, info in PartsDB.cpu.items():
            if search_graphics == info["integrated_graphics"]:
                graphics.append(info)
        return graphics


class Storage(ComputerParts):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.capacity = kwargs.get("capacity")
        self.type = kwargs.get("type")
        self.cache = kwargs.get("cache")
        self.form_factor = kwargs.get("form_factor")
        self.interface = kwargs.get("interface")

    @staticmethod
    def find_storage_by_name(name: str):
        """Funkcija randa Storage dalį pagal pavadinimą"""
        for part_id, part_info in PartsDB.storage.items():
            if part_info["name"] == name:
                return part_id, part_info
        return None

    def get_name(self, search_name: str) -> List:
        """Function find info in dictionary by name"""
        names = []
        for _, info in PartsDB.storage.items():
            if search_name == info["name"]:
                names.append(info)
        return names

    def get_price(self, search_price: float) -> List:
        """Function find info in dictionary by price"""
        prices = []
        for _, info in PartsDB.storage.items():
            if search_price == info["price"]:
                prices.append(info)
        return prices

    def get_capacity(self, search_capacity: str) -> List:
        """Function find info in dictionary by capacity"""
        capacity = []
        for _, info in PartsDB.storage.items():
            if search_capacity == info["capacity"]:
                capacity.append(info)
        return capacity


if __name__ == "__main__":
    searched_cpu_name = "AMD Ryzen 5 5600X"
    cpu_info = CPU.find_cpu_by_name(searched_cpu_name)
    if cpu_info:
        cpu_id, cpu_info = cpu_info
        print(f"CPU {searched_cpu_name} yra PartsDB.cpu[{cpu_id}]:")
        print(cpu_info)
    else:
        print(f"CPU {searched_cpu_name} nerastas.")

    cpu = CPU(**cpu_info)
    print(cpu.get_name("AMD Ryzen 5 5600X"))
    print(cpu.get_price("$162.66"))
    print(cpu.get_integrated_graphics("Intel UHD Graphics 770"))

    searched_storage_name = "Samsung 980 Pro"
    storage_info = Storage.find_storage_by_name(searched_storage_name)
    if storage_info:
        storage_id, storage_info = storage_info
        print(f"Storage {searched_storage_name} yra PartsDB.storage[{storage_id}]:")
        print(storage_info)
    else:
        print(f"Storage {searched_storage_name} nerastas.")

    storage = Storage(**storage_info)
    print(storage.get_name("Samsung 980 Pro"))
    print(storage.get_price("$119.99"))
    print(storage.get_capacity("1 TB"))


# import re

# words = ["zodzio1", "zodzio2", "zodzio3", "zodzio4", "zodzio5"]  # ir t.t.
# search_name = input("Iveskite paieskos zodi: ")

# matching_words = [word for word in words if re.search(search_name, word, re.IGNORECASE)]
# print("Atitinkantys zodziai:", matching_words)
