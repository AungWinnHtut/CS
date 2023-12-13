namespace CardGame2
{
    partial class frmMain
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMain));
            this.picP1C1 = new System.Windows.Forms.PictureBox();
            this.picP1C2 = new System.Windows.Forms.PictureBox();
            this.picP2C2 = new System.Windows.Forms.PictureBox();
            this.picP2C1 = new System.Windows.Forms.PictureBox();
            this.btnPlay = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.picP1C1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picP1C2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picP2C2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.picP2C1)).BeginInit();
            this.SuspendLayout();
            // 
            // picP1C1
            // 
            this.picP1C1.Image = ((System.Drawing.Image)(resources.GetObject("picP1C1.Image")));
            this.picP1C1.Location = new System.Drawing.Point(57, 100);
            this.picP1C1.Name = "picP1C1";
            this.picP1C1.Size = new System.Drawing.Size(196, 271);
            this.picP1C1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picP1C1.TabIndex = 0;
            this.picP1C1.TabStop = false;
            // 
            // picP1C2
            // 
            this.picP1C2.Image = ((System.Drawing.Image)(resources.GetObject("picP1C2.Image")));
            this.picP1C2.Location = new System.Drawing.Point(273, 102);
            this.picP1C2.Name = "picP1C2";
            this.picP1C2.Size = new System.Drawing.Size(196, 271);
            this.picP1C2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picP1C2.TabIndex = 1;
            this.picP1C2.TabStop = false;
            // 
            // picP2C2
            // 
            this.picP2C2.Image = ((System.Drawing.Image)(resources.GetObject("picP2C2.Image")));
            this.picP2C2.Location = new System.Drawing.Point(793, 102);
            this.picP2C2.Name = "picP2C2";
            this.picP2C2.Size = new System.Drawing.Size(196, 271);
            this.picP2C2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picP2C2.TabIndex = 3;
            this.picP2C2.TabStop = false;
            // 
            // picP2C1
            // 
            this.picP2C1.Image = ((System.Drawing.Image)(resources.GetObject("picP2C1.Image")));
            this.picP2C1.Location = new System.Drawing.Point(580, 100);
            this.picP2C1.Name = "picP2C1";
            this.picP2C1.Size = new System.Drawing.Size(196, 271);
            this.picP2C1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picP2C1.TabIndex = 2;
            this.picP2C1.TabStop = false;
            // 
            // btnPlay
            // 
            this.btnPlay.Location = new System.Drawing.Point(439, 417);
            this.btnPlay.Name = "btnPlay";
            this.btnPlay.Size = new System.Drawing.Size(187, 66);
            this.btnPlay.TabIndex = 4;
            this.btnPlay.Text = "Play";
            this.btnPlay.UseVisualStyleBackColor = true;
            this.btnPlay.Click += new System.EventHandler(this.btnPlay_Click);
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1104, 522);
            this.Controls.Add(this.btnPlay);
            this.Controls.Add(this.picP2C2);
            this.Controls.Add(this.picP2C1);
            this.Controls.Add(this.picP1C2);
            this.Controls.Add(this.picP1C1);
            this.Name = "frmMain";
            this.Text = "Green Hackers Card Game";
            ((System.ComponentModel.ISupportInitialize)(this.picP1C1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picP1C2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picP2C2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.picP2C1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox picP1C1;
        private System.Windows.Forms.PictureBox picP1C2;
        private System.Windows.Forms.PictureBox picP2C2;
        private System.Windows.Forms.PictureBox picP2C1;
        private System.Windows.Forms.Button btnPlay;
    }
}

