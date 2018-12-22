<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Das Formular überschreibt den Löschvorgang, um die Komponentenliste zu bereinigen.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Wird vom Windows Form-Designer benötigt.
    Private components As System.ComponentModel.IContainer

    'Hinweis: Die folgende Prozedur ist für den Windows Form-Designer erforderlich.
    'Das Bearbeiten ist mit dem Windows Form-Designer möglich.  
    'Das Bearbeiten mit dem Code-Editor ist nicht möglich.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.ButtonDetwist = New System.Windows.Forms.Button()
        Me.OpenFileDialog1 = New System.Windows.Forms.OpenFileDialog()
        Me.ButtonTwist = New System.Windows.Forms.Button()
        Me.RichTextBoxCharacters = New System.Windows.Forms.RichTextBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.RichTextBoxOutput = New System.Windows.Forms.RichTextBox()
        Me.ListBoxWords = New System.Windows.Forms.ListBox()
        Me.ButtonReadWordList1 = New System.Windows.Forms.Button()
        Me.ButtonReadWordList2 = New System.Windows.Forms.Button()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'ButtonDetwist
        '
        Me.ButtonDetwist.Enabled = False
        Me.ButtonDetwist.Location = New System.Drawing.Point(418, 118)
        Me.ButtonDetwist.Name = "ButtonDetwist"
        Me.ButtonDetwist.Size = New System.Drawing.Size(400, 100)
        Me.ButtonDetwist.TabIndex = 1
        Me.ButtonDetwist.Text = "Text Enttwisten"
        Me.ButtonDetwist.UseVisualStyleBackColor = True
        '
        'OpenFileDialog1
        '
        Me.OpenFileDialog1.FileName = "OpenFileDialog1"
        '
        'ButtonTwist
        '
        Me.ButtonTwist.Enabled = False
        Me.ButtonTwist.Location = New System.Drawing.Point(12, 118)
        Me.ButtonTwist.Name = "ButtonTwist"
        Me.ButtonTwist.Size = New System.Drawing.Size(400, 100)
        Me.ButtonTwist.TabIndex = 2
        Me.ButtonTwist.Text = "Text Twisten"
        Me.ButtonTwist.UseVisualStyleBackColor = True
        '
        'RichTextBoxCharacters
        '
        Me.RichTextBoxCharacters.AcceptsTab = True
        Me.RichTextBoxCharacters.Location = New System.Drawing.Point(343, 254)
        Me.RichTextBoxCharacters.Name = "RichTextBoxCharacters"
        Me.RichTextBoxCharacters.ReadOnly = True
        Me.RichTextBoxCharacters.Size = New System.Drawing.Size(69, 524)
        Me.RichTextBoxCharacters.TabIndex = 4
        Me.RichTextBoxCharacters.Text = ""
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(415, 238)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(69, 13)
        Me.Label1.TabIndex = 5
        Me.Label1.Text = "Fertiger Text:"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(340, 238)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(67, 13)
        Me.Label2.TabIndex = 7
        Me.Label2.Text = "Buchstaben:"
        '
        'RichTextBoxOutput
        '
        Me.RichTextBoxOutput.Location = New System.Drawing.Point(418, 254)
        Me.RichTextBoxOutput.Name = "RichTextBoxOutput"
        Me.RichTextBoxOutput.ReadOnly = True
        Me.RichTextBoxOutput.Size = New System.Drawing.Size(400, 524)
        Me.RichTextBoxOutput.TabIndex = 9
        Me.RichTextBoxOutput.Text = ""
        '
        'ListBoxWords
        '
        Me.ListBoxWords.FormattingEnabled = True
        Me.ListBoxWords.Location = New System.Drawing.Point(12, 254)
        Me.ListBoxWords.Name = "ListBoxWords"
        Me.ListBoxWords.Size = New System.Drawing.Size(325, 524)
        Me.ListBoxWords.TabIndex = 10
        '
        'ButtonReadWordList1
        '
        Me.ButtonReadWordList1.Location = New System.Drawing.Point(12, 12)
        Me.ButtonReadWordList1.Name = "ButtonReadWordList1"
        Me.ButtonReadWordList1.Size = New System.Drawing.Size(400, 100)
        Me.ButtonReadWordList1.TabIndex = 12
        Me.ButtonReadWordList1.Text = "Wörterliste einlesen und in ListBox ausgeben (langsamer)"
        Me.ButtonReadWordList1.UseVisualStyleBackColor = True
        '
        'ButtonReadWordList2
        '
        Me.ButtonReadWordList2.Location = New System.Drawing.Point(418, 12)
        Me.ButtonReadWordList2.Name = "ButtonReadWordList2"
        Me.ButtonReadWordList2.Size = New System.Drawing.Size(400, 100)
        Me.ButtonReadWordList2.TabIndex = 13
        Me.ButtonReadWordList2.Text = "Wörterliste einlesen ohne in die ListBox auszugeben (schneller)"
        Me.ButtonReadWordList2.UseVisualStyleBackColor = True
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(9, 238)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(263, 13)
        Me.Label3.TabIndex = 14
        Me.Label3.Text = "Wörterliste (bleibt leer, falls schnellere Option gewählt):"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(831, 791)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.ButtonReadWordList2)
        Me.Controls.Add(Me.ButtonReadWordList1)
        Me.Controls.Add(Me.ListBoxWords)
        Me.Controls.Add(Me.RichTextBoxOutput)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.RichTextBoxCharacters)
        Me.Controls.Add(Me.ButtonTwist)
        Me.Controls.Add(Me.ButtonDetwist)
        Me.Name = "Form1"
        Me.Text = "Twister"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents OpenFileDialog1 As OpenFileDialog
    Friend WithEvents ButtonTwist As Button
    Friend WithEvents RichTextBoxCharacters As RichTextBox
    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents RichTextBoxOutput As RichTextBox
    Friend WithEvents ListBoxWords As ListBox
    Friend WithEvents ButtonReadWordList1 As Button
    Friend WithEvents ButtonReadWordList2 As Button
    Friend WithEvents Label3 As Label
    Friend WithEvents ButtonDetwist As Button
End Class
