package Ejercicio2;

public class Calculadora
{
    State estado;
    private double primerOperando;
    private double segundoOperando;
    private double resultado;
    private char operacion;

    public Calculadora()
    {
        estado = new EsperandoPrimerOperandoState(this);
    }

    public void esperandoPrimerOperando()
    {
        estado.esperandoPrimerOperando();
    }

    public void esperandoOperador()
    {
        estado.esperandoOperador();
    }

    public void esperandoSegundoOperando()
    {
        estado.esperandoSegundoOperando();
    }

    public void mostrandoResultado()
    {
        estado.mostrandoResultado();
    }

    public void error()
    {
        estado.error();
    }

    public double getPrimerOperando()
    {
        return primerOperando;
    }

    public void setPrimerOperando(double primerOperando)
    {
        this.primerOperando = primerOperando;
    }

    public double getSegundoOperando()
    {
        return segundoOperando;
    }

    public void setSegundoOperando(double segundoOperando)
    {
        this.segundoOperando = segundoOperando;
    }

    public double getResultado()
    {
        return resultado;
    }

    public void setResultado(double resultado)
    {
        this.resultado = resultado;
    }

    public char getOperacion()
    {
        return operacion;
    }

    public void setOperacion(char operacion)
    {
        this.operacion = operacion;
    }

    public void setEstado(State estado)
    {
        this.estado = estado;
    }
}
