package Ejercicio7.Personajes;

public class Guerrero extends Personaje{
    private static final double ARMADURA = 1500;
    private static final double DANIO_ATAQUE_CORTO = 100;
    private static final double DANIO_ATAQUE_LARGO = 100;
    public Guerrero(String nombre){
        super(nombre, ARMADURA, DANIO_ATAQUE_CORTO, DANIO_ATAQUE_LARGO);
    }
}
