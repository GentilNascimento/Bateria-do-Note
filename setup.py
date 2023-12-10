from cx_Freeze import setup, Executable

executables = [Executable('app.py')]

setup(
    name='Bateria do Note',
    version='1.0',
    description='Sempre que a bateria do Notebook atingir 98% da carga toca o mp3, avisando p desligar a fonte',
    executables=executables,
    options={
        'build_exe': {
            'include_files': ['saxN.mp3']   
        }
    }
)
 
