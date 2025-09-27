package ejercicio5;

public class Prueba {

    public static void main(String[] args) {
        Domicilio d1 = new Domicilio("San Martín", 123);
        Persona p1 = new Persona(43508017, "Bautista", d1, new Perro(5, "Firulais"));

        Domicilio d2 = new Domicilio("Belgrano", 456);
        Persona p2 = new Persona(46564934, "Garcia Di Martino", d2, new Gato(3, "Misu"));

        System.out.println("=== Originales ===");
        System.out.println(p1);
        System.out.println(p2);

        System.out.println("\n=== Clonando personas ===");
        Persona copiaP1 = (Persona) p1.clone(); // debería funcionar
        Persona copiaP2 = (Persona) p2.clone(); // debería fallar

        System.out.println("Clon de Juan: " + copiaP1);
        System.out.println("Clon de Ana: " + copiaP2); // debería ser null
    }


}
