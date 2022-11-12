En este repositorio se encuentra documentada la informacion referente
al frameword slash y el uso de los fixtures para la relizacion de pruebas.

-Instale las librerias necesarias que se encuentran en el source SLASH-AND-FIXTURES/Requirements/requirements.txt

Tips

# comandos con slash

Available commands:
list
list-config
list-plugins
rerun
resume
run
version

# Consola sin color

slash run .\1-slash-introduction.py -v -v -v --no-color

# Consola con los colores correctos

slash run .\1-slash-introduction.py -v -v -v --force-color -l C:\Users\julio\OneDrive\Documentos\Cesar\Slash-and-fixtures\Slash\sessions

# Opciones para ejecutar los test(slash list)

slash list [options] PATH... [-h] [-f SUITE_FILES] [--only-fixtures] [--only-tests] [--show-tags] [--no-params]
[--allow-empty] [--warnings-as-errors] [-r] [-k FILTER] [--no-output] [--force-color]  
 [--no-color] [--show-duplicates]
[PATH ...]
