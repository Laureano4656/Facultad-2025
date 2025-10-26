package Ejercicio2;

import java.util.Scanner;

public class EsperandoPrimerOperandoState implements State
{
    Calculadora calculadora;

    public EsperandoPrimerOperandoState(Calculadora calculadora)
    {
        this.calculadora = calculadora;

    }

    @Override
    public void esperandoPrimerOperando()
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el primer operando: ");
        double primerOperando = sc.nextDouble();
        calculadora.setPrimerOperando(primerOperando);
        calculadora.setEstado(new EsperandoOperadorState(calculadora));
    }

    @Override
    public void esperandoOperador()
    {

    }

    @Override
    public void esperandoSegundoOperando()
    {

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
