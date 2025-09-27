package Ejercicio4;

public class Posicion implements Movible {
    private double x;
    private double y;

    public Posicion(double x, double y) {
        this.x = x;
        this.y = y;
    }
    @Override
    public double getPosX() {
        return x;
    }
    @Override
    public double getPosY() {
        return y;
    }
    @Override
    public void setXY(double x,double y) {
        this.x = x;
        this.y = y;
    }
    @Override
    public void incrementaPosicion(double dx, double dy) {
        this.x += dx;
        this.y += dy;
    }
    public double distancia(Movible m) {
        return Math.sqrt(Math.pow(this.x - m.getPosX(), 2) + Math.pow(this.y - m.getPosY(), 2));
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
