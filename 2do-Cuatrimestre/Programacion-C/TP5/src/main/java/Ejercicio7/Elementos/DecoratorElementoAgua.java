package Ejercicio7.Elementos;

import Ejercicio7.Personajes.IPersonaje;

public class DecoratorElementoAgua extends DecoratorElemento{
    public DecoratorElementoAgua(IPersonaje personaje) {
        super(personaje);
    }
    @Override
    public double getArmadura(){
        return super.getArmadura() * 0.85;
    }
    @Override
    public double getAtaqueCorto(){
        return super.getAtaqueCorto() * 1.20;
    }
    @Override
    public double getAtaqueLargo(){
        return super.getAtaqueLargo();
    }

}
