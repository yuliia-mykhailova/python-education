"""This module contains system of classes Transport"""
from abc import ABC, abstractmethod
from copy import copy


class Transport(ABC):
    """Represents base vehicle"""

    def __init__(self, name: str, color: str, model: str):
        """Constructor"""
        self._name = name
        self._color = color
        self._model = model

    @abstractmethod
    def get_name(self) -> str:
        """:return name of transport"""


class LicencePlate:
    """Class that represents the licence plate of the transport"""

    def __init__(self, series: str, registration_code: int, country: str):
        self._series = series
        self._registration_code = registration_code
        self.country = country

    def __str__(self):
        """To string method"""
        return "Licence Plate: " + self._series + " " + str(self._registration_code) + \
               ", country:" + str(self.country)

    def __eq__(self, other):
        """Override eq operator"""
        if isinstance(other, Car):
            return self._series == other._series and \
                   self._registration_code == other._registration_code
        return False

    def __ne__(self, other):
        """Override eq operator"""
        if isinstance(other, Car):
            return not self._series == other._series and \
                   self._registration_code == other._registration_code
        return True

    @property
    def license_plate_number(self) -> str:
        """:return license plate of transport"""
        return self._series + str(self._registration_code)

    @license_plate_number.setter
    def license_plate_number(self, registration_code):
        """sets license plate number of transport"""
        self._registration_code = registration_code

    def get_series(self):
        """:return series of license plate"""
        return self._series

    def get_registration_code(self):
        """:return registration code of license plate"""
        return self._registration_code

    def get_country(self):
        """:return country of license plate"""
        return self.country


class Car(Transport, LicencePlate):
    """Class that represents car inherited from Transport and LicensePlate"""

    __isCar = 'Definitely!'

    def __init__(self, name: str, color: str, model: str, amount_doors: int, **kwargs):
        Transport.__init__(self, name, color, model)
        LicencePlate.__init__(self, kwargs['series'], kwargs['registration_code'],
                              kwargs['country'])
        self.amount_doors = amount_doors

    def __str__(self):
        """To string method"""
        return "Car: " + self._name + ", color:" + self._color + ", model:" + self._model + \
               "\nLicense plate:" + self.license_plate_number + \
               "\nCountry:" + self.country

    def __len__(self):
        """Override len(), return length of car name+model"""
        return len(self._name + self._model)

    def __contains__(self, item):
        if item == 'door':
            return self.amount_doors > 2
        return False

    def __copy__(self):
        """:return a copy of a car object"""
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    @property
    def full_model_name(self) -> str:
        """:return full model name of a car"""
        return self._name + self._model

    def get_name(self) -> str:
        """:return name of transport"""
        return self._name

    @staticmethod
    def get_signal() -> str:
        """:return type of signal"""
        return 'bip'

    @classmethod
    def is_car(cls):
        """class method returns attribute of class"""
        print('Is this Car? ', cls.__isCar)


class Bus(Transport, LicencePlate):
    """Class that represents bus inherited from Transport and LicensePlate"""

    def __init__(self, name: str, color: str, model: str, passengers_amount: int, **kwargs):
        Transport.__init__(self, name, color, model)
        self.passengers_amount = passengers_amount
        LicencePlate.__init__(self, kwargs['series'], kwargs['registration_code'],
                              kwargs['country'])

    def __str__(self):
        """To string method"""
        return "Bus: " + self._name + ", color:" + self._color + \
               ", model:" + self._model + " passengers amount:" + str(self.passengers_amount)

    def get_name(self) -> str:
        """:return name of transport"""
        return self._name

    @staticmethod
    def get_signal() -> str:
        """:return type of signal"""
        return 'bup'


class Motorcycle(Transport, LicencePlate):
    """Class that represents motorcycle inherited from Transport and LicensePlate"""

    def __init__(self, name: str, color: str, model: str, **kwargs):
        Transport.__init__(self, name, color, model)
        LicencePlate.__init__(self, kwargs['series'], kwargs['registration_code'],
                              kwargs['country'])

    def __str__(self):
        """To string method"""
        return "Motorcycle: " + self._name + ", color:" + self._color + \
               ", model:" + self._model

    def get_name(self) -> str:
        """:return name of transport"""
        return self._name

    @staticmethod
    def get_signal() -> str:
        """:return type of signal"""
        return 'buzz'


class Bicycle(Transport):
    """Class that represents bicycle inherited from Transport"""

    def __init__(self, name: str, color: str, model: str, bicycle_type: str):
        super().__init__(name, color, model)
        self._bicycle_type = bicycle_type

    def __str__(self):
        """To string method"""
        return "Bicycle: " + self._name + ", color:" + self._color + \
               ", model:" + self._model + ", type:" + self._bicycle_type

    def get_name(self) -> str:
        """:return name of transport"""
        return self._name

    def get_bycicle_type(self) -> str:
        """:return type of bycicle"""
        return self._bicycle_type

    @staticmethod
    def get_signal() -> str:
        """:return type of signal"""
        return 'dzin'


if __name__ == "__main__":
    nissan_car = Car(name='Nissan Leaf', color='white', model='SV', amount_doors=4,
                     series='AA', registration_code=5867, country='Ukraine')
    nissan_car2 = Car(name='Nissan Leaf222', color='black', model='SV', amount_doors=4,
                      series='AA', registration_code=5867, country='Ukraine')
    lexus_car = Car(name='Lexus', color='white', model='RX 350', amount_doors=4,
                    series='АA', registration_code=5577, country='Ukraine')
    lexus_car2 = Car(name='Lexus', color='white', model='RX 350', amount_doors=4,
                     series='АX', registration_code=5577, country='Ukraine')
    small_car = Car(name='Cherry', color='yellow', model='Kimo S12', amount_doors=2,
                    series='ЛГ', registration_code=6677, country='Ukraine')

    print(nissan_car, end='\n\n')
    print(lexus_car, end='\n\n')
    print(lexus_car2, end='\n\n')

    print(len(lexus_car), end='\n\n')

    print(nissan_car == nissan_car2)
    print(nissan_car == lexus_car, end='\n\n')

    print(lexus_car != lexus_car2)
    print(nissan_car != nissan_car2, end='\n\n')

    print('door' in nissan_car)
    print('door' in small_car)
    print('girl' in small_car, end='\n\n')

    copy_lexus = copy(lexus_car)
    print(copy_lexus, end='\n\n')

    print(lexus_car.full_model_name)
    print(lexus_car.license_plate_number)
    lexus_car.license_plate_number = 6666
    print(lexus_car, end='\n\n')

    Car.is_car()

    print(Car.get_signal())
    print(Bus.get_signal())
    print(Motorcycle.get_signal())
    print(Bicycle.get_signal())
