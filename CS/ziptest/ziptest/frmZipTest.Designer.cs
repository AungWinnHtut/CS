namespace ziptest
{
    partial class frmZipTest
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmZipTest));
            this.btnCompress = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.btnVScode = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnCompress
            // 
            this.btnCompress.Location = new System.Drawing.Point(10, 103);
            this.btnCompress.Name = "btnCompress";
            this.btnCompress.Size = new System.Drawing.Size(96, 45);
            this.btnCompress.TabIndex = 0;
            this.btnCompress.Text = "Compress";
            this.btnCompress.UseVisualStyleBackColor = true;
            this.btnCompress.Click += new System.EventHandler(this.btnCompress_Click);
            // 
            // btnExit
            // 
            this.btnExit.Location = new System.Drawing.Point(10, 509);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(175, 51);
            this.btnExit.TabIndex = 1;
            this.btnExit.Text = "Exit";
            this.btnExit.UseVisualStyleBackColor = true;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // btnVScode
            // 
            this.btnVScode.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("btnVScode.BackgroundImage")));
            this.btnVScode.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.btnVScode.Image = ((System.Drawing.Image)(resources.GetObject("btnVScode.Image")));
            this.btnVScode.Location = new System.Drawing.Point(10, 180);
            this.btnVScode.Name = "btnVScode";
            this.btnVScode.Size = new System.Drawing.Size(91, 93);
            this.btnVScode.TabIndex = 2;
            this.btnVScode.UseVisualStyleBackColor = true;
            this.btnVScode.Click += new System.EventHandler(this.btnVScode_Click);
            // 
            // frmZipTest
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(196, 564);
            this.ControlBox = false;
            this.Controls.Add(this.btnVScode);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.btnCompress);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "frmZipTest";
            this.Text = "VScode";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnCompress;
        private System.Windows.Forms.Button btnExit;
        private System.Windows.Forms.Button btnVScode;
    }
}

