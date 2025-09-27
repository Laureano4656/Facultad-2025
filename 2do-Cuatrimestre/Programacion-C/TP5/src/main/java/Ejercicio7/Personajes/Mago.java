package Ejercicio7.Personajes;

public class Mago extends Personaje{
    private static final double ARMADURA = 500;
    private static final double DANIO_ATAQUE_CORTO = 50;
    private static final double DANIO_ATAQUE_LARGO = 70;
    public int prueba = 2;
    public Mago(String nombre){
        super(nombre, ARMADURA, DANIO_ATAQUE_CORTO, DANIO_ATAQUE_LARGO);
    }
}
