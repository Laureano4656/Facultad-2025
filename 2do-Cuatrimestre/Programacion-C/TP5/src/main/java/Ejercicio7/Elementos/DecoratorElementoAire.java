package Ejercicio7.Elementos;

import Ejercicio7.Personajes.IPersonaje;

public class DecoratorElementoAire extends DecoratorElemento{
    public DecoratorElementoAire(IPersonaje personaje) {
        super(personaje);
    }
    @Override
    public double getArmadura(){
        return super.getArmadura() * 0.9;
    }
    @Override
    public double getAtaqueCorto(){
        return super.getAtaqueCorto() * 1.20;
    }
    @Override
    public double getAtaqueLargo(){
        return super.getAtaqueLargo() * 1.10;
    }
    public String invocarHuracan(){
        return "El personaje ha invocado un huracán que arrasa con todo a su paso";
    }
}
