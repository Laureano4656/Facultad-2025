package Ejercicio6;

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

        biblioteca.agregarRevista(new Revista(1, "National Geographic"));
        biblioteca.agregarRevista(new Revista(2, "Time"));
        biblioteca.agregarRevista(new Revista(3, "Forbes"));
        biblioteca.agregarRevista(new Revista(4, "Vogue"));
        biblioteca.agregarRevista(new Revista(5, "Scientific American"));
        biblioteca.agregarRevista(new Revista(6, "The New Yorker"));
        biblioteca.agregarRevista(new Revista(7, "Wired"));

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

        SocioLibro socio1 = new SocioLibro("Ana", biblioteca);
        SocioLibro socio2 = new SocioLibro("Luis", biblioteca);
        SocioLibro socio3 = new SocioLibro("Marta", biblioteca);
        SocioLibro socio4 = new SocioLibro("Carlos", biblioteca);
        SocioLibro socio5 = new SocioLibro("Sofía", biblioteca);
        SocioLibro socio6 = new SocioLibro("Javier", biblioteca);
        SocioLibro socio7 = new SocioLibro("Lucía", biblioteca);
        SocioLibro socio8 = new SocioLibro("Diego", biblioteca);
        SocioLibro socio9 = new SocioLibro("Elena", biblioteca);
        SocioLibro socio10 = new SocioLibro("Miguel", biblioteca);

        SocioRevista socioRevista1 = new SocioRevista("Sofía Revista", biblioteca);
        SocioRevista socioRevista2 = new SocioRevista("Javier Revista", biblioteca);
        SocioRevista socioRevista3 = new SocioRevista("Lucía Revista", biblioteca);
        SocioRevista socioRevista4 = new SocioRevista("Diego Revista", biblioteca);
        SocioRevista socioRevista5 = new SocioRevista("Elena Revista", biblioteca);
        SocioRevista socioRevista6 = new SocioRevista("Miguel Revista", biblioteca);
        SocioRevista socioRevista7 = new SocioRevista("Ana Revista", biblioteca);

//
        new Thread(socio1).start();
        new Thread(socio2).start();
        new Thread(socio3).start();
        new Thread(socio4).start();
        new Thread(socio5).start();
        new Thread(socio6).start();
        new Thread(socio7).start();
        new Thread(socio8).start();
        new Thread(socio9).start();
        new Thread(socio10).start();

        new Thread(socioRevista1).start();
        new Thread(socioRevista2).start();
        new Thread(socioRevista3).start();
        new Thread(socioRevista4).start();
        new Thread(socioRevista5).start();
        new Thread(socioRevista6).start();
        new Thread(socioRevista7).start();

        donador1.start();
        donador2.start();
        donador3.start();
        donador4.start();
        donador5.start();

    }
}
