using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BeginnerSpecial3
{
    public partial class frmGame : Form
    {
        public frmGame()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnCheck_Click(object sender, EventArgs e)
        {

            lstHobby.Items.Clear();
            if( chkFootball.Checked == true )
            {
                lstHobby.Items.Add("FootBall");
            }
            if (chkReading.Checked == true)
            {
                lstHobby.Items.Add("Reading");
            }
            if (chkSwimming.Checked == true)
            {
                lstHobby.Items.Add("Swimming");
            }



        }

        private void btnCalculate_Click(object sender, EventArgs e)
        {
            // 1. read data from txtRadius (Text)
            string sRadius = txtRadius .Text;
            // 2. convert string to float
            float fRadius = float.Parse(sRadius);
            // 3. calculate area using A = 3.14 * R * R;
            float A;
            A = 3.14F * fRadius * fRadius; //F means float
            // 4. convert answer A to string
            string sArea = A.ToString();
            // 5. show answer A string to txtArea (Text)
            txtArea.Text = sArea;
        }
    }
}
