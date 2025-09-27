package Ejercicio7.Personajes;

public class Hechicera extends Personaje{
    private static final double ARMADURA = 1000;
    private static final double DANIO_ATAQUE_CORTO = 70;
    private static final double DANIO_ATAQUE_LARGO = 50;
    public Hechicera(String nombre){
        super(nombre, ARMADURA, DANIO_ATAQUE_CORTO, DANIO_ATAQUE_LARGO);
    }
}
