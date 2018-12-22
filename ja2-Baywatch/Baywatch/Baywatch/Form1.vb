Public Class Form1

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Dim george() As String
        Dim longstock() As String
        Dim translate() As String = {"?", "Wald", "Wiese", "Häuser", "Wüste", "See", "Sumpf", "Reisfeld", "Berg", "Vulkankater"}
        Dim dateileser As IO.StreamReader
        Dim startab As Integer = 0
        Dim counter As Integer = 0
        Dim ersteloesung As Integer
        ListBox_loesung.Items.Clear()
        If OpenFileDialog1.ShowDialog = DialogResult.OK Then
            If IO.File.Exists(OpenFileDialog1.FileName) Then
                dateileser = New IO.StreamReader(OpenFileDialog1.FileName)
                Dim zeile As String = dateileser.ReadLine
                Dim passt As Boolean = False
                zeile = zeile & " " & zeile
                george = zeile.Split(" ")
                zeile = dateileser.Readline
                zeile = zeile.Replace("?", "0")
                longstock = zeile.Split(" ")
                While startab < longstock.Length
                    passt = True
                    For check As Integer = 0 To longstock.Length - 1
                        If longstock(check) <> "0" Then
                            If longstock(check) <> george(startab + check) Then
                                passt = False
                                Exit For
                            End If
                        End If
                    Next
                    If passt Then
                        If counter = 0 Then ersteloesung = startab
                        counter = counter + 1
                    End If
                    startab += 1
                End While
                If counter > 0 Then
                    For lauf As Integer = 0 To longstock.Length - 1
                        ListBox_loesung.Items.Add(translate(george(lauf + ersteloesung)) & vbTab & ": " & translate(longstock(lauf)))
                    Next
                Else
                    ListBox_loesung.Items.Add("Keine Lösung!")
                End If
            End If
        End If
        If counter = 1 Then Label1.Text = counter & " Lösung"
        If counter <> 1 Then Label1.Text = counter & " Lösungen"
    End Sub
End Class


