from cx_Freeze import setup, Executable
 
setup(
 name="BASC",
 version="1.0",
 descriptiom="Algoritmo BASC",
 executables = [Executable("main.py")],
 )
