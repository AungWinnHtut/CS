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
    public partial class frmUnitConverter : Form
    {
        public frmUnitConverter()
        {
            InitializeComponent();
        }

        private void frmUnitConverter_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
        }

        private void btnConvert_Click(object sender, EventArgs e)
        {
            string sInches = txtInches.Text;      
            float fInches = float.Parse(sInches);
            float fCm = 0.0F;
            fCm =  fInches* 2.54F;
            txtCm.Text = fCm .ToString();
           
        }
    }
}
