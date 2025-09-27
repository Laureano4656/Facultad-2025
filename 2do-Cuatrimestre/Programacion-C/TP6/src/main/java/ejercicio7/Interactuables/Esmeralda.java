package ejercicio7.Interactuables;

public class Esmeralda extends Gema{

    @Override
    public String mezclar(Gema g) {
        return g.mezclarEsmeralda();
    }

    @Override
    public String mezclarEsmeralda() {
        return "Niebla Desoladora";
    }

    @Override
    public String mezclarDiamante() {
        return "Vientos venenosos";
    }

    @Override
    public String mezclarRubi() {
        return "Terremoto";
    }

    @Override
    public String mezclarZafiro() {
        return "Huracan";
    }
}
