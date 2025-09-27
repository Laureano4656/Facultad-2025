package ejercicio8;

public abstract class Personaje {
    private String nombre;
    private double vitalidad;
    private Posicion posicion;
    private double danioAtaque;
    private double distanciaAtaque;

    public Personaje(String nombre, int vitalidad, Posicion posicion, double danioAtaque, double distanciaAtaque) {
        this.nombre = nombre;
        this.vitalidad = vitalidad;
        this.posicion = posicion;
        this.danioAtaque = danioAtaque;
        this.distanciaAtaque = distanciaAtaque;
    }
    public Posicion getPosicion() {
        return posicion;
    }
    public void setDanioAtaque(double danioAtaque) {
        this.danioAtaque = danioAtaque;
    }
    public double getDanioAtaque() {
        return danioAtaque;
    }
    public void setDistanciaAtaque(double distanciaAtaque) {
        this.distanciaAtaque = distanciaAtaque;
    }
    public double getDistanciaAtaque() {
        return distanciaAtaque;
    }
    public boolean atacar(Personaje p){
        if (this.posicion.distancia(p.getPosicion()) <= distanciaAtaque) {
            p.recibirDanio(danioAtaque);
            return true;
        }
        return false;
    }

    public void recibirDanio(double danio){
        this.vitalidad -= danio;
        if (this.vitalidad < 0) this.vitalidad = 0;
    };
}
