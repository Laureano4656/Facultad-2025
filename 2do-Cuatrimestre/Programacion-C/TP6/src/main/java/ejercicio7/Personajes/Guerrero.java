package ejercicio7.Personajes;

import ejercicio7.Posicion;

public class Guerrero extends Personaje{
    private static final double danio = 10;
    private static final double distanciaAtaque = 5;
    private static final double distanciaMaximaDesplazamiento = 5;
    private double armadura;
    public Guerrero(String nombre, Posicion posicion, double armadura) {
        super(nombre, 800, posicion, danio, distanciaAtaque, distanciaMaximaDesplazamiento);
        this.armadura = armadura;
    }

    @Override
    public void recibirDanio(double danio) {
        super.recibirDanio(danio - armadura);
    }
    @Override
    public void serBendecido(){
        this.armadura +=200;
    }
    public void serMaldito(){
        this.armadura -=200;
        if(this.armadura <0) this.armadura =0;
    }
}
