package Ejercicio1.incisoB;

import java.io.IOException;
import java.util.ArrayList;

public class Prueba
{
    public FlotaDTO convertirFlotaAFlotaDTO(Flota flota)
    {
        FlotaDTO flotaDTO = new FlotaDTO();
        flotaDTO.setNombre(flota.getNombre());

        ArrayList<AutomovilDTO> automovilDTOs = new ArrayList<AutomovilDTO>();
        for (Automovil automovil : flota.getAutomoviles())
        {
            AutomovilDTO automovilDTO = new AutomovilDTO();
            automovilDTO.setN_Cashis(automovil.getN_Cashis());
            automovilDTO.setAnioFabricacion(automovil.getAnioFabricacion());
            automovilDTO.setModelo(automovil.getModelo());
            automovilDTO.setMarca(automovil.getMarca());
            automovilDTO.setPatente(automovil.getPatente());

            Motor motor = automovil.getMotor();
            MotorDTO motorDTO = new MotorDTO();
            motorDTO.setN_Serie(motor.getN_Serie());
            motorDTO.setComubstible(motor.getComubstible());

            automovilDTO.setMotor(motorDTO);
            automovilDTOs.add(automovilDTO);
        }
        flotaDTO.setAutomoviles(automovilDTOs);
        return flotaDTO;
    }

    public static void main(String[] args)
    {

        Motor motor = new Motor("MTR456", "Gasolina");
        Automovil automovil = new Automovil("123ABC",2020,"Model S", "Tesla", "XYZ789", motor);
        ArrayList<Automovil> automovils = new ArrayList<Automovil>();
        automovils.add(automovil);
        Flota flota = new Flota("Flota1", automovils);


        PersistenciaXML persistenciaXML = new PersistenciaXML();
        String nombreArchivo = "flota_con_DTO.xml";
        try
        {
            persistenciaXML.abrirOutput(nombreArchivo);
            FlotaDTO flotaDTO = new FlotaDTO();
            flotaDTO.setNombre(flota.getNombre());

            ArrayList<AutomovilDTO> automovilDTOs = new ArrayList<AutomovilDTO>();
            for (Automovil automovil1 : flota.getAutomoviles())
            {
                AutomovilDTO automovilDTO = new AutomovilDTO();
                automovilDTO.setN_Cashis(automovil1.getN_Cashis());
                automovilDTO.setAnioFabricacion(automovil1.getAnioFabricacion());
                automovilDTO.setModelo(automovil1.getModelo());
                automovilDTO.setMarca(automovil1.getMarca());
                automovilDTO.setPatente(automovil1.getPatente());

                Motor motor1 = automovil1.getMotor();
                MotorDTO motorDTO = new MotorDTO();
                motorDTO.setN_Serie(motor1.getN_Serie());
                motorDTO.setComubstible(motor1.getComubstible());

                automovilDTO.setMotor(motorDTO);
                automovilDTOs.add(automovilDTO);
            }
            flotaDTO.setAutomoviles(automovilDTOs);
            persistenciaXML.escribir(flotaDTO);
            persistenciaXML.cerrarOutput();
        } catch (IOException e)
        {
            e.printStackTrace();
        }
    }
}
