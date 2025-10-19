package ejercicio1.Personajes;

import ejercicio1.Exceptions.ExceptionAtaqueImposible;
import ejercicio1.Exceptions.ExceptionIncrementoImposible;
import ejercicio1.Hechizable;
import ejercicio1.Movible;
import ejercicio1.Posicion;
import ejercicio1.Posicionable;

public abstract class Personaje implements Movible, Posicionable, Hechizable, Comparable<Personaje>,Cloneable {
    private String nombre;
    private double vitalidad;
    private Posicion posicion;
    private double danioAtaque;
    private double distanciaAtaque;
    private double distanciaMaximaDesplazamiento;
    public Personaje(String nombre, int vitalidad, Posicion posicion, double danioAtaque, double distanciaAtaque, double distanciaMaximaDesplazamiento) {
        this.nombre = nombre;
        this.vitalidad = vitalidad;
        this.posicion = posicion;
        this.danioAtaque = danioAtaque;
        this.distanciaAtaque = distanciaAtaque;
        this.distanciaMaximaDesplazamiento = distanciaMaximaDesplazamiento;
    }

    @Override
    public Posicion getPosicion() {
        return posicion;
    }

    @Override
    public void setPosicion(Posicion p) {
        this.posicion = p;
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

    public String getNombre() {
        return nombre;
    }

    public void atacar(Personaje p) throws ExceptionAtaqueImposible {
        if (!( this.posicion.distancia(p.getPosicion()) <= distanciaAtaque)) {
            throw new ExceptionAtaqueImposible("Ataque imposible, fuera de rango", this, p);
        }
        p.recibirDanio(danioAtaque);
    }

    public void recibirDanio(double danio) {
        this.vitalidad -= danio;
        if (this.vitalidad < 0) this.vitalidad = 0;
    }

    public double getVitalidad() {
        return vitalidad;
    }

    public void setVitalidad(double vitalidad) {
        this.vitalidad = vitalidad;
    }

    @Override
    public double getPosX() {
        return posicion.getPosX();
    }

    @Override
    public double getPosY() {
        return posicion.getPosY();
    }

    @Override
    public void incrementaPosicion(double dx, double dy) throws ExceptionIncrementoImposible{
        double distancia = Math.sqrt(dx*dx + dy*dy);
        if (distancia > distanciaMaximaDesplazamiento) {
            throw new ExceptionIncrementoImposible("Incremento de posicion imposible", distanciaMaximaDesplazamiento, distancia);
        }
        this.posicion.incrementaPosicion(dx, dy);
    }
    @Override
    public int compareTo(Personaje o) {
        if (this.nombre.compareTo(o.getNombre()) != 0) {
            return this.nombre.compareTo(o.getNombre());
        } else {
            return Double.compare(o.getVitalidad(), this.vitalidad);
        }
    }
    @Override
    public double distancia(Movible m) {
        return posicion.distancia(m);
    }

    @Override
    public Object clone() {
        Personaje p = null;
        try {
            p = (Personaje) super.clone();
            p.posicion = new Posicion(this.posicion.getPosX(), this.posicion.getPosY());
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
            p = null;
        }
        return p;
    }
}
