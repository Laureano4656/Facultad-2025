package ejercicio7;

public class Mate extends Infusion{

    public Mate() {
        super("Mate", 1.5);
    }

    @Override
    public void endulzar() {
        System.out.println("La bebida se tomará amarga");
    }

}
