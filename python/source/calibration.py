from PIL import Image, ImageDraw, ImageFont

airplanetype='C208B'
client='Fuck Face'
agent='Dickhead'
mgh=20

my_image=Image.open("../Resources/GenericQuote.png")
title_font=ImageFont.truetype('../Resources/Calibri.ttf',30)
entry_font=ImageFont.truetype('../Resources/Calibri.ttf',18)
entry_font_bold=ImageFont.truetype('../Resources/Calibri_bold.ttf',18)

image_editable=ImageDraw.Draw(my_image)

#type insertion
image_editable.text((820,120),airplanetype,(0,0,0),font=title_font)

#prepared for insertion
image_editable.text((834,232),client,(0,0,0),font=entry_font)

#prepared by insertion
image_editable.text((834,252),agent,(0,0,0),font=entry_font)

#mgh insertion
image_editable.text((940,354),str(mgh),(0,0,0),font=entry_font)

#length insertion
image_editable.text((940,374),str(mgh),(0,0,0),font=entry_font)

#sector length insertion
image_editable.text((940,395),str(mgh),(0,0,0),font=entry_font)

#configuration insertion
image_editable.text((900,417),agent,(0,0,0),font=entry_font)

#flight cycle ratio insertion
image_editable.text((940,438),str(mgh),(0,0,0),font=entry_font)

#based abroad insertion
image_editable.text((113,458),str(mgh),(0,0,0),font=entry_font)

#proposed base insertion
image_editable.text((900,478),agent,(0,0,0),font=entry_font)

#includes crew p1 insertion
image_editable.text((113,498),str(mgh),(0,0,0),font=entry_font)

#includes crew p2 insertion
image_editable.text((940,498),str(mgh),(0,0,0),font=entry_font)

#pursers insertion
image_editable.text((113,518),str(mgh),(0,0,0),font=entry_font)

#flight engineer insertion
image_editable.text((113,538),str(mgh),(0,0,0),font=entry_font)

#crew positioning insertion
image_editable.text((113,558),str(mgh),(0,0,0),font=entry_font)

#crew accomodation insertion
image_editable.text((113,578),'Crew Accomodation Included',(0,0,0),font=entry_font)

#crew per diems insertion
image_editable.text((113,603),str(mgh),(0,0,0),font=entry_font)

#per diem insertion
image_editable.text((970,603),str(mgh),(0,0,0),font=entry_font)

#includes flight numbers insertion
image_editable.text((113,623),str(mgh),(0,0,0),font=entry_font)

#pax insurance insertion
image_editable.text((113,643),str(mgh),(0,0,0),font=entry_font)

#draw down insertion
image_editable.text((113,727),str(mgh),(0,0,0),font=entry_font)

#.text takes coordinates, input text, RGB font colour, and font

my_image.save("../Outputs/result.png")

#temp=Image.open("../Outputs/result.png")
#my_output=temp.convert('RGB')
#my_output.save('../Outputs/Finished_quote.pdf')
