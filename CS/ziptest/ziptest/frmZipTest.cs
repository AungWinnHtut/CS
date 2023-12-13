using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;

namespace ziptest
{
    public partial class frmZipTest : Form
    {

        string basic = "7za";
        string archive = " a";
        string extract_archive = " x";
        string password_options = " -p";
        string password = "12345";
        string archive_path = @"  archive.7z";
        string archive_path_options = @"  *.* ";
        string unzip_path = "./unzip";
        string list_archive_option = " l ";
        string compression_options = " -mx=";
        string compression_ratio = "9";
        string encrypt_file_names = " -mhe=";
        string encrypt_file_names_enable = "on";
        string encrypt_file_names_disable = "off";
        string command = "";



        public frmZipTest()
        {
            InitializeComponent();
        }

        private void btnCompress_Click(object sender, EventArgs e)
        {
            command += archive + archive_path + archive_path_options;
            MessageBox.Show(command);
          
          
          
            Process.Start(basic,command);
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnVScode_Click(object sender, EventArgs e)
        {
            Process.Start(@"C:\Users\bluephoenix\AppData\Local\Programs\Microsoft VS Code\Code.exe");
        }
    }
}
