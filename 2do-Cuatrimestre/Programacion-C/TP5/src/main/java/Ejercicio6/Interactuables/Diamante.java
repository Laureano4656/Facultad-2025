package Ejercicio6.Interactuables;

public class Diamante extends Gema{

    @Override
    public String mezclar(Gema g) {
        return g.mezclarDiamante();
    }

    @Override
    public String mezclarEsmeralda() {
        return "Vientos venenosos";
    }

    @Override
    public String mezclarDiamante() {
        return "Congelamiento";
    }

    @Override
    public String mezclarRubi() {
        return "Tormenta de rayos";
    }

    @Override
    public String mezclarZafiro() {
        return "Granizo Asesino";
    }
}
