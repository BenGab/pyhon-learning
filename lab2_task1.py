#!/usr/bin/env python3
import weakref
from collections import Sequence


class Person(Sequence):
    __slots__ = ("__name", "__age", "__gender")

    persons = []
    __len__ = persons.__len__

    def __init__(self, name, gender, age=0):
        self.__name = name
        self.__age = age
        self.__gender = gender
        Person.persons.append(weakref.ref(self))

    def __del__(self):
        for person in Person.persons:
            if person is None:
                Person.persons.remove(person)

    def __setName(self, name):
        if (str.upper(self.__name) == str.upper(name)):
            self.__name = name
        else:
            raise AttributeError("Changin name is not allowed")

    def __getName(self):
        return self.__name

    name = property(__getName, __setName)

    def __getitem__(self, index):
        p = Person.persons[index]
        if p:
            return p

        return None

    def __str__(self):
        return self.__name + " " + self.__age + " " + self.__gender

    def __cmp__(self, other):
        return cmp(self.name, other.name)

    def __add__(self, other):
        self.__age += other

    @staticmethod
    def printAll():
        for p in Person.persons:
            print(p)

class Gender(object):
    def __get__(self, instance, owner):
        return instance._gender

    def __set__(self, instance, value):
        if str.upper(value) in ("MALE","FEMALE", "OTHER"):
            instance._gender = str.upper(value)
        else:
            raise AttributeError("Value is invalid")