package Ejercicio2;

import java.util.Scanner;

public class EsperandoOperadorState implements State
{
    Calculadora calculadora;

    public EsperandoOperadorState(Calculadora calculadora)
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
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el operador (+, -, *, /): ");
        char operador = sc.next().charAt(0);
        calculadora.setOperacion(operador);
        calculadora.setEstado(new EsperandoSegundoOperandoState(calculadora));
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
