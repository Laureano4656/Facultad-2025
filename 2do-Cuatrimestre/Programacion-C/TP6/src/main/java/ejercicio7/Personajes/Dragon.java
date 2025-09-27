package ejercicio7.Personajes;

import ejercicio7.Posicion;

public class Dragon extends Personaje{
    private final static double poderDeFuegoInicial = 100;
    private static final double distanciaAtaque = 50;
    private static final double distanciaMaximaDesplazamiento = 20;
    private double poderDeFuego = poderDeFuegoInicial;

    public Dragon(String nombre, Posicion posicion) {
        super(nombre, 1000, posicion, poderDeFuegoInicial, distanciaAtaque, distanciaMaximaDesplazamiento);
    }
    @Override
    public void serBendecido(){
        this.setDanioAtaque(this.getDanioAtaque()*1.40);
        this.setVitalidad(this.getVitalidad() + 250);
    }
    @Override
    public void serMaldito(){
        this.setDanioAtaque(this.getDanioAtaque()*0.70);
        this.setVitalidad(this.getVitalidad()*0.8);
    }
}
