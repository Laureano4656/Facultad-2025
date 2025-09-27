package Ejercicio7;

import Ejercicio7.Personajes.IPersonaje;
import Ejercicio7.Personajes.Mago;
import Ejercicio7.Personajes.PersonajeFactory;

public class Prueba {
    public static void main(String[] args){
        // Crear personajes
        PersonajeFactory factory = new PersonajeFactory();
        Mazo mazo = new Mazo();
        IPersonaje merlin = factory.crearPersonaje("Merlin","Mago","Agua");
        mazo.agregarPersonaje(factory.crearPersonaje("Licht","Elfo","Aire"));
        mazo.agregarPersonaje(factory.crearPersonaje("Guts","Humano","Tierra"));
        mazo.agregarPersonaje(factory.crearPersonaje("Gon","Humano","Agua"));
        mazo.agregarPersonaje(factory.crearPersonaje("Naruto","Humano","Fuego"));
        mazo.agregarPersonaje(factory.crearPersonaje("Sasuke","Humano","Fuego"));
        mazo.agregarPersonaje(factory.crearPersonaje("Zoro","Humano","Agua"));
        mazo.agregarPersonaje(factory.crearPersonaje("Ichigo","Humano","Aire"));
        mazo.agregarPersonaje(factory.crearPersonaje("Asta","Humano","Tierra"));

    }
}
