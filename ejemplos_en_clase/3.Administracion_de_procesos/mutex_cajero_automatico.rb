#!/usr/bin/ruby
# coding: utf-8
class CajeroAutomatico
  def initialize
  end
  def identifica(x)
    puts "Identificando al usuario %s" % x.nombre
    sleep 0.1
  end
  def dame_dinero(x, num)
    puts "Le doy $%d a %s" % [num, x.nombre]
    sleep 0.1
  end
  def dame_saldo(x)
    puts "Le doy su saldo a %s" % x.nombre
    sleep 0.1
  end
end

class Persona
  attr_accessor :nombre
  def initialize(nombre)
    @nombre = nombre
  end
  def usa_cajero(cajero)
    cajero.identifica(self)
    cajero.dame_saldo(self) if rand > 0.5
    cajero.dame_dinero(self, rand*500) if rand > 0.4
  end
end

hilos = []
mutex = Mutex.new
c = CajeroAutomatico.new
%w(José Pedro María Juan Gonzalo).each do |nombre|
  hilos << Thread.new do
    p = Persona.new(nombre)
    mutex.lock
    p.usa_cajero(c)
    mutex.unlock
  end
end

hilos.each {|hilo| hilo.join}
