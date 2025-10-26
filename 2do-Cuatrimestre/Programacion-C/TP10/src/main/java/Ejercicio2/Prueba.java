package Ejercicio2;

public class Prueba
{
    public static void main(String[] args)
    {
        Calculadora calculadora = new Calculadora();

        calculadora.esperandoPrimerOperando();
        calculadora.esperandoOperador();
        calculadora.esperandoSegundoOperando();
        calculadora.mostrandoResultado();
    }
}
