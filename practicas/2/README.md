# Depuración por trazas

    Práctica creada el 20.02.2018
	Entrega: 27.02.2018

Para afianzar el tema de _excepciones, interrupciones y llamadas al
sistema_, les propongo el siguiente ejercicio: Encontrar qué pasos
sigue la ejecución de un programa sin contar con su código fuente.

Lo que van a hacer es, de cierto modo, equiparable a una _ingeniería
inversa de caja negra_: Usar un programa que intercepte las llamadas
al sistema que efectúe su programa, y de esa manera averiguar qué
servicios le está pidiendo al sistema operativo. Pueden revisar una
muy (tal vez demasiado) breve explicación en las
[láminas 32 y 33 de la presentación](http://gwolf.sistop.org/laminas/03-relacion-con-el-hardware.pdf#page=32)
o en la
[sección 2.7.1 del libro](http://sistop.org/pdf/sistemas_operativos.pdf)).

Esta práctica consiste en realizar algo similar a lo que demostré en
clase. Esto es:

- Elijan un programa _sencillo_, y _tracen_ su ejecución. Ojo: Trazar
  la ejecución de un programa con interfaz gráfica es muy complejo;
  desenterrar la lógica del programa de entre todos los elementos
  gráficos y de eventos es casi imposible. Busquen algo que puedan
  ejecutar desde su línea de comando.
    - En Linux, con `strace`. En MacOS, pueden usar `ktrace` o
      `dtrace`.
    - En Windows hay muchos programas, aunque hasta donde puedo
      entender, ninguno viene preinstalado por default. Me encontré
      con el [Dr. Memory Framework](http://drmemory.org/), que dice
      tener un _Strace for Windows_.
    - Obviamente, si encuentran otra herramienta, ¡bienvenida!
- La salida de la ejecución probablemente va a ser _muy_
  grande. Hagan una revisión rápida a ojo para buscar una región
  interesante, y elijan unas _15 llamadas consecutivas_ en que se
  quieran enfocar
    - En clase les mostré que hay una sección que constituye el inicio
      de puesta en marcha del programa; abordaremos parte de esta
      lógica en el transcurso del curso. En el ejemplo que presento en
      el libro (el de las láminas está muy recortado), esta comprende
      aproximadamente hasta la línea 25. **Ignoren este primer
      pedazo**, me interesa que se enfoquen en la lógica del proceso
      en cuestión (no en su inicialización.
    - _Ojo:_ No hace falta que detallen las 15 llamadas una tras
      otra. Si tenemos grupos de llamadas relacionadas, ahórrense el
      describir a cada una de ellas. Hay llamadas obvias y aburridas,
      como `close` o `munmap` que no requieren profundizar.
    - Intenten limitarse a programas sencillos: Programas que hagan su
      entrada/salida desde la línea de comando, que efectúen alguna
      tarea sencilla. Puede ser un programa escrito por ustedes,
      listar el contenido de un directorio (en Linux, `ls`), obtener
      la fecha (`date`), obtener el directorio actual (`pwd`), o algo
      por el estilo.
- Expliquen qué comprenden o qué intuyen de esa porción de la
  ejecución.
    - ¿Línea por línea? ¿Explicando grupos de llamadas? De ustedes
      depende

## Instrucciones de entrega

- Esta práctica es para entrega individual.
- La entrega se hará por Git, siguiendo el esquema de directorios
  especificado en el
  [punto 4 de la práctica 1](https://github.com/gwolf/sistop-2018-2/blob/master/practicas/1/README.md),
  y se considera entregado en el momento en que generen el _pull
  request_ correspondiente.
- Pueden entregar un documento de texto, un archivo PDF, las
  fotografías de pantallazos impresos y anotados en pluma, _como les
  acomode realizar esta práctica_.
- Deben indicar:
    - En qué sistema operativo trabajaron
    - Qué programa emplearon para obtener la traza
    - Qué programa objetivo trazaron
        - ¿Por qué eligieron este programa?
		- Si es un programa hecho por ustedes, me gustaría ver el
          código fuente ☺
	- Sus observaciones / resultados

## Recursos adicionales

- En sistemas Unix, recuerden la máxima: _man es tu amigo_. Si quieren
  saber qué hace una llamada al sistema, revisen la sección 2 del
  manual. Esto es, del ejemplo anterior: Si quieren saber qué hace
  `fstat`, basta con que escriban desde la terminal `man 2 fstat`, y
  el título de la página les indica `get file status` — Obtiene la
  información acerca de determinado archivo.
    - Claro está, pueden seguir leyendo el texto de la página para
      comprender qué significan los argumentos que recibe y los
      códigos de retorno que entrega.
- Si les interesa revisar una página del manual y no tienen un sistema
  Unix a la mano, pueden entrar a
  [Debian Manpages](https://manpages.debian.org/) y obtener la misma
  información para un sistema Debian
    - Con las ligas en la parte derecha de la pantalla pueden
      consultar las secciones y páginas relacionadas
- Las herramientas de traza son muchas veces importantes bloques de
  construcción para diferentes tareas de monitoreo. Pueden referirse
  por ejemplo a
  [Top 10 DTrace scripts for MacOS X](http://dtrace.org/blogs/brendan/2011/10/10/top-10-dtrace-scripts-for-mac-os-x/)
  como un ejemplo de cómo se obtiene esta información en MacOS
- La página de manual de `strace` les presenta cómo afinar sus
  consultas, obtener datos totalizados, ver cuánto tiempo toma cada
  llamada al sistema, etc. Pueden jugar con esta salida
  también. ¿Encontraron algo interesante especificando estas opciones?

## Algunas respuestas a los alumnos

Algunos de ustedes me dejaron varios comentarios abiertos en la tarea,
aparentemente esperando mi respuesta. ¡Muy bien! No los dejaré con la
palabra en la boca. En órden alfabético,

- [Alejandro Espejel](EspejelAlejandro/Practica2): Muy bueno. Sí,
  sería ridículo que yo les pidiera entrar al nivel de detalle que
  presentaste en *todas* las llamadas. Cubre perfectamente lo que
  buscábamos.

- [Juan Flores](./FloresJuan/practica2.pdf): Bien. Sí, hay muchos
  puntos pendientes de revisar. Y no, no vamos a cubrirlos todos. Pero
  si tienes curiosidad, `man` es tu amigo :-]

- [Marcos López](./LopezMarcos/Practica2.pdf): No entregaste la
  práctica correctamente, no subiste el archivo (¿sólo una referencia
  a él?)

- [Rubén Lozano](LozanoRuben/practica2.txt): Buen reporte. Buenas
  conclusiones. Un par de interpretaciones erróneas, pero no podría yo
  exigir que comprendan todo lo que pasa a ese nivel (yo no lo
  lograría).

- [Ernesto Ochoa](./OchoaLuis/practica_2.pdf): ¡Muy buen e interesante
  reporte! Me gustaría ver un poco más la salida de `dtrace`. Pero me
  gusta cómo te enfrentaste con el error y lo resolviste.

- [Andrew Sánchez](./SanchezAndrew/DepuracionPorTraza.odt): Buen
  trabajo. Preguntas respecto a `fstat64` y `lstat64` — Ambas
  funciones te dan información general de los metadatos
  respectivamente de un archivo y de una *liga simbólica*; ya luego
  abordamos a detalle el qué y el por qué de estas llamadas. Lo
  importante de que sean la versión `64` es el tamaño máximo de
  archivos que soportan los sistemas de archivo actuales: En un
  sistema de archivos puro de 32 bits, sería complicado representar el
  tamaño de un archivo de más de 4GB (2³² bits). Preguntas también
  respecto a `getrlimit`; esta es una llamada que le pregunta al
  sistema operativo respecto a los límites de ejecución que tiene el
  usuario actual (particularmente, uso de memoria, número máximo de
  archivos abiertos y procesos en ejecución, etc.)

- [Eduardo Tolentino](./TolentinoEduardo/P2.pdf): Entrega
  muy tardía, no puedo ya darte puntos por ella ☹. Reporte correcto,
  aunque mencionas únicamente cuatro llamadas utilizadas (aunque, sí,
  el programa las realiza varias veces).

- [Eduardo Valdez](./ValdezEduardo/Practica_02.pdf): ¡Ojo! Por lo que
  mencionas, parecería que entiendes que cada una de las cadenas
  mostradas (p.ej. `init     Create an empty Gi"...`) invoca a la
  función en cuestión. ¡No! La llamada en todos estos casos es un
  `write` al descriptor de archivos `1`, esto es, es la "ayuda corta"
  de Git mostrándote cómo puede ser invocado. Pero son únicamente
  cadenas enviadas a la terminal.
