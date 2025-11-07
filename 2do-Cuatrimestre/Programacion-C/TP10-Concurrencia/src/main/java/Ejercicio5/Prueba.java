package Ejercicio5;

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
        biblioteca.agregarLibro(new Libro(6, "Luiz"));
        biblioteca.agregarLibro(new Libro(7,"Yo soy el arma" ));
        biblioteca.agregarLibro(new Libro(8,"Yo soy la mision" ));
        biblioteca.agregarLibro(new Libro(9,"Yo soy el traidor" ));
        biblioteca.agregarLibro(new Libro(10,"Ready player one" ));


        Libro libroParaDonar1 = new Libro(11, "El Principito");
        Libro libroParaDonar2 = new Libro(12, "El juego infinito");
        Libro libroParaDonar3 = new Libro(13, "Sapiens");
        Libro libroParaDonar4 = new Libro(14, "La sombra del viento");
        Libro libroParaDonar5 = new Libro(15, "El código Da Vinci");
        Thread donador1 = new Thread(new Donador("Donador1", biblioteca, libroParaDonar1));
        Thread donador2 = new Thread(new Donador("Donador2", biblioteca, libroParaDonar2));
        Thread donador3 = new Thread(new Donador("Donador3", biblioteca, libroParaDonar3));
        Thread donador4 = new Thread(new Donador("Donador4", biblioteca, libroParaDonar4));
        Thread donador5 = new Thread(new Donador("Donador5", biblioteca, libroParaDonar5));

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
        donador1.start();
        donador2.start();
        donador3.start();
        donador4.start();
        donador5.start();

//        biblioteca.mostrarLibros();
//        Libro libro = biblioteca.getLibro(3);
//        System.out.println("Libro obtenido: ID = " + libro.getIdLibro() + ", Título = " + libro.getTitulo());
    }
}
