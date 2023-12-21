using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace WinForm1
{
    public partial class frmLibrary : Form
    {

        private string conString = "Server=127.0.0.1;Database=librarydb;User Id=root;Password='';";
        public frmLibrary()
        {
            InitializeComponent();
        }

        private void btnInsert_Click(object sender, EventArgs e)
        {
            string sBookName = txtName.Text;
            string sYear = txtYear.Text;
            int iYear = int.Parse(sYear);
            using (MySqlConnection connection = new MySqlConnection(conString))
            {
                connection.Open();
                                             

                // Insertion code
                string insertQuery = "INSERT INTO books (name, year) VALUES (@name, @year)";
                using (MySqlCommand insertCmd = new MySqlCommand(insertQuery, connection))
                {
                    // Replace these values with the actual values you want to insert
                    insertCmd.Parameters.AddWithValue("@name", sBookName);
                    insertCmd.Parameters.AddWithValue("@year", iYear);

                    // Execute the insertion query
                    int rowsAffected = insertCmd.ExecuteNonQuery();

                    if (rowsAffected > 0)
                    {
                        // If insertion is successful, refresh the data in the DataGridView
                        string refreshQuery = "SELECT * FROM books";
                        using (MySqlCommand refreshCmd = new MySqlCommand(refreshQuery, connection))
                        {
                            using (MySqlDataReader refreshReader = refreshCmd.ExecuteReader())
                            {
                                dataGridView.DataSource = null;
                                dataGridView.Rows.Clear();

                                while (refreshReader.Read())
                                {
                                    dataGridView.Rows.Add(refreshReader["id"], refreshReader["name"], refreshReader["year"]);
                                    cboBooks.Items.Add(refreshReader["name"]);
                                }
                                cboBooks.Text = cboBooks.Items.Count > 0 ? cboBooks.Items[0].ToString() : string.Empty;
                            }
                        }
                    }
                }
            }



        }

        private void btnShowAllBooks_Click(object sender, EventArgs e)
        {
            using (MySqlConnection connection = new MySqlConnection(conString))
            {
                connection.Open();
                
                string selectQuery = "SELECT * FROM books";
                using (MySqlCommand cmd = new MySqlCommand(selectQuery, connection))
                {
                    using (MySqlDataReader reader = cmd.ExecuteReader())
                    {
                        dataGridView.DataSource = null;
                        dataGridView.Rows.Clear();

                        while (reader.Read())
                        {
                            //MessageBox.Show(reader["name"].ToString());
                            dataGridView.Rows.Add(reader["id"], reader["name"], reader["year"]);
                            cboBooks.Items.Add(reader["name"]);
                        }
                        cboBooks.Text = cboBooks.Items[0].ToString();
                    }
                }
            }
        }
    }
}
