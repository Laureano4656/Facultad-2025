package Ejercicio1;

public interface IMonitor
{
    Via via = new Via();
    void entrar(int miDireccion) throws InterruptedException;
    void salir(int miDireccion);
}
