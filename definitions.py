from enum import Enum
class RRule(Enum):
    #Define rule relations

    IMB = 5  # "IMB"  # Inclusive match (subset)
    IMP = 4  # "IMP"  # Inclusive match (superset)
    CC = 3  # "CC"  # corrolation
    EM = 2  # "EM"  # exact match
    PD = 1  # "PD"  # partial disjoint
    CD = 0  # "CD"  # complete disjoint

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class RField(Enum):
    #Define field relations

    UNEQUAL = 0
    EQUAL = 1
    SUBSET = 2
    SUPERSET = 3

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Anomaly(Enum):
    #Define anomalies
    AOK = 0  # no anomaly
    SHD = 1  # shadowing
    COR = 2  # corrolation
    RYD = 3  # redundancy: x is a superset of y
    RXD = 4  # redundancy: x is a supset of y
    GEN = 5  # generalization

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
