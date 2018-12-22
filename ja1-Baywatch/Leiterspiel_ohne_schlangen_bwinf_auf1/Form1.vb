Public Class Form1

    Private Sub Button1_Click(sender As System.Object, e As System.EventArgs) Handles Button1.Click
        Dim augen As Integer
        Dim feld As Integer
        Dim schritte As Integer
        feld = 0
        augen = ComboBox1.SelectedItem.ToString
        schritte = 0

        While feld <> 100
            feld = feld + augen
            schritte = schritte + 1
            If feld > 100 Then feld = 200 - feld
            If schritte > 100 Then
                MsgBox("Dat kann gar nicht funktionieren!!!")
                Exit Sub
            End If
            Select Case feld
                Case 6
                    feld = 27
                Case 14
                    feld = 19
                Case 21
                    feld = 53
                Case 27
                    feld = 6
                Case 31
                    feld = 42
                Case 33
                    feld = 38
                Case 38
                    feld = 33
                Case 42
                    feld = 31
                Case 46
                    feld = 62
                Case 51
                    feld = 59
                Case 53
                    feld = 21
                Case 57
                    feld = 96
                Case 59
                    feld = 51
                Case 62
                    feld = 46
                Case 65
                    feld = 85
                Case 68
                    feld = 80
                Case 70
                    feld = 76
                Case 76
                    feld = 70
                Case 80
                    feld = 68
                Case 85
                    feld = 65
                Case 92
                    feld = 98
                Case 96
                    feld = 57
                Case 98
                    feld = 92

            End Select

        End While

        MsgBox("Juhu, es sind " & schritte & " Schritte!")
    End Sub
End Class
