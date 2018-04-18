# 4. Administración de memoria

#### Programas ejemplo ####

1. Para explicar los diferentes momentos del proceso de *resolución de
   direcciones* (en *tiempo de compilación*, en *tiempo de carga* y en
   *tiempo de ejecución*), en clase hicimos un sencillo programa que
   consta de tres archivos: [ligado.c](./ligado.c),
   [ligado2.c](./ligado2.c) y [ligado.h](./ligado.h). Es un ejemplo mínimo
   de un programa para cuya ejecución (./la función `main()` está en
   `ligado.c`) algunas de las funciones son provistas por un archivo
   externo (`ligado2.c`).

   Compilamos estos archivos indicándole a `gcc` que guarde los
   archivos temporales, y le preguntamos al sistema qué es cada uno de
   los archivos generados:

        $ gcc -save-temps ligado.c ligado2.c -o ligado
		$ file ligado*
		ligado2.c: C source, ASCII text
		ligado2.h: ASCII text
		ligado2.i: C source, ASCII text
		ligado2.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
		ligado2.s: assembler source, ASCII text
		ligado.c:  C source, UTF-8 Unicode text
		ligado.i:  C source, UTF-8 Unicode text
		ligado.o:  ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
		ligado.s:  assembler source, ASCII text

	Tenemos entonces:

	1. Nuestros archivos fuente [ligado.c](./ligado.c) y
       [ligado2.c](./ligado2.c), así como el archivo de encabezados
       [ligado2.h](./ligado2.h).
    2. Los archivos *preprocesados* (esto es, tras resolver los
       *macros* y la biblioteca estándar de C), [ligado.i](./ligado.i) y
       [ligado2.i](./ligado2.i).
    3. Nuestro programa ya *compilado* pero aún no ensamblado — El
       último paso que, como humanos y con cierta habilidad, podemos
       leer y comprender: [ligado.s](./ligado.s) y
       [ligado2.s](./ligado2.s)
    4. Los *módulos objeto*, [ligado.o](./ligado.o) y
       [ligado2.o](./ligado2.o), compilados y ensamblados, pero aún no
       ligados.
    5. El programa completo como un solo binario, [ligado](./ligado)

	Agrego aquí, por conveniencia, el *volcado* de hexadecimal a
    formato textual (realizado con `hexdump -C`) de los últimos tres:
    [ligado.o.dump](./ligado.o.dump),
    [ligado2.o.dump](./ligado2.o.dump) y [ligado.dump](./ligado.dump).

2. Al entrar al tema de *paginación*, hicimos un programita llamado
   [asignando.c](./asignando.c), que muestra el funcionamiento de
   `malloc()` sobre la sección de libres: Cada medio segundo, el
   programa solicita la asignación (mediante `malloc(sizeof(int))`) de
   un entero (4 bytes).

   Ejecutamos este programa (`./a.out`), y desde otra terminal
   lanzamos `watch -n 0.2 pmap $(pidof a.out)` (¿qué hace esta línea?
   `pidof a.out` entrega el ID del proceso en que se ejecuta `a.out`;
   `$(…)` captura el resultado de ese comando y lo pasa como
   argumento a `pmap`, que presenta el mapa de memoria del proceso
   especificado, y mediante `watch` ejecutamos esto cada ⅕ de segundo)

   Vean cómo crece la sección de libres — La sección anónima más baja
   en la memoria.
