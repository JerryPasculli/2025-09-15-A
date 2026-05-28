from dataclasses import dataclass
from datetime import datetime


@dataclass
class Nodo:
    driverId: int
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: datetime
    nationality: str
    url: str


    def __hash__(self):
        return hash(self.driverId)

    def __eq__(self, other):
        if other is None:
            return False
        return self.driverId==other.driverId

    def __str__(self):
        return self.driverRef + f"({str(self.driverId)})--DoB:" + str(self.dob)
    def __lt__(self, other):
        return self.dob<other.dob
