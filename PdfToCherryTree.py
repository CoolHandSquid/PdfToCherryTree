#!/usr/bin/env python3
import os
import base64
import magic
import ntpath
import sys
import time
from wand.image import Image
from PyPDF2 import PdfFileReader

###Build
#python3 -m pip install wand
###

if len(sys.argv) != 3:
    print("""Synatx:     python3 PdfToCherry.py inputPdf outputCtd
Example:    python3 /root/Desktop/PdfDirOrPdf/ /root/Desktop/TempCherryTree.ctd
Note:       The goal of this tool is to turn the PDF into a node in a temporary CherryTree that you can then merge with your functional CherryTree.
You can put a folder in place of inputPdf and the tool will convert all Pdf's (and only Pdf's) into their own node in the outputCtd CherryTree.
This tool will not parse nodes, or add to an existing CherryTree.
This tool will only work on linux (could be ported with relative ease).
Be sure to make your outfile a .ctd so cherrytree knows to open it as an unprotected xml.""")
    quit()

indata  = sys.argv[1]
outfile = sys.argv[2]
node_Name   = ntpath.basename(outfile)[:-4]
uid     = 2

if os.path.isfile(outfile):
    print("File exists. Please do not point to an outfile a file that exists")
    exit()

#initialize .ctd file by writing to the variable writetofile
ctdHead     = '<?xml version="1.0" encoding="UTF-8"?>\n<cherrytree>\n  <bookmarks list=""/>\n  <node name="{}" unique_id="1" prog_lang="custom-colors" tags="" readonly="0" custom_icon_id="0" foreground="" ts_creation="{}" ts_lastsave="{}">\n'.format(node_Name, time.time(), time.time())
writetofile = ctdHead

def createnode(file):
    #createnode() Initializes a node, converts each page of a pdf into a png file, base64 encodes it, and then adds that base64 encoded png file to writetofile variable.
    #The writetofile variable is what is then written to the outfile and is opened by cherrytree.
    global writetofile                                                                                      #writetofile is what will be written to the .ctd file
    global uid                                                                                              #uid is used to iterate through uniqueid numbers
    writetofile = writetofile + '  <node name="{}" unique_id="{}" prog_lang="custom-colors" tags="" readonly="0" custom_icon_id="0" foreground="" ts_creation="{}" ts_lastsave="{}">\n'.format(filename, uid, time.time(), time.time())                 #begin a new node
    uid += 1                                                                                                #next uniqueid will be +1
    encoded_strings = []                                                                                    #encoded strings will be a list of base64 encoded png files. (each item will be a page of the pdf)
    all_pages   = Image(filename=file)                                                                      #all_pages is the pdf converted to Image format (wand)
    for pagenum, page in enumerate(all_pages.sequence):                                                     #for each page in the pdf
        pagenum += 1                                                                                        #iterate through page numbers (force start at page 1)
        with Image(page) as i:                                                                              #open page in Image format as i
            i.format        = 'png'                                                                         #force format to .png
            i.alpha_channel = 'remove'                                                                      #removes some of the transparency enacted pdf protections to prevent copying
            Image(i).save(filename="/dev/shm/temp.png")                                                     #saves the page in png format to /dev/shm/temp.png
            with open("/dev/shm/temp.png", "rb") as image_file:                                             #opens file and base64 encodes it
                encoded_string = base64.b64encode(image_file.read())
                encoded_strings.append(encoded_string.decode("utf-8"))
                image_file.close()
                os.system("rm /dev/shm/temp.png")                                                           #removes the temp png file
    ctdPerPage  = '    <rich_text justification="left"></rich_text>\n    <rich_text>\n</rich_text>\n'       #format needed for each page/png
    for i in range(len(encoded_strings)):                                                                   
        writetofile = writetofile + ctdPerPage
    offset = 0                                                                                              #inialize offset
    for i in range(len(encoded_strings)):
        writetofile = writetofile + '    <encoded_png char_offset="{}" justification="left" link="">{}</encoded_png>\n'.format(offset, encoded_strings.pop(0)) #add png
        offset += 3                                                                                         #increase offset by 3
    writetofile = writetofile + '  </node>\n'                                                               #close node

def status(file):
    with open(file, "rb") as pdf_file:
        pdf_reader = PdfFileReader(pdf_file)
        print("Converting {} page/s of {} into CherryTree.\n".format(pdf_reader.numPages, filename))

###<MAIN>###
#Identify if it is a file or a directory, Verify if each file is a PDF, if it is a pdf, send it to createnode().
#If there is no pdf exit without creating a .ctd file
#At the end of adding pdfs/nodes to the variable writetofile, add the closing to the xml file.
#open the outfile, write to it, close it.
#chmod the outfile and open it with cherrytree 
if os.path.isfile(indata):
    path        = ntpath.dirname(indata)
    filename    = ntpath.basename(indata)
    pnf         = indata
    if "PDF" in magic.from_file(pnf):
        status(pnf)
        createnode(pnf)
    else:
        print("Warning: {} is not a PDF".format(pnf))
        quit()
elif os.path.isdir(indata):
    path        = ntpath.dirname(indata)
    empty       = True
    for filename in os.listdir(indata):
        if filename.endswith(".pdf"):
            file = indata + "/" + filename
            if "PDF" in magic.from_file(file):
                status(file)
                createnode(file)
                empty = False
            else:
                print("Warning: {} is not a PDF".format(indata + "/" + filename))
                continue
        else:
            continue
    if empty == True:
        print("Warning: No PDF's found in {}".foramt(indata))
else:
    print("Hmmm, I'm having trouble finding this file/dir. Are you sure the path is correct?")
    quit()

ctdTail     = '  </node>\n  </cherrytree>'
writetofile = writetofile + ctdTail

f = open(outfile, "w")
f.write(writetofile)
f.close()

os.system('chmod 644 {}'.format(outfile))
os.system('cherrytree {}'.format(outfile))
###</MAIN>###
