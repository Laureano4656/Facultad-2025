package Ejercicio2;

public interface State
{
    void esperandoPrimerOperando();
    void esperandoOperador();
    void esperandoSegundoOperando();
    void mostrandoResultado();
    void error();
}
