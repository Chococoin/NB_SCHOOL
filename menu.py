import argparse
import json
import os
import sys

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# menu.py

#-------------------------------------------------------------------- Constantes
LIMPIAR = "clear" if sys.platform.startswith("linux") else "cls"

#------------------------------------------------------------------------ Clases
class Menu(object) :
    """Lista de funciones opcionales, las cuales le permitirán al usuario
    realizar operaciones matemáticas básicas.

    Argumentos
        prompt -- Es el prompt del menú (default '>')
    """

    def __init__(self, prompt=">") :
        self.prompt = prompt + " "
        self.opciones = [
            self.insert_new,
            self.view_all,
            self.edit_one,
            self.delete_one,
            self.exit,
        ]
        self.presentacion = "------------------ PhoneBook ------------------\n"

        for numero, opcion in enumerate(self.opciones, 1) :
            self.presentacion += "{0}. {1}\n".format(numero, opcion.__name__[7:])

    def loop(self) :
        while True:
            print (self.presentacion)

            try:
                seleccion = int(input(self.prompt))

                if seleccion >= 1 and seleccion < len(self.opciones) :
                    op1, op2 = self.pedir_operandos()
                    # Los indices van desde 0 hasta len(self.opciones)-1
                    resultado = self.opciones[seleccion - 1](op1, op2)
                    input("\nEl resultado es {0}".format(resultado))

                # Caso especial para la opción "salir"
                elif seleccion == len(self.opciones) :
                    self.opciones[seleccion - 1]()

                else:
                    input("Error: Opción invalida")

            except ValueError:
                input("Error: Debes introducir un número")

            except ZeroDivisionError:
                input("Acaso quieres destruir el universo!?")

            except KeyboardInterrupt:
                break

            os.system(LIMPIAR)

    def pedir_operandos(self) :
        while True:
            print("Por favor, ingrese el primer operando")

            try:
                op1 = int(input(self.prompt))
            except ValueError:
                print("Error: Debes introducir un número\n")
            else:
                break

        while True:
            print("Por favor, ingrese el segundo operando")

            try:
                op2 = int(input(self.prompt))
            except ValueError:
                print("Error: Debes introducir un número\n")
            else:
                break

        return op1, op2

    def insert_new(self, op1, op2) :
        return op1 + op2

    def view_all(self, op1, op2) :
        return op1 - op2

    def edit_one(self, op1, op2) :
        return op1 * op2

    def delete_one(self, op1, op2) :
        return op1 / op2

    def exit(self) :
        # Aquí podría ir un mensaje de despedida
        raise KeyboardInterrupt()