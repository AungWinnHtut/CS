namespace WinForm1
{
    partial class frmUnitConverter
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
            this.lblInches = new System.Windows.Forms.Label();
            this.txtInches = new System.Windows.Forms.TextBox();
            this.lblCm = new System.Windows.Forms.Label();
            this.txtCm = new System.Windows.Forms.TextBox();
            this.btnConvert = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblInches
            // 
            this.lblInches.AutoSize = true;
            this.lblInches.Location = new System.Drawing.Point(63, 95);
            this.lblInches.Name = "lblInches";
            this.lblInches.Size = new System.Drawing.Size(86, 30);
            this.lblInches.TabIndex = 0;
            this.lblInches.Text = "Inches";
            // 
            // txtInches
            // 
            this.txtInches.Location = new System.Drawing.Point(160, 89);
            this.txtInches.Name = "txtInches";
            this.txtInches.Size = new System.Drawing.Size(225, 26);
            this.txtInches.TabIndex = 1;
            // 
            // lblCm
            // 
            this.lblCm.AutoSize = true;
            this.lblCm.Location = new System.Drawing.Point(457, 94);
            this.lblCm.Name = "lblCm";
            this.lblCm.Size = new System.Drawing.Size(45, 30);
            this.lblCm.TabIndex = 2;
            this.lblCm.Text = "cm";
            // 
            // txtCm
            // 
            this.txtCm.Location = new System.Drawing.Point(512, 94);
            this.txtCm.Name = "txtCm";
            this.txtCm.Size = new System.Drawing.Size(326, 26);
            this.txtCm.TabIndex = 3;
            // 
            // btnConvert
            // 
            this.btnConvert.Location = new System.Drawing.Point(73, 160);
            this.btnConvert.Name = "btnConvert";
            this.btnConvert.Size = new System.Drawing.Size(764, 95);
            this.btnConvert.TabIndex = 4;
            this.btnConvert.Text = "Convert";
            this.btnConvert.UseVisualStyleBackColor = true;
            this.btnConvert.Click += new System.EventHandler(this.btnConvert_Click);
            // 
            // frmUnitConverter
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(933, 299);
            this.Controls.Add(this.btnConvert);
            this.Controls.Add(this.txtCm);
            this.Controls.Add(this.lblCm);
            this.Controls.Add(this.txtInches);
            this.Controls.Add(this.lblInches);
            this.Name = "frmUnitConverter";
            this.Text = "frmUnitConverter";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.frmUnitConverter_FormClosing);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblInches;
        private System.Windows.Forms.TextBox txtInches;
        private System.Windows.Forms.Label lblCm;
        private System.Windows.Forms.TextBox txtCm;
        private System.Windows.Forms.Button btnConvert;
    }
}