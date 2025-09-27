package ejercicio6;

public class Link extends Entidad{
    private Entidad referencia;

    public Link(Entidad referencia) {
        super("Acceso directo a "+referencia.getNombre(), 1);
        this.referencia = referencia;
    }
    @Override
    protected int calcTamanio() {
        return 1;
    }
    @Override
    public String toString() {
        return "Link{" +
                "referencia=" + referencia.getNombre() +
                '}';
    }
}
