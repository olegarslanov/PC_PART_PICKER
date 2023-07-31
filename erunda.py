from abc import ABC, abstractmethod
from typing import List, Dict, Any
from data import PartsDB


class ComputerParts(ABC):
    def __init__(self, part_info: Dict[str, Any]) -> None:
        self.name = part_info["name"]
        self.price = part_info["price"]

    @abstractmethod
    def get_name(self, search_name: str) -> Any:
        pass

    @abstractmethod
    def get_price(self, search_price: float) -> Any:
        pass


class CPU(ComputerParts):
    def __init__(self, part_info: Dict[str, Any]) -> None:
        super().__init__(part_info)
        self.core_count = part_info["core_count"]
        self.perfomance_core_clock = part_info["perfomance_core_clock"]
        self.perfomance_boost_clock = part_info["perfomance_boost_clock"]
        self.tdp = part_info["TDP"]
        self.integrated_graphics = part_info["integrated_graphics"]
        self.smt = part_info["SMT"]

    @staticmethod
    def find_cpu_by_name(name: str):
        """Funkcija randa CPU dalį pagal pavadinimą"""
        for part_id, part_info in PartsDB.cpu.items():
            if part_info["name"] == name:
                return part_id, part_info
        return None

    def get_name(self, search_name: str) -> Any:
        """Function find info in dictionary by name"""
        for _, part_info in PartsDB.cpu.items():
            if part_info["name"] == search_name:
                return part_info
        return None

    def get_price(self, search_price: float) -> Any:
        """Function find info in dictionary by price"""
        for _, info in PartsDB.cpu.items():
            if search_price == info["price"]:
                return info
        return None


class Storage(ComputerParts):
    def get_name(self, search_name: str) -> Any:
        """Function find info in dictionary by name"""
        for _, info in PartsDB.storage.items():
            if search_name == info["name"]:
                return info
        return None

    def get_price(self, search_price: float) -> Any:
        """Function find info in dictionary by price"""
        for _, info in PartsDB.storage.items():
            if search_price == info["price"]:
                return info
        return None


if __name__ == "__main__":
    searched_cpu_name = "AMD Ryzen 5 5600X"
    cpu_info = CPU.find_cpu_by_name(searched_cpu_name)
    if cpu_info:
        cpu_id, cpu_info = cpu_info
        print(f"CPU {searched_cpu_name} yra PartsDB.cpu[{cpu_id}]:")
        print(cpu_info)

        cpu = CPU(
            cpu_info
        )  # Perduoti tik konkrečią CPU dalies informaciją, o ne visą žodyną
        print(cpu.get_name("AMD Ryzen 5 5600X"))
        print(cpu.get_price("$162.66"))
    else:
        print(f"CPU {searched_cpu_name} nerastas.")
