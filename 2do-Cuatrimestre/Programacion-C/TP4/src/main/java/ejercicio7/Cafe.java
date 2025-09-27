package ejercicio7;

public class Cafe extends Infusion{
    private boolean dulce;

    public Cafe(boolean dulce) {
        super("Café", 1.0);
        this.dulce = dulce;
    }
    @Override
    public void endulzar() {
        if(dulce) {
            System.out.println("Se agrega azucar a la bebida");
        } else {
            System.out.println("La bebida se tomará amarga");
        }
    }
}
