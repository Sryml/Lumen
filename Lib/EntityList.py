



import Tkinter
import Pmw
import Bladex
import sys
#import bldb




#Bldb=bldb.Bldb()

class VectorEntry:
  def __init__(self,text_label,parent,dim=3,labels=["X","Y","Z"],width=12):
    w = Pmw.Group(parent, tag_text=text_label)
    w.pack( fill='x', expand = 1, padx = 4, pady = 4)
    self.dimension=dim

    self.Comp=[]
    for i in range(0,dim):
      self.Comp.append(
         Pmw.EntryField(w.interior(),
         entry_width = width,
         validate = {'validator' : 'real'},
         labelpos = 'w',
         label_text = labels[i])
        )
      self.Comp[i].grid(row=0, column=i)


  def setentry(self,s):
    if s is None:
      for i in range(0,self.dimension):
        self.Comp[i].setentry("")
    else:
      for i in range(0,self.dimension):
        self.Comp[i].setentry(s[i])




class VectorEntryEntity(VectorEntry):

  def SetEntry(self,entity,attribute):
    if hasattr(entity,attribute)==1:
      s=getattr(entity,attribute)
      VectorEntry.setentry(self,s)
    else:
      VectorEntry.setentry(self,None)
      







class EntitiesDialog:
  def __init__(self, parent):
    self.Parent=parent
    exitButton = Tkinter.Button(parent, text = 'Exit', command = parent.destroy)
    exitButton.pack(side = 'bottom')

    # Create and pack the MenuBar.
    menuBar = Pmw.MenuBar(parent,
          hull_relief = 'raised',
          hull_borderwidth = 1)
    menuBar.pack(fill = 'x')
    self.menuBar = menuBar

    # Add some buttons to the MenuBar.
    menuBar.addmenu('File', 'Close this window or exit')
    menuBar.addmenuitem('File', 'command', 'Close this window',
#        command = lambda: print('Action: close'),
        label = 'Close')

    menuBar.addmenuitem('File', 'command', 'Exit the application',
        command = self.CreateDOLFile,
        label = 'Create DOL File')

    menuBar.addmenuitem('File', 'separator')
    menuBar.addmenuitem('File', 'command', 'Exit the application',
#        command = lambda: print('Action: exit'),
        label = 'Exit')

    menuBar.addmenu('Edit', 'Cut, copy or paste')
    menuBar.addmenuitem('Edit', 'command', 'Delete the current selection',
#        command = lambda: print('Action: delete'),
        label = 'Delete')

    menuBar.addmenu('Options', 'Set user preferences')
    menuBar.addmenuitem('Options', 'command', 'Set general preferences',
#        command = lambda: print('Action: general options'),
        label = 'General...')


    pane = Pmw.PanedWidget(parent, hull_width=550, hull_height=300, orient='horizontal')
    pane.add('left')
    pane.add('right')
    pane.pack(expand = 1, fill = 'both')

    self.box = Pmw.ScrolledListBox(pane.pane("left"),
        listbox_selectmode='single',
	      label_text='Entities  '+str(Bladex.nEntities()),
        labelpos='nw',
        vscrollmode = 'static',
        selectioncommand=self.ListSelectionCommand)
    self.box.pack(fill = 'both', expand = 'yes', padx = 10, pady = 10)

    sf=Pmw.ScrolledFrame(pane.pane("right"))
    sf.pack(padx = 10, pady = 10, fill = 'both', expand = 1)
    sfframe = sf.getFrame()
    sfframe.configure(bg="SystemButtonFace")
    self.sfpr=sfframe

    EntList=range(Bladex.nEntities())
    for i in EntList:
      currEntity=Bladex.GetEntity(i)
      self.box.insert('end', currEntity.Name)


    ##### Tipo ##########
    self.Kind= Pmw.EntryField(sfframe,
      entry_width = 20,
      labelpos = 'w',
      label_text = 'Kind')
    self.Kind.pack(fill = "x", padx = 4, pady = 10)
    #self.Kind.grid(row=0, column=1)


    ##### Clase de Entidad ##########
    self.EntityClass = Pmw.OptionMenu ( sfframe,
      labelpos = 'w',
      labelmargin = 10,
      label_text = 'Entity Class :',
      #variable = self._var,
      items = ( 'Actor', 'Physic', 'Static', 'Weapon', "Arrow", "Person", "Other" ) )
    self.EntityClass.pack ( fill = "x", padx = 4, pady = 10 )

    ##### Posición ###########
    self.Pos=VectorEntryEntity("Position",sfframe,3)

    ##### Orientación ###########
    self.Ori=VectorEntryEntity("Orientation",sfframe,4,["a","b","c","d"],10)
    

    ##### Escala ##########
    self.Scale= Pmw.EntryField(sfframe,
      validate = {'validator' : 'real'},
      entry_width = 20,
      labelpos = 'w',
      label_text = 'Scale')
    self.Scale.pack(fill = "x", padx = 4, pady = 10)

    ##### Velocidad ##########
    self.Vel=VectorEntryEntity("Velocity",sfframe,3)

    ##### Gravedad ##########
    self.Grav=VectorEntryEntity("Gravity",sfframe,3)




  def FillDialog(self,entName):
    CurrEntity=Bladex.GetEntity(entName)
    self.Kind.setentry(CurrEntity.Kind)

    self.Pos.SetEntry(CurrEntity,"Position")
    self.Vel.SetEntry(CurrEntity,"Velocity")
    self.Grav.SetEntry(CurrEntity,"Gravity")
    self.Ori.SetEntry(CurrEntity,"Orientation")
    if CurrEntity.Actor==1:
      self.EntityClass.select(self.EntityClass.index("Actor"))
    elif CurrEntity.Static==1:
      self.EntityClass.select(self.EntityClass.index("Static"))
    elif CurrEntity.Weapon==1:
      self.EntityClass.select(self.EntityClass.index("Weapon"))
    elif CurrEntity.Arrow==1:
      self.EntityClass.select(self.EntityClass.index("Arrow"))
    elif CurrEntity.Person==1:
      self.EntityClass.select(self.EntityClass.index("Person"))
    elif CurrEntity.Physic==1:
      self.EntityClass.select(self.EntityClass.index("Physic"))
    else:
      self.EntityClass.select(self.EntityClass.index("Other"))


  def ListSelectionCommand(self):
    EntName=self.box.getcurselection()[0]
    self.FillDialog(EntName)


  def CreateDOLFile(self):
    import sys
    sys.path.append("C:/Program Files/Python/Lib/Lib-tk")
    import tkMessageBox.tkFileDialog
    filename = tkMessageBox.tkFileDialog.asksaveasfilename(parent=self.Parent,filetypes=[("Dol files","*.dol")])
    Create_DOLFile(filename)





