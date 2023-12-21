using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinForm1
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private void btnSingin_Click(object sender, EventArgs e)
        {
            string sUsername = txtUname.Text;
            string sPass = txtPass.Text;
            if(sUsername == "admin" &&  sPass == "1234")
            {
                MessageBox.Show("Logging in!!");
                frmUnitConverter frmmUnitConverter = new frmUnitConverter();
                frmmUnitConverter.Show();
                this.Hide();
            }
            else
            {
                MessageBox.Show("Wrong!!");
            }
        }
    }
}
