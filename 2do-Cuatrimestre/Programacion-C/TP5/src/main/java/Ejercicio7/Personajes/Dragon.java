package Ejercicio7.Personajes;

public class Dragon extends Personaje{
    private static final double ARMADURA = 1500;
    private static final double DANIO_ATAQUE_CORTO = 500;
    private static final double DANIO_ATAQUE_LARGO = 200;
    public Dragon(String nombre){
        super(nombre, ARMADURA, DANIO_ATAQUE_CORTO, DANIO_ATAQUE_LARGO);
    }
}
