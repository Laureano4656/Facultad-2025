package ejercicio2;

public class Punto {

	private int x;
	private int y;
	public Punto(int x, int y)
	{
	this.x = x;
	this.y = y;
	}
	public void cambia(int x1,int y1)
	{
	setX(x1);
	setY(y1);
	}
	public int getX() {
		return x;
	}
	public void setX(int x) {
		this.x = x;
	}
	public int getY() {
		return y;
	}
	public void setY(int y) {
		this.y = y;
	}
	public String cartel()
	{return"Punto[x="+x+",y="+y+"]";}

}
