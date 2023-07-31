import unittest
from app import CPU, Storage
from data import PartsDB


class TestCPU(unittest.TestCase):
    def test_get_cpu_name(self):
        cpu_info = PartsDB.cpu[1]  # pasirenkame CPU su ID 1

        cpu = CPU(**cpu_info)

        result = cpu.get_name("AMD Ryzen 5 5600X")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "AMD Ryzen 5 5600X")

    def test_get_cpu_price(self):
        cpu_info = PartsDB.cpu[1]  # pasirenkame CPU su ID 1

        cpu = CPU(**cpu_info)
        result = cpu.get_price("$162.66")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["price"], "$162.66")


class TestStorage(unittest.TestCase):
    def test_get_storage_name(self):
        storage_info = PartsDB.storage[1]

        storage = Storage(**storage_info)

        result = storage.get_name("Samsung 980 Pro")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Samsung 980 Pro")

    def test_get_storage_price(self):
        storage_info = PartsDB.storage[1]  # pasirenkame CPU su ID 1

        storage = Storage(**storage_info)
        result = storage.get_price("$119.99")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["price"], "$119.99")


# def test_atbulai1(self):
#     rezultatas = self.object.atbulai()
#     lukestis = "skot ary satsket onaM"
#     self.assertEqual(lukestis, rezultatas)

# def test_atbulai2(self):
#     rezultatas = Sakinys().atbulai()
#     lukestis = "nohtyP fo neZ"
#     self.assertEqual(lukestis, rezultatas)


if __name__ == "__main__":
    unittest.main()


# Testo paleidimas komandinėje eilutėje (cmd):
# python -m unittest test.py
