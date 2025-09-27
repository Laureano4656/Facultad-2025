package Ejercicio6.Personajes;

import Ejercicio6.Posicion;

public class Arquero extends Personaje {
    private static final double danioFlechas = 15;
    private static final double danioCuerpoACuerpo = 5;
    private static final double distanciaAtaqueFlechas = 100;
    private static final double distanciaAtaqueCuerpo = 5;
    private int flechas;

    public Arquero(String nombre, Posicion posicion, int flechas) {
        super(nombre, 300, posicion, danioFlechas, distanciaAtaqueFlechas);
        this.flechas = flechas;
    }
    public void recargarFlechas(int cantidad) {
        assert cantidad > 0 : "La cantidad de flechas a recargar debe ser positiva";
        this.flechas += cantidad;
    }
    @Override
    public boolean atacar(Personaje p){
        assert p!= null : "El personaje a atacar no puede ser nulo";
        if (flechas > 0) {
            flechas--;
        } else {
            super.setDanioAtaque(danioCuerpoACuerpo);
            super.setDistanciaAtaque(distanciaAtaqueCuerpo);
        }
        return super.atacar(p);
    }
    @Override
    public void serBendecido(){
        this.flechas += 5;
    }
    @Override
    public void serMaldito(){
        this.flechas = 0;
    }
}
