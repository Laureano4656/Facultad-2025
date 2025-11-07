package Ejercicio4;

public class Prueba
{
    public static void main(String[] args)
    {
        Biblioteca biblioteca = new Biblioteca();
        biblioteca.agregarLibro(new Libro(1, "Cien años de soledad"));
        biblioteca.agregarLibro(new Libro(2, "Don Quijote de la Mancha"));
        biblioteca.agregarLibro(new Libro(3, "La Odisea"));
        biblioteca.agregarLibro(new Libro(4, "Hamlet"));
        biblioteca.agregarLibro(new Libro(5, "1984"));

        Socio socio1 = new Socio("Ana", biblioteca);
        Socio socio2 = new Socio("Luis", biblioteca);
        Socio socio3 = new Socio("Marta", biblioteca);
        Socio socio4 = new Socio("Carlos", biblioteca);
        Socio socio5 = new Socio("Sofía", biblioteca);
        Socio socio6 = new Socio("Javier", biblioteca);
        Socio socio7 = new Socio("Lucía", biblioteca);
        Socio socio8 = new Socio("Diego", biblioteca);
        Socio socio9 = new Socio("Elena", biblioteca);
        Socio socio10 = new Socio("Miguel", biblioteca);
//
        socio1.start();
        socio2.start();
        socio3.start();
        socio4.start();
        socio5.start();
        socio6.start();
        socio7.start();
        socio8.start();
        socio9.start();
        socio10.start();

//        biblioteca.mostrarLibros();
//        Libro libro = biblioteca.getLibro(3);
//        System.out.println("Libro obtenido: ID = " + libro.getIdLibro() + ", Título = " + libro.getTitulo());
    }
}
