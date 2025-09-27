package Ejercicio7.Personajes;

import Ejercicio7.Elementos.DecoratorElementoAgua;
import Ejercicio7.Elementos.DecoratorElementoAire;
import Ejercicio7.Elementos.DecoratorElementoFuego;
import Ejercicio7.Elementos.DecoratorElementoTierra;

public class PersonajeFactory {
    public IPersonaje crearPersonaje(String nombre,String clase, String elemento) {
        IPersonaje personaje = null;
        assert nombre != null;
        assert clase != null;
        assert elemento != null;
        personaje = switch (clase.toLowerCase()) {
            case "guerrero" -> new Guerrero(nombre);
            case "hechicera" -> new Hechicera(nombre);
            case "elfo" -> new Elfo(nombre);
            case "dragon" -> new Dragon(nombre);
            case "mago" -> new Mago(nombre);
            default -> throw new IllegalArgumentException("Clase de personaje no válida");
        };
        personaje = switch (elemento.toLowerCase()) {
            case "fuego" -> new DecoratorElementoFuego(personaje);
            case "agua" -> new DecoratorElementoAgua(personaje);
            case "tierra" -> new DecoratorElementoTierra(personaje);
            case "aire" -> new DecoratorElementoAire(personaje);
            default -> throw new IllegalArgumentException("Elemento no válido");
        };
        return personaje;

    }
}
