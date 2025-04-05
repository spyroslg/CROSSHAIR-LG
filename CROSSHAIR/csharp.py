Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> using System;
... using System.Drawing;
... using System.Windows.Forms;
... 
... public class CrosshairApp : Form
... {
...     public CrosshairApp()
...     {
...         this.FormBorderStyle = FormBorderStyle.None;
...         this.StartPosition = FormStartPosition.CenterScreen;
...         this.BackColor = Color.Magenta; // Διαφανές χρώμα
...         this.TransparencyKey = Color.Magenta; // Κάνει το χρώμα διαφανές
...         this.TopMost = true;
...         this.Width = 50;
...         this.Height = 50;
...     }
... 
...     protected override void OnPaint(PaintEventArgs e)
...     {
...         base.OnPaint(e);
...         Graphics g = e.Graphics;
... 
...         // Ζωγραφίζουμε τον οριζόντιο και κατακόρυφο σταυρό
...         Pen pen = new Pen(Color.Black, 2);
...         g.DrawLine(pen, 0, this.Height / 2, this.Width, this.Height / 2); // Οριζόντια γραμμή
...         g.DrawLine(pen, this.Width / 2, 0, this.Width / 2, this.Height); // Κάθετη γραμμή
...     }
... 
...     [STAThread]
...     static void Main()
...     {
...         Application.Run(new CrosshairApp());
...     }
... }
