# coding: utf8
'''
Created on 28 ����. 2018 �.

@author: Aleksandr.Muga
'''
from cx_Freeze import setup, Executable

setup( 
    name = "MainProgramm",
    version = "1.0",
    description = "Description of the app here.",
    executables = Executable("passwordgen.py")
    )