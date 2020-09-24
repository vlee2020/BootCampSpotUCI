Attribute VB_Name = "Module1"
Sub AnalyzeStockWorksheetLoop()
        
        Dim ws As Worksheet
        
        For Each ws In ThisWorkbook.Worksheets
        
         
            Dim LastRow
            Dim minDate As Double
            Dim maxDate As Double
            Dim minUniqueID As String
            Dim maxUniqueID As String
            Dim openPrice As Double
            Dim closePrice As Double
            Dim yearlyChange As Variant
            Dim percentChange As Variant
            Dim stockVolume As Variant
           
        
            LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row 'Identify LastRow Number
         
        
            'Insert Column to contain and populate UniqueID---------------------------------------------------------------------------------------------------------------------
        
            ws.Range("A:A").EntireColumn.Insert
            ws.Cells(1, 1).Value = "<UniqueId>"
            
        
                For y = 2 To LastRow
        
                    If ws.Cells(y, 3).Value Mod 1 = 0 Then
                
                        ws.Cells(y, 1).Value = ws.Cells(y, 3) & ws.Cells(y, 2)
                    
                    Else
            
                    End If
        
                Next y
 
              
            'Set Headers--------------------------------------------------------------------------------------------------------------------------------------------------------
        
                ws.Cells(1, 10).Value = "Ticker"
                ws.Cells(1, 11).Value = "YearlyChange"
                ws.Cells(1, 12).Value = "PercentChange"
                ws.Cells(1, 13).Value = "Total Stock Volume"
    
    
            'Output Unique Ticker List------------------------------------------------------------------------------------------------------------------------------------------
        
                ws.Range("b2:b" & LastRow).Copy Destination:=ws.Range("j2:j" & LastRow) 'Copy range data to destination range; determine the ending row using LastRow dynamic variable
                ws.Range("j2:j" & LastRow).RemoveDuplicates Columns:=1, Header:=xlNo 'Remove duplicates from specific column...in this case Tickers column I
        
                    'Initiate 2nd for loop for summary data
        
                    For x = 2 To LastRow
        
        
                        'Calculate MinDate and MaxDate for each unique ticker range leveraging the worksheet functions----------------------------------------------------------------------
            
                        minDate = WorksheetFunction.MinIfs(ws.Range("c2:c" & LastRow), ws.Range("b2:b" & LastRow), ws.Cells(x, 10)) 'Determine earliest date based on arguments
                        maxDate = WorksheetFunction.MaxIfs(ws.Range("c2:c" & LastRow), ws.Range("b2:b" & LastRow), ws.Cells(x, 10)) 'Determine latest date based on arguments
              
                        
                        'Calculate and Output: Yearly Change from opening price at the beginning of a given year to the closing price at the end of that year-------------------------------
                        minUniqueID = minDate & ws.Cells(x, 10)
                        maxUniqueID = maxDate & ws.Cells(x, 10)
                        
                        'end for loop if condition is met
                        If minUniqueID = "0" Or maxUniqueID = "0" Then
                            
                            Exit For
                            
                        End If
                        
                        'Calculate % Change from opening price at the beginning of a given year to the closing price at the end of the year
                        openPrice = WorksheetFunction.VLookup(Trim(minUniqueID), ws.Range("A2:H" & LastRow), 4, False)
                        closePrice = WorksheetFunction.VLookup(Trim(maxUniqueID), ws.Range("A2:H" & LastRow), 7, False)
  
                        'end for loop if condition is met
                        If openPrice = "0" Then
                            
                            Exit For
                            
                        End If
                        
                        yearlyChange = closePrice - openPrice
                    
                        ws.Cells(x, 11).Value = yearlyChange
                        
                        percentChange = yearlyChange / openPrice
                        
                        'Calculate Total Stock Volume
                        stockVolume = WorksheetFunction.SumIf(ws.Range("B2:B" & LastRow), ws.Cells(x, 10), ws.Range("H2:H" & LastRow))
                        ws.Cells(x, 13).Value = stockVolume
                        
                        'Conditional Highlight Formatting based on +/- %age
                        
                        If percentChange >= 0 Then
                                ws.Cells(x, 12).Value = FormatPercent(percentChange)
                                ws.Cells(x, 12).Interior.ColorIndex = 4
                         
                            Else
                                ws.Cells(x, 12).Value = FormatPercent(percentChange)
                                ws.Cells(x, 12).Interior.ColorIndex = 3
                               
                        End If
                        
                    Next x
                
            'Autofit Columns all columns on worksheet
                ws.Range("A:A, M:M").EntireColumn.AutoFit
                      
            
            'Bonus Calculations and Output
                       
                Dim GreatestIncreaseTicker
                Dim GreatestDecreaseTicker
                Dim GreatestVolumeTicker
                Dim GreatestIncreaseValue
                Dim GreatestDecreaseValue
                Dim GreatestVolumeValue
                
                ws.Cells(2, 16).Value = "Greatest % Increase"
                ws.Cells(3, 16).Value = "Greatest % Decrease"
                ws.Cells(4, 16).Value = "Greatest Total Volume"
                ws.Cells(1, 17).Value = "Ticker"
                ws.Cells(1, 18).Value = "Value"
                      
        Next ws
               
    End Sub




