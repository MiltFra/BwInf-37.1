Public Class Form1

    Dim alphabet As List(Of String)
    Dim woerterbuch As Dictionary(Of String, List(Of String))

    Private Function twist(ByVal input As String) As String
        If input.Length < 4 Then Return input
        Dim output As String
        Dim alreadyDrawn(input.Length - 1) As Boolean

        Do
            output = ""
            'Array mit false-Werten füllen
            For i As Integer = 0 To alreadyDrawn.Length - 1
                alreadyDrawn(i) = False
            Next

            'ersten und letzten Buchstaben als gezogen markieren -> bleiben unverändert
            alreadyDrawn(0) = True
            alreadyDrawn(input.Length - 1) = True

            'ersten Buchstaben in den Output geben
            output = input(0)

            'random Buchstaben auswählen, zum Output hinzufügen
            Dim j As Integer
            For i As Integer = 1 To input.Length - 2
                Do
                    j = CInt(Rnd() * (input.Length - 2) + 1)
                Loop Until Not alreadyDrawn(j)
                alreadyDrawn(j) = True
                output &= input(j)
            Next

            'letzten Buchstaben in den Output geben
            output &= input(input.Length - 1)
        Loop While output = input
        Return output
    End Function

    Private Function deTwist(word As String) As String
        Dim upperLowerCase(word.Length - 1) As Boolean

        'Es gibt nichts zu tun, wenn das Wort zu kurz ist
        If word.Length <= 3 Then
            Return word
        End If

        'Groß- und Kleinschreibung wird gespeichert, danach alles klein geschrieben
        For i As Integer = 0 To upperLowerCase.Length - 1
            upperLowerCase(i) = (word(i) = UCase(word(i)))
        Next
        Dim lowWord As String = LCase(word)

        'Falls im Wörterbuch das Wort enthalten ist, wird das enttwistete äquivalent benutzt
        If woerterbuch.ContainsKey(fingerprint(lowWord)) Then
            word = applyCase(upperLowerCase, woerterbuch.Item(fingerprint(lowWord)).Item(0))
            If woerterbuch.Item(fingerprint(lowWord)).Count > 1 Then
                word = "[ " & word
                For i As Integer = 1 To woerterbuch.Item(fingerprint(lowWord)).Count - 1
                    word &= " | "
                    word &= woerterbuch.Item(fingerprint(lowWord)).Item(i)
                Next
                word &= " ]"
            End If
        End If

        Return word
    End Function

    Private Function applyCase(ByRef ulc() As Boolean, ByVal _item As String) As String
        'Groß- und Kleinschreibung des Wortes wiederherstellen
        Dim newWord As String = ""
        For i As Integer = 0 To ulc.Length - 1
            If ulc(i) Then
                newWord &= UCase(_item(i))
            Else
                newWord &= LCase(_item(i))
            End If
        Next
        Return newWord
    End Function

    Private Function chooseFile(title As String, filter As String) As String
        Dim output As String = Nothing

        'File auswählen
        OpenFileDialog1.Title = title
        OpenFileDialog1.Filter = filter
        If OpenFileDialog1.ShowDialog() = DialogResult.OK And OpenFileDialog1.CheckFileExists Then
            output = OpenFileDialog1.FileName
        Else
            MsgBox("Bitte Datei auswählen")
        End If

        'Dateipfad zurückgeben
        Return output
    End Function

    Private Function fingerprint(ByVal input As String) As String
        'gibt das übergebene Wort alphabetisch sortiert zurück
        'lässt die äußeren Buchstaben am Ort

        'falls Wort zu kurz, gibt es nichts zu tun
        If input.Length < 4 Then Return input

        'temp ist String mit erstem Buchstaben des Wortes
        Dim temp As String = input(0)

        'Array mit Buchstaben deklariert und mit den mittleren Buchstaben des Wortes gefüllt
        Dim characters(input.Length - 3) As Char
        input.CopyTo(1, characters, 0, input.Length - 2)

        'characters-Array alphabetisch sortiert
        Array.Sort(characters)

        'characters-Array zu temp hinzugefügt, letzter Buchstabe an temp angehängt
        For Each character As Char In characters
            temp &= character
        Next
        Return temp & input(input.Length - 1)
    End Function

    Private Sub readWordlist(path As String, output As Boolean)
        Dim reader As New IO.StreamReader(path)
        Dim line As String = ""
        Dim lineFingerprint As String = ""
        Dim wordList As New List(Of String)
        alphabet = New List(Of String)
        'Wörterbuch mit *Wort-Fingerprint -> mögliche Wörter*
        woerterbuch = New Dictionary(Of String, List(Of String))

        'Wörterliste Zeile für Zeile einlesen
        While Not reader.EndOfStream()
            line = reader.ReadLine()

            'Zum Alphabet Buchstaben hinzufügen
            For i As Integer = 0 To line.Length() - 1
                If Not alphabet.Contains(line(i)) Then
                    alphabet.Add(line(i))
                    RichTextBoxCharacters.Text &= line(i) & vbCrLf
                End If
            Next

            line = LCase(line)

            'Im Wörterbuch Wörter einfügen, falls der Wort-Fingerprint noch nicht existiert, hinzufügen
            lineFingerprint = fingerprint(line)
            If Not woerterbuch.ContainsKey(lineFingerprint) Then
                woerterbuch.Add(lineFingerprint, New List(Of String))
            End If
            woerterbuch(lineFingerprint).Add(line)

            'Wörterliste ergänzen
            wordList.Add(line & " - " & lineFingerprint)
        End While

        'Wörterliste in ListBox einfügen
        If output Then
            For Each thing In wordList
                ListBoxWords.Items.Add(thing)
            Next
        End If
    End Sub

    Private Sub ButtonDetwist_Click(sender As Object, e As EventArgs) Handles ButtonDetwist.Click
        Dim deTwistFile As String = chooseFile("Datei zum Twisten auswählen", "Textfile|*.txt")
        Dim reader As New IO.StreamReader(deTwistFile)
        Dim tempCharacter As String
        Dim tempWord As String = ""
        Dim output As String = ""

        'Falls der File nicht existiert
        If deTwistFile = Nothing Then
            Exit Sub
        End If

        While Not reader.EndOfStream
            tempCharacter = Convert.ToChar(reader.Read())

            If alphabet.Contains(tempCharacter) Then    'Falls es ein gültiger Buchstabe ist, wird er zum Wort addiert
                tempWord &= tempCharacter
            Else                                        'Ansonsten ist es ein Sonderzeichen, das heißt, das Wort ist fertig
                If tempWord <> "" Then
                    output &= deTwist(tempWord)
                    tempWord = ""
                End If
                output &= tempCharacter
            End If

        End While

        reader.Close()

        If tempWord <> "" Then
            output &= twist(tempWord)
            tempWord = ""
        End If

        RichTextBoxOutput.Text = output
    End Sub

    Private Sub ButtonTwist_Click(sender As Object, e As EventArgs) Handles ButtonTwist.Click
        Dim twistFile As String = chooseFile("Datei zum Twisten auswählen", "Textfile|*.txt")

        'Falls der File nicht existiert
        If twistFile = Nothing Then
            Exit Sub
        End If

        Dim reader As New IO.StreamReader(twistFile)
        Dim tempCharacter As String
        Dim tempWord As String = ""
        Dim output As String = ""

        While Not reader.EndOfStream
            tempCharacter = Convert.ToChar(reader.Read())
            If alphabet.Contains(tempCharacter) Then
                tempWord &= tempCharacter
            Else
                If tempWord <> "" Then
                    output &= twist(tempWord)
                    tempWord = ""
                End If
                output &= tempCharacter
            End If
        End While
        reader.Close()
        If tempWord <> "" Then
            output &= twist(tempWord)
            tempWord = ""
        End If
        RichTextBoxOutput.Text = output
    End Sub

    Private Sub ButtonReadWordList1_Click(sender As Object, e As EventArgs) Handles ButtonReadWordList1.Click
        Dim wordListFile As String = chooseFile("Wörterliste auswählen", "Textfile|*.txt")
        If wordListFile <> Nothing Then
            readWordlist(wordListFile, True)
            ButtonTwist.Enabled = True
            ButtonDetwist.Enabled = True
        End If
    End Sub

    Private Sub ButtonReadWordList2_Click(sender As Object, e As EventArgs) Handles ButtonReadWordList2.Click
        Dim wordListFile As String = chooseFile("Wörterliste auswählen", "Textfile|*.txt")
        If wordListFile <> Nothing Then
            readWordlist(wordListFile, False)
            ButtonTwist.Enabled = True
            ButtonDetwist.Enabled = True
        End If
    End Sub
End Class
