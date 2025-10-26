package Ejercicio2;

import java.util.Scanner;

public class EsperandoSegundoOperandoState implements State
{
    Calculadora calculadora;

    public EsperandoSegundoOperandoState(Calculadora calculadora)
    {
        this.calculadora = calculadora;

    }

    @Override
    public void esperandoPrimerOperando()
    {

    }

    @Override
    public void esperandoOperador()
    {

    }

    @Override
    public void esperandoSegundoOperando()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el segundo operando: ");
        double segundoOperando = sc.nextDouble();
        calculadora.setSegundoOperando(segundoOperando);
        calculadora.setEstado(new MostrandoResultadoState(calculadora));
    }

    @Override
    public void mostrandoResultado()
    {

    }

    @Override
    public void error()
    {

    }
}
