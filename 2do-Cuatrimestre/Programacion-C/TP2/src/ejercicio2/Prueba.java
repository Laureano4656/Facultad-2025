package ejercicio2;

public class Prueba {	

	public static void main(String[] args) {
		Punto p1 = new Punto(2,3);
		Punto p2;
		//Punto p3 = new Punto(); //no existe el constructor vacio
		System.out.println("P1="+p1.cartel());
		//p3=p2; // p3 no puede referenciar a lo mismo que p2 ya que p2 no referencia a nada
		p2=p1;
		p1.cambia(8,5);
		System.out.println("P2="+p2.cartel()); //es lo mismo que hacer p1.cartel()
		}

	}

