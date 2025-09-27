package Ejercicio4;

public interface Movible {
    double getPosX();
    double getPosY();
    void setXY(double x, double y);
    void incrementaPosicion(double dx, double dy);
    double distancia(Movible m);
}
