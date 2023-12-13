using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace KaraokeTest
{
    public partial class frmKaraoke : Form
    {
        public frmKaraoke()
        {
            InitializeComponent();
        }

        private void btnMp3Play_Click(object sender, EventArgs e)
        {
            player.URL = "music.mp3";

        }

        private void btnMp3Pause_Click(object sender, EventArgs e)
        {
            player.Ctlcontrols.pause();
        }

        private void btnMp3Stop_Click(object sender, EventArgs e)
        {
            player.Ctlcontrols.stop();
        }

        private void btnMp4Play_Click(object sender, EventArgs e)
        {
            player.URL = "cartoon.mp4";
        }

        private void btnMp4Pause_Click(object sender, EventArgs e)
        {
            player.Ctlcontrols.pause();
        }

        private void btnMp4Stop_Click(object sender, EventArgs e)
        {
            player.Ctlcontrols.stop();
        }

        private void btnMplayer_Click(object sender, EventArgs e)
        {
            // Define the path to the MPlayer executable
            string mplayerPath = @"mplayer.exe";

            // Define the path to the video file you want to play
            string videoFilePath = @"cartoon.mp4";

            try
            {
                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = mplayerPath,
                    Arguments = $"\"{videoFilePath}\" -ni",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    CreateNoWindow = true
                };

                Process mplayerProcess = new Process { StartInfo = psi };
                mplayerProcess.Start();

                // Optionally, you can wait for MPlayer to finish
                mplayerProcess.WaitForExit();

                // Check the exit code to see if MPlayer encountered an error
                int exitCode = mplayerProcess.ExitCode;
                if (exitCode != 0)
                {
                    Console.WriteLine($"MPlayer exited with error code {exitCode}");
                    // Handle the error as needed
                }

                mplayerProcess.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
                // Handle the exception as needed
            }
        }
    }
    }

