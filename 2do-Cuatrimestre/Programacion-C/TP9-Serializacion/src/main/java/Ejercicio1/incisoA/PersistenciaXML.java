package Ejercicio1.incisoA;

import java.beans.XMLDecoder;
import java.beans.XMLEncoder;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.Serializable;

public class PersistenciaXML
{
    private XMLEncoder xmlEncoder;
    private XMLDecoder xmlDecoder;
    private FileOutputStream fileoutput;
    private FileInputStream fileinput;

    public void abrirInput(String nombre) throws IOException
    {
        fileinput = new FileInputStream(nombre);
        xmlDecoder = new XMLDecoder(fileinput);

    }
    public void abrirOutput(String nombre) throws IOException
    {
        fileoutput = new FileOutputStream(nombre);
        xmlEncoder = new XMLEncoder(fileoutput);
    }
    public void cerrarOutput() throws IOException
    {
        xmlEncoder.close();
        fileoutput.close();
    }
    public void cerrarInput() throws IOException
    {
        xmlDecoder.close();
        fileinput.close();
    }
    public void escribir(Object objeto) throws IOException
    {
        xmlEncoder.writeObject(objeto);

    }
    public Object leer() throws IOException, ClassNotFoundException
    {
        Object objecto = null;
        if (xmlDecoder != null)
            objecto = (Serializable) xmlDecoder.readObject();

        return objecto;
    }
}
