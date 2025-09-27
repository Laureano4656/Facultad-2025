package Ejercicio6.Personajes;

import Ejercicio6.Hechizable;
import Ejercicio6.Movible;
import Ejercicio6.Posicion;
import Ejercicio6.Posicionable;

public abstract class Personaje implements Movible, Posicionable, Hechizable {
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

    public boolean atacar(Personaje p) {
        if (this.posicion.distancia(p.getPosicion()) <= distanciaAtaque) {
            p.recibirDanio(danioAtaque);
            return true;
        }
        return false;
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
    public void setXY(double x, double y) {
        posicion.setXY(x, y);
    }

    @Override
    public void incrementaPosicion(double dx, double dy) {
        posicion.incrementaPosicion(dx, dy);
    }

    @Override
    public double distancia(Movible m) {
        return posicion.distancia(m);
    }
}
