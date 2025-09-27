package ejercicio7;

import ejercicio7.Exceptions.ExceptionIncrementoImposible;

public interface Movible {
    double getPosX();
    double getPosY();
    void incrementaPosicion(double dx, double dy) throws ExceptionIncrementoImposible;
    double distancia(Movible m);
}
