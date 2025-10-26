package Ejercicio2;

public class ErrorState implements State
{
    Calculadora calculadora;

    public ErrorState(Calculadora calculadora)
    {
        this.calculadora = calculadora;

    }

    public void esperandoPrimerOperando()
    {

    }

    public void esperandoOperador()
    {

    }

    public void esperandoSegundoOperando()
    {

    }

    public void mostrandoResultado()
    {

    }

    public void error()
    {
        System.out.println("La calculadora está en estado de error. Reinicie para continuar.");
    }
}
