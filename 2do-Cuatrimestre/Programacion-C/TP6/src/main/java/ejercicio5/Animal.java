package ejercicio5;

public abstract class Animal {
    private int esperanzaDeVida;
    private String nombre;

    public Animal(int esperanzaDeVida, String nombre) {
        this.esperanzaDeVida = esperanzaDeVida;
        this.nombre = nombre;
    }

    public int getEsperanzaDeVida() {
        return esperanzaDeVida;
    }

    public void setEsperanzaDeVida(int esperanzaDeVida) {
        this.esperanzaDeVida = esperanzaDeVida;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public Object clone() throws  CloneNotSupportedException {
        Animal cloned = null;
        try {
            cloned = (Animal) super.clone();

        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
    }
        return cloned;
    }
}