def Create_DOLFile(FileName):
#  Bldb.set_trace()
  if FileName:
    temp_stdout=sys.stdout
    sys.stdout=open(FileName,"w")

  #print "# Archivo DOL generado a partir de Python\n"
  #print "NumItems ->",Bladex.nEntities()
  print "NumItems -> Hacer"
  print "\n\n"
  
  EntList=range(Bladex.nEntities())
  for i in EntList:
    currEntity=Bladex.GetEntity(i)
    if currEntity.Physic==1 or currEntity.Static==1:
      print "BeginObject"
      print "  Kind -> ",currEntity.Kind
      print "  Name -> ",currEntity.Name

      print "  Static -> ",currEntity.Static
      print "  Scale -> ",currEntity.Scale

      print "  Position -> ",currEntity.Position[0]/1000,-currEntity.Position[2]/1000,currEntity.Position[1]/1000
      print "  Orientation -> ",currEntity.Orientation[0],currEntity.Orientation[1],currEntity.Orientation[2],currEntity.Orientation[3]

      if currEntity.nFires:
        print "  nFires -> ",currEntity.nFires
        for fires in range(currEntity.nFires):
          print "    FireIntensity ->",fires,currEntity.FireIntensity[fires]

      if currEntity.nLights:
        print "  nLights -> ",currEntity.nLights
        for lights in range(currEntity.nLights):
          print "    LightIntensity ->",lights,currEntity.FireIntensity[lights]
          print "    LightPrecission ->",lights,currEntity.FireIntensity[lights]
          print "    LightColor ->",lights,currEntity.FireIntensity[lights]
          #print "    LightGlow ->",lights,currEntity.FireIntensity[lights]
          # Glow no implementado

      print "EndObject\n\n\n"

  if FileName:
    sys.stdout.close()
    sys.stdout=temp_stdout


def EntitiList():
  root = Tkinter.Tk()
  Pmw.initialise(root, fontScheme = 'pmw1')
  root.title('Entities List')

  widget = EntitiesDialog(root)
  root.mainloop()


# Create demo in root window for testing.
if __name__ == '__main__':
  EntitiList()
  #Create_DOLFile("Hola.dol")