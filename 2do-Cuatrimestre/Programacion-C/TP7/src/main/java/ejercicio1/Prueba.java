package ejercicio1;

import java.util.*;

public class Prueba
{
    public static void main(String[] args)
    {
        Persona[] personas = new Persona[5];

        Persona p1 = new Persona();
        p1.setApellido("Perez");
        p1.setNombre("Carlos");
        p1.setDireccion("Colon 3212");
        personas[0] = p1;

        Persona p2 = new Persona();
        p2.setApellido("Perez");
        p2.setNombre("Carlos");
        p2.setDireccion("Colon 3212");
        personas[1] = p2;

        Persona p3 = new Persona();
        p3.setApellido("Garcia");
        p3.setNombre("Ana");
        p3.setDireccion("Mitre 2812");
        personas[2] = p3;

        Persona p4 = new Persona();
        p4.setApellido("Alvarez");
        p4.setNombre("Valeria");
        p4.setDireccion("San Luis 2812");
        personas[3] = p4;

        Persona p5 = new Persona();
        p5.setApellido("Garcia");
        p5.setNombre("Luis");
        p5.setDireccion("Matheu 3538");
        personas[4] = p5;

        System.out.println("Antes de ordenar:");
        for (Persona persona : personas)
        {
            System.out.println(persona.getApellido() + ", " + persona.getNombre());
        }
        if (personas[0] == personas[1])
        {
            System.out.println("\nSon el mismo objeto");
        }
        else
        {
            System.out.println("\nNo son el mismo objeto");
        }
        Ordenadora.ordenar(personas);

        System.out.println("\nDespués de ordenar:");
        for (Persona persona : personas)
        {
            System.out.println(persona.getApellido() + ", " + persona.getNombre());
        }
        HashSet<Persona> set = new HashSet<Persona>();
        set.add(p1);
        set.add(p2);
        set.add(p3);
        set.add(p4);
        set.add(p5);

        // use of iterator
        Iterator<Persona> it = set.iterator();
        while (it.hasNext())
        {
            Persona p = it.next();
            System.out.println("\n Apellido: " + p.getApellido() + ", Nombre: " + p.getNombre());
        }

        System.out.println("\n Usando LinkedHashSet: \n");
        LinkedHashSet<Persona> set2 = new LinkedHashSet<Persona>();
        set2.add(p1);
        set2.add(p2);
        set2.add(p3);
        set2.add(p4);
        set2.add(p5);

        // use of iterator
        Iterator<Persona> it2 = set2.iterator();
        while (it2.hasNext())
        {
            Persona p = (Persona) it2.next();
            System.out.println("\n Apellido: " + p.getApellido() + ", Nombre: " + p.getNombre());
        }

        System.out.println("\n TreeSet: \n");

        TreeSet<Persona> set3 = new TreeSet<Persona>();

        set3.add(p1);
        set3.add(p2);
        set3.add(p3);
        set3.add(p4);
        set3.add(p5);
        // use of iterator
        Iterator<Persona> it3 = set3.iterator();
        while (it3.hasNext())
        {
            Persona p = it3.next();
            System.out.println("\n Apellido: " + p.getApellido() + ", Nombre: " + p.getNombre());
        }

        System.out.println("\n Usando ArrayList: \n");

        ArrayList<Persona> set4 = new ArrayList<Persona>();
        set4.add(p1);
        set4.add(p2);
        set4.add(p3);
        set4.add(p4);
        set4.add(p5);
        // use of iterator
        Iterator<Persona> it4 = set4.iterator();
        while (it4.hasNext())
        {
            Persona p = (Persona) it4.next();
            System.out.println("\n Apellido: " + p.getApellido() + ", Nombre: " + p.getNombre());
        }

        System.out.println("\n Usando LinkedList: \n");

        LinkedList<Persona> set5 = new LinkedList<Persona>();
        set5.add(p1);
        set5.add(p2);
        set5.add(p3);
        set5.add(p4);
        set5.add(p5);
        // use of iterator
        Iterator<Persona> it5 = set5.iterator();
        while (it5.hasNext())
        {
            Persona p = (Persona) it5.next();
            System.out.println("\n Apellido: " + p.getApellido() + ", Nombre: " + p.getNombre());
        }

        System.out.println("\n Usando PrioirtyQueue: \n");
        PriorityQueue<Persona> set6 = new PriorityQueue<Persona>();
        set6.add(p1);
        set6.add(p2);
        set6.add(p3);
        set6.add(p4);
        set6.add(p5);
        // metodo poll
        while (!set6.isEmpty())
        {
            Persona p = set6.poll();
            System.out.println("\n Apellido: " + p.getApellido() + ", Nombre: " + p.getNombre());
        }
    }
}
