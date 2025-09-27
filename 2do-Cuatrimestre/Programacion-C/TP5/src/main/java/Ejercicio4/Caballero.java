package Ejercicio4;

public class Caballero extends Personaje {
    private static final double danio = 10;
    private static final double distanciaAtaque = 10;

    public Caballero(String nombre, Posicion posicion) {
        super(nombre, 500, posicion, danio, distanciaAtaque);
    }

}
