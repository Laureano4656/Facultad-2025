package Ejercicio7;

import java.util.ArrayList;

public class Prueba
{
    public static void main(String[] args)
    {

        ArrayList<Persona> personas = new ArrayList<>();
        Bote bote = new Bote(2, personas); // Bote con capacidad para 2 personas
        // Crear personas que quieren ir a la orilla derecha (true) o izquierda (false)
        Persona p1 = new Persona("Persona 1", bote, true);
        Persona p2 = new Persona("Persona 2", bote, true);
        Persona p3 = new Persona("Persona 3", bote, true);
        Persona p4 = new Persona("Persona 4", bote, true);
        Persona p5 = new Persona("Persona 5", bote, false);
        Persona p6 = new Persona("Persona 6", bote, false);
        personas.add(p1);
        personas.add(p2);
        personas.add(p3);
        personas.add(p4);
        personas.add(p5);
        personas.add(p6);
        // Iniciar hilos para cada persona
        new Thread(p1).start();
        new Thread(p2).start();
        new Thread(p3).start();
        new Thread(p4).start();
        new Thread(p5).start();
        new Thread(p6).start();
    }
}
