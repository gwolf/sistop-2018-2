# 3. Administración de procesos

## Programas ejemplo

1. [Mutex para el cajero automático](./mutex_cajero_automatico.rb)
   ilustrando el uso de un mecanismo de exclusión mutua (_mutex_) para
   proteger la sección crítica.

## Lecturas útiles

1. [Linux Load Averages: Solving the Mystery](http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html):
   Para esta unidad, les pedí que realicen un
   [../../proyectos/1](proyecto de desarrollo de un monitor de
   sistema). Puede resultarles interesante revisar este artículo: ¿Qué
   es la *carga promedio* (*load average*) de un sistema Unix? ¿Qué
   diferencias hay entre lo que se reporta para éste en Linux y en
   otros Unixes?
2. [24-core CPU and I can’t move my mouse](http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)
   explica cómo Bruce Dawson depuró en 2017 un problema aparentemente
   imposible: Teniendo una computadora con 24 núcleos y 64GB de
   memoria, con almacenamiento en una unidad rápida de estado sólido,
   ¿cómo puede explicarse que el sistema está *tan lento* que hasta
   el movimiento del mouse toma varios segundos en reflejarse en
   pantalla?
   
   Les adelanto la respuesta, muy relacionada con lo que vemos hacia
   el principio de esta unidad: Dawson estaba compilando Chrome en
   Windows 10. El proceso de construcción de Chrome busca aprovechar
   el paralelismo al máximo, y lo hace — Pero un comportamiento *no
   documentado* de la finalización de los procesos en Windows 10 llevó
   a una fuerte penalización que lleva a la serialización por la
   espera a un recurso no-paralelizable.
