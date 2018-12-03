Attribute VB_Name = "Ä£¿é1"
Sub Generate_PDF_Cert()
'This function saves the last slide as a PDF file with a time stamp and the users name who completed the induction.

timestamp = Now()

Dim PR As PrintRange
Dim lngLast As Long
Dim savePath As String
Dim PrintPDF As Integer


'Location of saved file
'savePath = Environ("USERPROFILE") & "\Desktop\Induction\Certificates\" & Format(timestamp, "yyyymmdd-hhnn") & "_" & FirstNameX & "_" & LastNameX & ".pdf"
savePath = "D:\dk_ze\Arno\" & Format(timestamp, "yyyymmdd-hhnn") & "_" & FirstNameX & "_" & LastNameX & ".pdf"


lngLast = ActivePresentation.Slides.Count

With ActivePresentation.PrintOptions
    .Ranges.ClearAll ' always do this
    Set PR = .Ranges.Add(Start:=lngLast, End:=lngLast)
    .HighQuality = msoCTrue
End With

ActivePresentation.ExportAsFixedFormat _
Path:=savePath, _
FixedFormatType:=ppFixedFormatTypePDF, _
PrintRange:=PR, _
Intent:=ppFixedFormatIntentScreen, _
FrameSlides:=msoTrue, _
RangeType:=ppPrintSlideRange

'Prompt user of file location and option to print.
PrintPDF = MsgBox("A PDF file of this certificate has been saved to: " & vbCrLf & savePath & vbCrLf & vbCrLf & "Would you like to print a copy also?", vbYesNo, "PDF File Created")
If PrintPDF = 6 Then Call Print_Active_Slide


End Sub

