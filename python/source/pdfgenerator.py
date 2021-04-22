#import sys

#usrinputs=[]

#for i in sys.argv[1:]:
#    usrinputs.append(float(i))
    
#print(usrinputs[0]*usrinputs[1])

from fpdf import FPDF

class PDF(FPDF):
    def lines(self):
        #could also add self.set_fill_colour(R,G,B) and add 'DF' to rect to add colour
        self.rect(5,5,pdf_w-10,pdf_h-10)
    def imagex(self):
        self.set_xy(pdf_w/3,50)
        self.image(name='logo.png',w=pdf_w/3)

#class PDF(FPDF):
#    pass

pdf=PDF()

pdf = PDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf_w=210
pdf_h=297


pdf.lines()
pdf.imagex()

pdf.ln(10)

th=10
col_width=(pdf_w)/6

data=[['Item','Cost'],['Fuel','$50'],['Insurance','$1000']]
pdf.set_font('Arial','B',15.0)

ypos=100

pdf.set_xy(pdf_w/3,ypos)

for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 2*th, str(datum), border=1)
    ypos+=20
    pdf.set_xy(pdf_w/3,ypos)

pdf.output('quote.pdf','F')
