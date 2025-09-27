package Ejercicio6.Interactuables;

public class Zafiro extends Gema{

    @Override
    public String mezclar(Gema g) {
        return g.mezclarZafiro();
    }

    @Override
    public String mezclarEsmeralda() {
        return "Huracan";
    }

    @Override
    public String mezclarDiamante() {
        return "Granizo Asesino";
    }

    @Override
    public String mezclarRubi() {
        return "Erupcion Volcanica";
    }

    @Override
    public String mezclarZafiro() {
        return "Inundacion";
    }
}
