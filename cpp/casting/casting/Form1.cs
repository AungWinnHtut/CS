using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace casting
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnCalculate_Click(object sender, EventArgs e)
        {
            float fRadius = float.Parse(txtRadius.Text);
            float Area = 3.14F * fRadius * fRadius;
            txtArea.Text = Area.ToString();

            char c = 'A';
            int data = (int)c;

            string number = "1234";
            int no = 1234;

        }
    }
}
