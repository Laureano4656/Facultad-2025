package Ejercicio7;

import Ejercicio7.Personajes.IPersonaje;
import Ejercicio7.Personajes.Personaje;

import java.util.ArrayList;

public class Mazo {
    private ArrayList<IPersonaje> personajes;
    public Mazo() {
        this.personajes = new ArrayList<>();
    }
    public void agregarPersonaje(IPersonaje personaje) {
        this.personajes.add(personaje);
    }
    public ArrayList<IPersonaje> getPersonajes() {
        return personajes;
    }
    public IPersonaje elijeAdversario(){
        int indice = (int) (Math.random() * personajes.size());
        return personajes.get(indice);
    }
}
