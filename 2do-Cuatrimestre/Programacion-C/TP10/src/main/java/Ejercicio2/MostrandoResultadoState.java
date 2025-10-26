package Ejercicio2;

import java.util.Scanner;

public class MostrandoResultadoState implements State
{
    Calculadora calculadora;

    public MostrandoResultadoState(Calculadora calculadora)
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

    }

    @Override
    public void mostrandoResultado()
    {
        Scanner sc = new Scanner(System.in);
        char igual;
        do {
            System.out.print("Presione '=' para mostrar el resultado: ");
            igual = sc.next().charAt(0);
        } while (igual != '=');
        double resultado = 0;
        switch (calculadora.getOperacion())
        {
            case '+':
                resultado = calculadora.getPrimerOperando() + calculadora.getSegundoOperando();
                break;
            case '-':
                resultado = calculadora.getPrimerOperando() - calculadora.getSegundoOperando();
                break;
            case '*':
                resultado = calculadora.getPrimerOperando() * calculadora.getSegundoOperando();
                break;
            case '/':
                if (calculadora.getSegundoOperando() != 0)
                {
                    resultado = calculadora.getPrimerOperando() / calculadora.getSegundoOperando();
                }
                else
                {
                    System.out.println("Error: División por cero.");
                    calculadora.setEstado(new ErrorState(calculadora));
                    return;
                }
                break;
            default:
                System.out.println("Error: Operador inválido.");
                calculadora.setEstado(new ErrorState(calculadora));
                return;
        }
        System.out.println("El resultado es: " + resultado);
        calculadora.setEstado(new EsperandoPrimerOperandoState(calculadora));
    }

    @Override
    public void error()
    {

    }
}
