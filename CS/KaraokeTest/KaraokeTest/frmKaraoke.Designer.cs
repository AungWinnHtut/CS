namespace KaraokeTest
{
    partial class frmKaraoke
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmKaraoke));
            this.btnMp3Play = new System.Windows.Forms.Button();
            this.btnMp3Pause = new System.Windows.Forms.Button();
            this.btnMp3Stop = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.btnMp4Play = new System.Windows.Forms.Button();
            this.btnMp4Pause = new System.Windows.Forms.Button();
            this.btnMp4Stop = new System.Windows.Forms.Button();
            this.player = new AxWMPLib.AxWindowsMediaPlayer();
            this.btnMplayer = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.player)).BeginInit();
            this.SuspendLayout();
            // 
            // btnMp3Play
            // 
            this.btnMp3Play.Location = new System.Drawing.Point(24, 16);
            this.btnMp3Play.Name = "btnMp3Play";
            this.btnMp3Play.Size = new System.Drawing.Size(107, 37);
            this.btnMp3Play.TabIndex = 1;
            this.btnMp3Play.Text = "Play";
            this.btnMp3Play.UseVisualStyleBackColor = true;
            this.btnMp3Play.Click += new System.EventHandler(this.btnMp3Play_Click);
            // 
            // btnMp3Pause
            // 
            this.btnMp3Pause.Location = new System.Drawing.Point(145, 17);
            this.btnMp3Pause.Name = "btnMp3Pause";
            this.btnMp3Pause.Size = new System.Drawing.Size(119, 35);
            this.btnMp3Pause.TabIndex = 2;
            this.btnMp3Pause.Text = "Pause";
            this.btnMp3Pause.UseVisualStyleBackColor = true;
            this.btnMp3Pause.Click += new System.EventHandler(this.btnMp3Pause_Click);
            // 
            // btnMp3Stop
            // 
            this.btnMp3Stop.Location = new System.Drawing.Point(280, 17);
            this.btnMp3Stop.Name = "btnMp3Stop";
            this.btnMp3Stop.Size = new System.Drawing.Size(119, 33);
            this.btnMp3Stop.TabIndex = 3;
            this.btnMp3Stop.Text = "Stop";
            this.btnMp3Stop.UseVisualStyleBackColor = true;
            this.btnMp3Stop.Click += new System.EventHandler(this.btnMp3Stop_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.btnMp3Play);
            this.groupBox1.Controls.Add(this.btnMp3Pause);
            this.groupBox1.Controls.Add(this.btnMp3Stop);
            this.groupBox1.Location = new System.Drawing.Point(248, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(434, 62);
            this.groupBox1.TabIndex = 7;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "mp3";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.btnMp4Play);
            this.groupBox2.Controls.Add(this.btnMp4Pause);
            this.groupBox2.Controls.Add(this.btnMp4Stop);
            this.groupBox2.Location = new System.Drawing.Point(248, 80);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(434, 62);
            this.groupBox2.TabIndex = 8;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "mp4";
            // 
            // btnMp4Play
            // 
            this.btnMp4Play.Location = new System.Drawing.Point(24, 16);
            this.btnMp4Play.Name = "btnMp4Play";
            this.btnMp4Play.Size = new System.Drawing.Size(107, 37);
            this.btnMp4Play.TabIndex = 1;
            this.btnMp4Play.Text = "Play";
            this.btnMp4Play.UseVisualStyleBackColor = true;
            this.btnMp4Play.Click += new System.EventHandler(this.btnMp4Play_Click);
            // 
            // btnMp4Pause
            // 
            this.btnMp4Pause.Location = new System.Drawing.Point(145, 16);
            this.btnMp4Pause.Name = "btnMp4Pause";
            this.btnMp4Pause.Size = new System.Drawing.Size(119, 35);
            this.btnMp4Pause.TabIndex = 2;
            this.btnMp4Pause.Text = "Pause";
            this.btnMp4Pause.UseVisualStyleBackColor = true;
            this.btnMp4Pause.Click += new System.EventHandler(this.btnMp4Pause_Click);
            // 
            // btnMp4Stop
            // 
            this.btnMp4Stop.Location = new System.Drawing.Point(280, 18);
            this.btnMp4Stop.Name = "btnMp4Stop";
            this.btnMp4Stop.Size = new System.Drawing.Size(119, 33);
            this.btnMp4Stop.TabIndex = 3;
            this.btnMp4Stop.Text = "Stop";
            this.btnMp4Stop.UseVisualStyleBackColor = true;
            this.btnMp4Stop.Click += new System.EventHandler(this.btnMp4Stop_Click);
            // 
            // player
            // 
            this.player.Enabled = true;
            this.player.Location = new System.Drawing.Point(12, 12);
            this.player.Name = "player";
            this.player.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("player.OcxState")));
            this.player.Size = new System.Drawing.Size(189, 125);
            this.player.TabIndex = 0;
            // 
            // btnMplayer
            // 
            this.btnMplayer.Location = new System.Drawing.Point(64, 286);
            this.btnMplayer.Name = "btnMplayer";
            this.btnMplayer.Size = new System.Drawing.Size(447, 167);
            this.btnMplayer.TabIndex = 9;
            this.btnMplayer.Text = "Mplayer";
            this.btnMplayer.UseVisualStyleBackColor = true;
            this.btnMplayer.Click += new System.EventHandler(this.btnMplayer_Click);
            // 
            // frmKaraoke
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(998, 583);
            this.Controls.Add(this.btnMplayer);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.player);
            this.Name = "frmKaraoke";
            this.Text = "GH Karaoke System";
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.player)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private AxWMPLib.AxWindowsMediaPlayer player;
        private System.Windows.Forms.Button btnMp3Play;
        private System.Windows.Forms.Button btnMp3Pause;
        private System.Windows.Forms.Button btnMp3Stop;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button btnMp4Play;
        private System.Windows.Forms.Button btnMp4Pause;
        private System.Windows.Forms.Button btnMp4Stop;
        private System.Windows.Forms.Button btnMplayer;
    }
}

