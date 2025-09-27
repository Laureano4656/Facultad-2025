package ejercicio3;

public class CuentaBancaria {
	private double saldo;
	private String titular;
	
	public CuentaBancaria(String titular) {
		this.titular = titular;
		this.saldo = 0;
	}
	public void depositar(double monto)
	{
		if (monto>0)
			this.saldo +=monto;
	}
	public boolean extraer(double monto)
	{
		if (monto >= 0 && monto-this.saldo >= 0)
		{
			this.saldo -=monto;
			return true;
		}
		else
			return false;
	}
	public double getSaldo() {
		return saldo;
	}
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	public String getTitular() {
		return titular;
	}
	public void setTitular(String titular) {
		this.titular = titular;
	}
	
}
