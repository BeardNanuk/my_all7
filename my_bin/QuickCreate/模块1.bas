Attribute VB_Name = "ģ��1"
Sub Export()

FileName = "D:\dk_ze\Arno\PtoP.png"
ActiveWindow.Selection.SlideRange(1).Export FileName, "PNG", 1280, 720

End Sub
