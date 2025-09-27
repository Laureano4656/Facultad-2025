package Ejercicio7.Elementos;

import Ejercicio7.Personajes.IPersonaje;

public class DecoratorElementoTierra extends DecoratorElemento{
    public DecoratorElementoTierra(IPersonaje personaje) {
        super(personaje);
    }
    @Override
    public double getArmadura() {
        return super.getArmadura() * 1.25;
    }
    @Override
    public double getAtaqueCorto() {
        return super.getAtaqueCorto() * 0.8;
    }
    @Override
    public double getAtaqueLargo() {
        return super.getAtaqueLargo() * 0.7;
    }
}
