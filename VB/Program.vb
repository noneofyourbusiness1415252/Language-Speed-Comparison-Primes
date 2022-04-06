Imports System.Console

Module Program
	Sub Main(args As String())
		Write(2)
		Dim half = args(0) \ 2ui, sieve(half) As Boolean, total = 1ui
		For i = 3us To args(0) ^ .5 Step 2
			If Not sieve(i \ 2) Then
				For j = i ^ 2ui \ 2 To half - 1 Step i
					sieve(j) = True
				Next
			End If
		Next
		For i = 1ui To half - 1
			If Not sieve(i) Then
				Write(", {0}", 2 * i + 1)
				total = total + 1
			End If
		Next
		WriteLine(vbLf & "Total: {0}", total)
	End Sub
End Module
