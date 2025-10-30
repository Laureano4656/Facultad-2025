package Ejercicio2;

public class Prueba
{
    public static void main(String[] args)
    {
        Mostrador mostrador = new Mostrador(3);
        Thread persona1 = new Thread(new Persona(1, mostrador));
        Thread persona2 = new Thread(new Persona(2, mostrador));
        Thread persona3 = new Thread(new Persona(3, mostrador));

        persona1.start();
        persona2.start();
        persona3.start();


    }
}
