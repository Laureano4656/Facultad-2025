package Ejercicio7.Elementos;

import Ejercicio7.Personajes.IPersonaje;

public class DecoratorElementoFuego extends DecoratorElemento{
    public DecoratorElementoFuego(IPersonaje personaje) {
        super(personaje);
    }
    @Override
    public double getArmadura(){
        return super.getArmadura() * 0.50;
    }
    @Override
    public double getAtaqueCorto(){
        return super.getAtaqueCorto() * 1.80;
    }
    @Override
    public double getAtaqueLargo(){
        return super.getAtaqueLargo() * 1.70;
    }
    public String Incendiar(){
        return "El personaje ha incendiado a su enemigo";
    }
}
