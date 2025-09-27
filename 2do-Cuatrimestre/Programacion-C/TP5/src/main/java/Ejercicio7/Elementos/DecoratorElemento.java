package Ejercicio7.Elementos;

import Ejercicio7.Personajes.IPersonaje;

public class DecoratorElemento implements IPersonaje {
    protected IPersonaje personaje;

    public DecoratorElemento(IPersonaje personaje) {
        this.personaje = personaje;
    }

    @Override
    public String getNombre() {
       return personaje.getNombre();
    }

    @Override
    public double getAtaqueCorto() {
        return personaje.getAtaqueCorto();
    }

    @Override
    public double getAtaqueLargo() {
        return personaje.getAtaqueLargo();
    }

    @Override
    public double getArmadura() {
        return personaje.getArmadura();
    }
}
