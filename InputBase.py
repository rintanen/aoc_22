from abc import ABCMeta, abstractmethod
from functools import cached_property

class InputBase(metaclass=ABCMeta):
    def __init__(self, input_path):
        self.input_path = input_path

    @cached_property
    def raw_input(self):
        with open(self.input_path, 'r') as f:
            return f.readlines()

    @abstractmethod
    def read_task_input(self):
        """ to be implemented in each task """
        pass