# PdfToCherryTree
* Convert a pdf file (or folder of pdf's) into a series of nodes in cherrytree. That cherrytree can be merged into a larger cherrytree. Linux only for now.
* PdfToCherryTree is a product of 19% security solutions
## Useage
* Synatx:     python3 PdfToCherry.py inputPdf outputCtd
* Example:    python3 /root/Desktop/Example.pdf /root/Desktop/TempCherryTree.ctd
* Note:       The goal of this tool is to turn the PDF into a node in a temporary CherryTree that you can then merge with your functional CherryTree.
* This tool will not parse nodes, or add to an existing CherryTree.
* This tool will only work on linux (could be ported with relative ease).
* Be sure to make your outfile a .ctd so cherrytree knows to open it as an unprotected xml.
![alt text](https://github.com/CoolHandSquid/PdfToCherryTree/Images/PdfToCherryTree_Run1)
![alt text](https://github.com/CoolHandSquid/PdfToCherryTree/Images/PdfToCherryTree_Run1)
## Build
* python3 -m pip install wand
## Contact
* Please contact me at coolhandsquid@yahoo.com for suggestions and ideas! (I'd be willing to make this work for windows if asked nicely...)
