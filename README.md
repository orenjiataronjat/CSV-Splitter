# CSV-Splitter
(Using pandas) At my work today we had an excel file over 2 gigabytes and needed to open it. That is too large for either Excel or Google Sheets to work with. This code cut the file into seperate files. This could also be accomplished on macOS using "split -l filename.csv" but this code can be modified further for other needed tasks using the read csv function commented out from pandas.