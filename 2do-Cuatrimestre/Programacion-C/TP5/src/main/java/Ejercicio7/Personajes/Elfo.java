package Ejercicio7.Personajes;

public class Elfo extends  Personaje {
    private static final double ARMADURA = 100;
    private static final double DANIO_ATAQUE_CORTO = 20;
    private static final double DANIO_ATAQUE_LARGO = 100;
    public Elfo(String nombre){
        super(nombre, ARMADURA, DANIO_ATAQUE_CORTO, DANIO_ATAQUE_LARGO);
    }
}
