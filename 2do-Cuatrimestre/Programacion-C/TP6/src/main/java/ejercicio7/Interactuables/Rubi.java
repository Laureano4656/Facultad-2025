package ejercicio7.Interactuables;

public class Rubi extends Gema{

    @Override
    public String mezclar(Gema g) {
        return g.mezclarRubi();
    }

    @Override
    public String mezclarEsmeralda() {
        return "Terremoto";
    }

    @Override
    public String mezclarDiamante() {
        return "Tormenta de rayos";
    }

    @Override
    public String mezclarRubi() {
        return "LLuvia de fuego";
    }

    @Override
    public String mezclarZafiro() {
        return "Erupcion Volcanica";
    }
}
