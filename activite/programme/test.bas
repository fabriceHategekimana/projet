REM  *****  BASIC  *****

Sub Main
	StartDialog1()
End Sub


Sub StartDialog1()
    BasicLibraries.LoadLibrary("Tools")
    oDialog1 = LoadDialog("Standard", "programme")
    oDialog1.Execute()
End Sub

Sub readDialog1()
	oT1 = oDialog1.GetControl("TextField1")
    msgbox cell_val.String & chr(13) & "Value from controls: "  & oT1.Text
End Sub

