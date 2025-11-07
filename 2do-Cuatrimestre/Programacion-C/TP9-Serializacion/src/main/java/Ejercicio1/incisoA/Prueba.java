package Ejercicio1.incisoA;

import java.io.IOException;

public class Prueba
{
    public static void main(String[] args)
    {
        Vehiculo vehiculo = new Vehiculo();
        vehiculo.setN_Cashis("CHS123456");
        vehiculo.setAnioFabricacion(2020);
        Motor motor = new Motor();
        motor.setN_Serie("MTR987654");
        motor.setComubstible("Gasolina");
        Automovil automovil = new Automovil();
        automovil.setModelo("Model S");
        automovil.setMarca("Tesla");
        automovil.setPatente("ABC123");
        automovil.setMotor(motor);
        automovil.setN_Cashis(vehiculo.getN_Cashis());
        automovil.setAnioFabricacion(vehiculo.getAnioFabricacion());
        Flota flota = new Flota();
        flota.getAutomoviles().add(automovil);

        PersistenciaXML persistenciaXML = new PersistenciaXML();
        String nombreArchivo = "flota.xml";
        try
        {
            persistenciaXML.abrirOutput(nombreArchivo);
            persistenciaXML.escribir(flota);
            persistenciaXML.cerrarOutput();
        } catch (IOException e)
        {
            e.printStackTrace();
        }
    }
}
