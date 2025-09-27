package ejercicio2;

import ejercicio2.exceptions.DatoInvalido;
import ejercicio2.exceptions.DepositoInvalidoException;
import ejercicio2.exceptions.ExtraccionInvalidaException;

public class CuentaBancaria {
    private double saldo;
    private String titular;

    public CuentaBancaria(String titular){
        this.titular = titular;
        this.saldo = 0.0;
    }
    public double getSaldo() {
        return saldo;
    }
    public String getTitular() {
        return titular;
    }
    public void depositar(double monto) throws DepositoInvalidoException {
        if (monto <= 0) {
            throw new DepositoInvalidoException(monto);
        }
        this.saldo += monto;
    }

    public void extraer(double monto) throws ExtraccionInvalidaException{
        if (monto > this.saldo || monto < 0) {
            throw new ExtraccionInvalidaException(new DatoInvalido(monto, this.saldo));
        }
        this.saldo -= monto;
    }
}
