package ejercicio5;

public class ColectivoLargaDistancia extends Colectivo {
    private boolean cocheCama;

    public ColectivoLargaDistancia(String modelo, int cantidadPasajeros, boolean cocheCama) {
        super(modelo, cantidadPasajeros);
        this.cocheCama = cocheCama;
    }
    @Override
    public boolean aceptoChofer(Chofer chofer) {
        return chofer.getCategoria().getHabilitaColectivoLarga();
    }
    @Override
    public String toString() {
        return "ColectivoLargaDistancia{" +
                "cocheCama=" + cocheCama +
                "} " + super.toString();}
}
