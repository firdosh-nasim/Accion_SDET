# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:45:03 2018

@author: firdo
"""


class WorkForce(object):
    """
    Class: WorkForce: This is the base for all types workers

    Attributes:
        __count: Class attribute to hold the total count of workers

        first_name: First name of the worker
        last_name: Last name of the worker
        pay_rate: Hourly pay rate of worker
        yearly_vacation: Amount of yearly vacation. 0 for Temporary & Contract 
                        employees

    Methods:
        get_count(): Static method. Returns the count of total work force

        get_name(): Returns the name(first_name & last_name) of worker
        get_pay_rate(): Returns the pay rate of the worker
        get_yearly_vacation(): Returns the number of vacation days of worker

    """

    # Class variable
    __count = 0

    # Initializer
    def __init__(self, first_name, last_name, pay_rate, yearly_vacation):
        self.first_name = first_name
        self.last_name = last_name
        self.pay_rate = pay_rate
        self.yearly_vacation = yearly_vacation
        WorkForce.__count += 1

    def get_name(self):
        """
        Returns the name(first_name & last_name) of worker
        """
        return f"{self.last_name}, {self.first_name}"

    def get_pay_rate(self):
        """
        Returns the pay rate of the worker
        """
        return self.pay_rate

    def get_yearly_vacation(self):
        """
        Returns the pay rate of the worker
        """
        return self.yearly_vacation

    @staticmethod
    def get_count():
        """
        Static method. Returns the count of total work force
        """
        return WorkForce.__count


class Employee(WorkForce):
    """
    Class: Employee: This is the Employee class, inherited from WorkForce 
                    base class

    Attributes:
        __count: Class attribute to hold the total count of employees

        first_name: First name of the employee
        last_name: Last name of the employee
        pay_rate: Hourly pay rate of employee
        yearly_vacation: Amount of yearly vacation.

    Methods:
        get_count(): Static method. Returns the count of total employees

    """

    # Class variable
    __count = 0

    # Initializer
    def __init__(self, first_name, last_name, pay_rate, yearly_vacation):
        WorkForce.__init__(self, first_name, last_name, pay_rate, yearly_vacation)

        Employee.__count += 1

    @staticmethod
    def get_count():
        """
        Static method. Returns the count of total employees
        """
        return Employee.__count


class Contractor(WorkForce):
    """
    Class: Contractor: This is the Contractor class, inherited from WorkForce 
                      base class

    Attributes:
        __count: Class attribute to hold the total count of Contractor

        first_name: First name of the Contractor
        last_name: Last name of the Contractor
        pay_rate: Hourly pay rate of Contractor
        yearly_vacation: Amount of yearly vacation. Defaults to 0
        agency_name: Name of the contracting agency

    Methods:
        get_count(): Static method. Returns the count of total Contractor

        get_name(): Returns the name(first_name & last_name) of Contractor
        get_agency(): Returns the name of contract agency

    """

    # Class variable
    __count = 0

    # Initializer
    def __init__(self, first_name, last_name, pay_rate, agency_name, yearly_vacation=0):
        WorkForce.__init__(self, first_name, last_name, pay_rate, yearly_vacation)
        self.agency_name = agency_name
        Contractor.__count += 1

    def get_name(self):
        """
        Returns the name contract employee
        """
        return f"{super(Contractor, self).get_name()} [C]"

    def get_agency(self):
        """
        Returns the name of contract agency
        """
        return self.agency_name

    @staticmethod
    def get_count():
        """
        Static method. Returns the count of contract employees
        """
        return Contractor.__count


class Temporary(WorkForce):
    """
    Class: Temporary: This is the Temporary class, inherited from WorkForce 
                     base class

    Attributes:
        __count: Class attribute to hold the total count of Temporary

        first_name: First name of the Temporary
        last_name: Last name of the Temporary
        pay_rate: Hourly pay rate of Temporary
        yearly_vacation: Amount of yearly vacation. Defaults to 0
        agency_name: Name of the contracting agency

    Methods:
        get_count(): Static method. Returns the count of total Temporary

        get_name(): Returns the name(first_name & last_name) of Temporary
        get_agency(): Returns the name of Temporary agency

    """
    # Class variable
    __count = 0

    # Initializer
    def __init__(self, first_name, last_name, pay_rate, agency_name, yearly_vacation=0):
        WorkForce.__init__(self, first_name, last_name, pay_rate, yearly_vacation)
        self.agency_name = agency_name
        Temporary.__count += 1

    def get_name(self):
        """
        Returns the name temporary employee
        """
        return f"{super(Temporary, self).get_name()} [T]"

    def get_agency(self):
        """
        Returns the name of temp agency
        """
        return self.agency_name

    @staticmethod
    def get_count():
        """
        Static method. Returns the count of total temporary employees
        """
        return Temporary.__count


# Driver code
if __name__ == "__main__":

    print(" Working with Temporary class ".center(80, '*'))

    # Instantiate 2 temporary employees
    t1 = Temporary(first_name='t1First', last_name='t1Last', pay_rate=100, agency_name='HireTemp1')
    t2 = Temporary(first_name='t2First', last_name='t2Last', pay_rate=110, agency_name='HireTemp1')

    # Fetch the details
    print(f"Name of t1: \"{t1.get_name()}\"")
    print(f"Pay rate of t2: {t2.get_pay_rate()}")
    print(f"Vacation days of t1: {t1.get_yearly_vacation()}")
    print(f"Agency name of t2: {t1.get_agency()}")
    print(f"Number of temporary employees: {Temporary.get_count()}")

    print('*' * 80)

    print(" Working with Contractor class ".center(80, '*'))

    # Instantiate 3 contractors
    c1 = Contractor(first_name='c1First', last_name='c1Last', pay_rate=500, agency_name='HireContractor1')
    c2 = Contractor(first_name='c2First', last_name='c2Last', pay_rate=550, agency_name='HireContractor1')
    c3 = Contractor(first_name='c3First', last_name='c3Last', pay_rate=650, agency_name='HireContractor2')

    # Fetch the details
    print(f"Name of c1: \"{c1.get_name()}\"")
    print(f"Pay rate of c2: {c2.get_pay_rate()}")
    print(f"Vacation days of c3: {c3.get_yearly_vacation()}")
    print(f"Agency name of c1: {c1.get_agency()}")
    print(f"Number of contractors: {Contractor.get_count()}")

    print('*' * 80)

    print(" Working with Employee class ".center(80, '*'))

    # Instantiate 5 employees
    e1 = Employee(first_name='e1First', last_name='e1Last', pay_rate=1500, yearly_vacation=20)
    e2 = Employee(first_name='e2First', last_name='e2Last', pay_rate=1600, yearly_vacation=20)
    e3 = Employee(first_name='e3First', last_name='e3Last', pay_rate=1650, yearly_vacation=20)
    e4 = Employee(first_name='e4First', last_name='e4Last', pay_rate=1750, yearly_vacation=20)
    e5 = Employee(first_name='e5First', last_name='e5Last', pay_rate=1850, yearly_vacation=25)

    # Fetch the details
    print(f"Name of e1: \"{e1.get_name()}\"")
    print(f"Pay rate of e2: {e2.get_pay_rate()}")
    print(f"Vacation days of e3: {e3.get_yearly_vacation()}")
    print(f"Number of employees: {Employee.get_count()}")
    print('*' * 80)

    print(" Working with Base Class WorkForce ".center(80, '*'))
    print(f"Total number of workers: {WorkForce.get_count()}")
    print('*' * 80)