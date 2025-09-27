package Ejercicio6.Personajes;

import Ejercicio6.Posicion;

public class Caballero extends Personaje {
    private static final double danio = 10;
    private static final double distanciaAtaque = 10;

    public Caballero(String nombre, Posicion posicion) {
        super(nombre, 500, posicion, danio, distanciaAtaque);
    }
    @Override
    public void serBendecido(){
        this.setVitalidad(this.getVitalidad()*1.25);
    }
    @Override
    public void serMaldito(){
        this.setVitalidad(this.getVitalidad()*0.50);
    }
}
