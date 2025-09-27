package ejercicio5;

public class Persona implements Cloneable, Comparable<Persona> {
    private int DNI;
    private String apellido;
    private Domicilio domicilio;
    private Animal mascota;

    public Persona(int DNI, String apellido, Domicilio domicilio, Animal mascota) {
        this.DNI = DNI;
        this.apellido = apellido;
        this.domicilio = domicilio;
        this.mascota = mascota;
    }


    @Override
    public Object clone() {
        Persona cloned = null;
        try {
            cloned = (Persona) super.clone();
            cloned.domicilio = (Domicilio) this.domicilio.clone();
            cloned.mascota = (Animal) this.mascota.clone();
            return cloned;
        } catch (CloneNotSupportedException e) {
            System.err.println("Clone not supported");
        }
        return null;
    }

    @Override
    public int compareTo(Persona o) {
        int apellidoComparison = this.apellido.compareTo(o.apellido);
        if (apellidoComparison != 0) {
            return apellidoComparison;
        } else {
            return Integer.compare(this.DNI, o.DNI);
        }
    }

    public int getDNI() {
        return DNI;
    }

    public void setDNI(int DNI) {
        this.DNI = DNI;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public Domicilio getDomicilio() {
        return domicilio;
    }

    public void setDomicilio(Domicilio domicilio) {
        this.domicilio = domicilio;
    }

}
