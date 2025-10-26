package Ejercicio1;

public class Prueba
{
    public static void main(String[] args)
    {
        Observador observador = new Observador();
        Mascota mascota1 = new Mascota("Humberto");
        Mascota mascota2 = new Mascota("Archie");
        Mascota mascota3 = new Mascota("Spike");
        Mascota mascota4 = new Mascota("Spot");
        Mascota mascota5 = new Mascota("Buddy");

        observador.agregarObservado(mascota1);
        observador.agregarObservado(mascota2);
        observador.agregarObservado(mascota3);
        observador.agregarObservado(mascota4);
        observador.agregarObservado(mascota5);

        new Thread(mascota1).start();
        new Thread(mascota2).start();
        new Thread(mascota3).start();
        new Thread(mascota4).start();
        new Thread(mascota5).start();
    }
}
