using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using add; // Referencia del web service
 
namespace add
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
 
  private void button1_Click(object sender, EventArgs e)
        {
            String usuario = "ccalix@finkok.com.mx"; // Usuario de Finkok
            String password = "Legoland1953!"; // Contraseña de Finkok
            String RFC = "AAD990814BP7"; // RFC del cliente que se desea agregar
 
            // Instancias del web service
            add.add  ws = new add.add ();
            add.RegistrationSOAP SoapAdd = new add.RegistrationSOAP();
            add.addResponse respuesta = new add.addResponse();
 
            // Envio de párametros al web service 
            ws.reseller_username = usuario;
            ws.reseller_password = password;
            ws.taxpayer_id = RFC;
 
            // Obtener respuesta del web service
            respuesta = SoapAdd.add(ws);
 
            // Imprimir respuesta del web service en un mensaje 
            MessageBox.Show(respuesta.addResult.message);
 
        }
 
        private void Form1_Load(object sender, EventArgs e)
        {
 
        }
    }
}