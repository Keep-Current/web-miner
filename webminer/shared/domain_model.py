""" Create a DomainModel providing a metaclass"""

from abc import ABCMeta


class DomainModel(metaclass=ABCMeta):
    """An ABC can be subclassed directly, and then acts as a mix-in class
        metaclass (class, optional): Defaults to ABCMeta.
    """

    pass
