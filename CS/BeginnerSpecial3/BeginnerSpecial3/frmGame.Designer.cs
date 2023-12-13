namespace BeginnerSpecial3
{
    partial class frmGame
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
            this.chkReading = new System.Windows.Forms.CheckBox();
            this.chkSwimming = new System.Windows.Forms.CheckBox();
            this.chkFootball = new System.Windows.Forms.CheckBox();
            this.lblHobby = new System.Windows.Forms.Label();
            this.btnCheck = new System.Windows.Forms.Button();
            this.lstHobby = new System.Windows.Forms.ListBox();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.gbBin = new System.Windows.Forms.GroupBox();
            this.gbCurrent = new System.Windows.Forms.GroupBox();
            this.txtRadius = new System.Windows.Forms.TextBox();
            this.lblRadius = new System.Windows.Forms.Label();
            this.btnCalculate = new System.Windows.Forms.Button();
            this.txtArea = new System.Windows.Forms.TextBox();
            this.lblArea = new System.Windows.Forms.Label();
            this.gbBin.SuspendLayout();
            this.gbCurrent.SuspendLayout();
            this.SuspendLayout();
            // 
            // chkReading
            // 
            this.chkReading.AutoSize = true;
            this.chkReading.Location = new System.Drawing.Point(21, 65);
            this.chkReading.Name = "chkReading";
            this.chkReading.Size = new System.Drawing.Size(95, 24);
            this.chkReading.TabIndex = 0;
            this.chkReading.Text = "Reading";
            this.chkReading.UseVisualStyleBackColor = true;
            // 
            // chkSwimming
            // 
            this.chkSwimming.AutoSize = true;
            this.chkSwimming.Location = new System.Drawing.Point(128, 65);
            this.chkSwimming.Name = "chkSwimming";
            this.chkSwimming.Size = new System.Drawing.Size(107, 24);
            this.chkSwimming.TabIndex = 1;
            this.chkSwimming.Text = "Swimming";
            this.chkSwimming.UseVisualStyleBackColor = true;
            // 
            // chkFootball
            // 
            this.chkFootball.AutoSize = true;
            this.chkFootball.Location = new System.Drawing.Point(250, 65);
            this.chkFootball.Name = "chkFootball";
            this.chkFootball.Size = new System.Drawing.Size(146, 24);
            this.chkFootball.TabIndex = 2;
            this.chkFootball.Text = "Plyaing Football";
            this.chkFootball.UseVisualStyleBackColor = true;
            // 
            // lblHobby
            // 
            this.lblHobby.AutoSize = true;
            this.lblHobby.Location = new System.Drawing.Point(20, 32);
            this.lblHobby.Name = "lblHobby";
            this.lblHobby.Size = new System.Drawing.Size(55, 20);
            this.lblHobby.TabIndex = 3;
            this.lblHobby.Text = "Hobby";
            // 
            // btnCheck
            // 
            this.btnCheck.Location = new System.Drawing.Point(21, 114);
            this.btnCheck.Name = "btnCheck";
            this.btnCheck.Size = new System.Drawing.Size(115, 47);
            this.btnCheck.TabIndex = 4;
            this.btnCheck.Text = "Check";
            this.btnCheck.UseVisualStyleBackColor = true;
            this.btnCheck.Click += new System.EventHandler(this.btnCheck_Click);
            // 
            // lstHobby
            // 
            this.lstHobby.FormattingEnabled = true;
            this.lstHobby.ItemHeight = 20;
            this.lstHobby.Location = new System.Drawing.Point(435, 15);
            this.lstHobby.Name = "lstHobby";
            this.lstHobby.Size = new System.Drawing.Size(219, 204);
            this.lstHobby.TabIndex = 5;
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Location = new System.Drawing.Point(21, 178);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(126, 24);
            this.radioButton1.TabIndex = 6;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "radioButton1";
            this.radioButton1.UseVisualStyleBackColor = true;
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Location = new System.Drawing.Point(176, 178);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(126, 24);
            this.radioButton2.TabIndex = 7;
            this.radioButton2.TabStop = true;
            this.radioButton2.Text = "radioButton2";
            this.radioButton2.UseVisualStyleBackColor = true;
            // 
            // gbBin
            // 
            this.gbBin.Controls.Add(this.chkFootball);
            this.gbBin.Controls.Add(this.lstHobby);
            this.gbBin.Controls.Add(this.radioButton2);
            this.gbBin.Controls.Add(this.radioButton1);
            this.gbBin.Controls.Add(this.chkReading);
            this.gbBin.Controls.Add(this.chkSwimming);
            this.gbBin.Controls.Add(this.lblHobby);
            this.gbBin.Controls.Add(this.btnCheck);
            this.gbBin.Location = new System.Drawing.Point(12, 12);
            this.gbBin.Name = "gbBin";
            this.gbBin.Size = new System.Drawing.Size(682, 239);
            this.gbBin.TabIndex = 8;
            this.gbBin.TabStop = false;
            this.gbBin.Text = "Bin";
            // 
            // gbCurrent
            // 
            this.gbCurrent.Controls.Add(this.lblArea);
            this.gbCurrent.Controls.Add(this.txtArea);
            this.gbCurrent.Controls.Add(this.btnCalculate);
            this.gbCurrent.Controls.Add(this.lblRadius);
            this.gbCurrent.Controls.Add(this.txtRadius);
            this.gbCurrent.Location = new System.Drawing.Point(12, 267);
            this.gbCurrent.Name = "gbCurrent";
            this.gbCurrent.Size = new System.Drawing.Size(682, 249);
            this.gbCurrent.TabIndex = 9;
            this.gbCurrent.TabStop = false;
            this.gbCurrent.Text = "Current Task";
            // 
            // txtRadius
            // 
            this.txtRadius.Location = new System.Drawing.Point(107, 37);
            this.txtRadius.Name = "txtRadius";
            this.txtRadius.Size = new System.Drawing.Size(204, 26);
            this.txtRadius.TabIndex = 0;
            // 
            // lblRadius
            // 
            this.lblRadius.AutoSize = true;
            this.lblRadius.Location = new System.Drawing.Point(11, 40);
            this.lblRadius.Name = "lblRadius";
            this.lblRadius.Size = new System.Drawing.Size(90, 20);
            this.lblRadius.TabIndex = 1;
            this.lblRadius.Text = "Radius(cm)";
            // 
            // btnCalculate
            // 
            this.btnCalculate.Location = new System.Drawing.Point(15, 162);
            this.btnCalculate.Name = "btnCalculate";
            this.btnCalculate.Size = new System.Drawing.Size(185, 72);
            this.btnCalculate.TabIndex = 2;
            this.btnCalculate.Text = "Calculate";
            this.btnCalculate.UseVisualStyleBackColor = true;
            this.btnCalculate.Click += new System.EventHandler(this.btnCalculate_Click);
            // 
            // txtArea
            // 
            this.txtArea.Enabled = false;
            this.txtArea.Location = new System.Drawing.Point(108, 85);
            this.txtArea.Name = "txtArea";
            this.txtArea.Size = new System.Drawing.Size(203, 26);
            this.txtArea.TabIndex = 3;
            // 
            // lblArea
            // 
            this.lblArea.AutoSize = true;
            this.lblArea.Location = new System.Drawing.Point(17, 85);
            this.lblArea.Name = "lblArea";
            this.lblArea.Size = new System.Drawing.Size(47, 20);
            this.lblArea.TabIndex = 4;
            this.lblArea.Text = "Area ";
            // 
            // frmGame
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(712, 528);
            this.Controls.Add(this.gbCurrent);
            this.Controls.Add(this.gbBin);
            this.Name = "frmGame";
            this.Text = "Green Hackers Game";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.gbBin.ResumeLayout(false);
            this.gbBin.PerformLayout();
            this.gbCurrent.ResumeLayout(false);
            this.gbCurrent.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.CheckBox chkReading;
        private System.Windows.Forms.CheckBox chkSwimming;
        private System.Windows.Forms.CheckBox chkFootball;
        private System.Windows.Forms.Label lblHobby;
        private System.Windows.Forms.Button btnCheck;
        private System.Windows.Forms.ListBox lstHobby;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.GroupBox gbBin;
        private System.Windows.Forms.GroupBox gbCurrent;
        private System.Windows.Forms.Label lblRadius;
        private System.Windows.Forms.TextBox txtRadius;
        private System.Windows.Forms.Label lblArea;
        private System.Windows.Forms.TextBox txtArea;
        private System.Windows.Forms.Button btnCalculate;
    }
}

