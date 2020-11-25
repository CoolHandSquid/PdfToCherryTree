# PdfToCherryTree
* Convert a pdf file (or folder of pdf's) into a series of nodes in cherrytree. That cherrytree can be merged into a larger cherrytree. Linux only for now.
* PdfToCherryTree is a product of 19% security solutions
## Build
* python3 -m pip install wand
## Useage
* Synatx:     python3 PdfToCherry.py inputPdf outputCtd
* Example:    python3 /root/Desktop/Example.pdf /root/Desktop/TempCherryTree.ctd
* Note:       The goal of this tool is to turn the PDF into a node in a temporary CherryTree that you can then merge with your functional CherryTree.
* This tool will not parse nodes, or add to an existing CherryTree.
* You can put a folder in place of inputPdf and the tool will convert all Pdf's (and only Pdf's) into their own node in the outputCtd CherryTree.
* This tool will only work on linux (could be ported with relative ease).
* Be sure to make your outfile a .ctd so cherrytree knows to open it as an unprotected xml.
![alt text](https://github.com/CoolHandSquid/PdfToCherryTree/blob/main/Images/PdfToCherryTree_Run1.png)
![alt text](https://github.com/CoolHandSquid/PdfToCherryTree/blob/main/Images/PdfToCherryTree_Run2.png)
## Contact
* Please contact me at coolhandsquid@yahoo.com for suggestions and ideas! (I'd be willing to make this work for windows if asked nicely...)
