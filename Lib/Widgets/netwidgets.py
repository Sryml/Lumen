import BUIx
import BVideo
import Raster
import BBLib
import math
import sys
import MenuWidget
import BInput
import ListWidget
import ScorerWidgets
import NetMisc
import Language

CharList = None
#print "arrecho"

def ChangePlayer(n):
	global CharList
	CharList.ChangeImage(n)

#
# Seleccion de personaje
################################
class B_ImageListWidget(BUIx.B_RectWidget):

	def __init__(self,Parent,MenuDescr,StackMenu):
		global CharList

		imagelist=MenuDescr["ImageList"]
		self.MaxHeight = None
		try:
			self.MaxHeight = MenuDescr["MaxHeight"]
		except:
			pass
		self.Bitmap={}
		self.IDX = imagelist[0][0]

		for i in imagelist:
			bitm = BBLib.B_BitMap24()
			bitm.ReadFromBMP(i[1])
			self.Bitmap[i[0]] = bitm

		self.vidw,self.vidh=self.Bitmap[self.IDX].GetDimension()
		BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],self.vidw,self.vidh)
		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)
		CharList = self
		self.IDX         = MenuDescr["GetCharType"]()


	def ChangeImage(self,name):
		self.IDX = name

	def Draw(self,x,y,time):
		Raster.SetPosition(x,y)
		self.vidw,self.vidh=self.Bitmap[self.IDX].GetDimension()
		if self.MaxHeight is None:
			Raster.DrawImage(self.vidw,self.vidh,"BGR","Normal",self.Bitmap[self.IDX].GetData());
		else:
			NewWidth = (float(self.vidw)/float(self.vidh))*self.MaxHeight
			Raster.SetPosition(x+(self.vidw - NewWidth)/2,y)
			Raster.DrawResizeImage(self.vidw,self.vidh,"BGR","Normal",self.Bitmap[self.IDX].GetData(), NewWidth, self.MaxHeight)
			self.DefDraw(x,y,time)

	def FinalRelease(self):
		global CharList
		CharList = None
		BUIx.B_RectWidget.FinalRelease(self)

	def AcceptsFocus(self):
		return 0

#
#  Seleccion de mapas
#############################################
class B_MapListWidget(BUIx.B_RectWidget,MenuWidget.B_MenuTreeItem):
	def __init__(self,Parent,MenuDescr,StackMenu):
		name=MenuDescr["LeftMap"]
		self.LeftMap       = BBLib.B_BitMap24()
		self.LeftMap.ReadFromBMP(name)
		self.LSize,garbage = self.LeftMap.GetDimension()

		name=MenuDescr["RightMap"]
		self.RightMap      = BBLib.B_BitMap24()
		self.RightMap.ReadFromBMP(name)
		self.RSize,garbage = self.RightMap.GetDimension()

		name=MenuDescr["SelMap"]
		self.SelMap      = BBLib.B_BitMap24()
		self.SelMap.ReadFromBMP(name)
		self.SSize,self.vidh = self.SelMap.GetDimension()

		name=MenuDescr["MarkMap"]
		self.MarkMap     = BBLib.B_BitMap24()
		self.MarkMap.ReadFromBMP(name)
		self.SSize,self.vidh = self.MarkMap.GetDimension()

		self.vidw = self.SSize*3+self.LSize+self.RSize

		imagelist = NetMisc.ActualizeMapsBitmaps()
		self.Bitmap=[]
		self.IDX = 0

		self.MapSetValue = MenuDescr["MapSetValue"]
		dta              = MenuDescr["MapGetValue"]()

		for i in imagelist:
			bitm = BBLib.B_BitMap24()
			bitm.ReadFromBMP(i[0])

			self.Bitmap.append([bitm,i[1],i[2],0])

			for j in dta:
				if j == i[2]:
					self.Bitmap[len(self.Bitmap)-1][3] = 1

		self.MapW,self.MapH = self.Bitmap[self.IDX][0].GetDimension()

		self.MapW = (self.SSize - self.MapW)/2
		self.MapH = (self.vidh  - self.MapH)/2

		BUIx.B_RectWidget.__init__(self,Parent,MenuDescr["Name"],self.vidw,self.vidh)
		MenuWidget.B_MenuTreeItem.__init__(self,MenuDescr,StackMenu)

		self.Selected=0
		self.Solid=0
		self.Border=0
		self.SetDrawFunc(self.Draw)

	def Draw(self,x,y,time):
		global LabelName
		if self.IDX == 0:
			first = len(self.Bitmap)-1
		else:
			first = self.IDX-1

		if self.IDX == len(self.Bitmap)-1:
			last = 0
		else:
			last = self.IDX+1

		if self.Bitmap[first][3]:
			Raster.SetPosition(x+self.SSize*0+self.LSize, y)
			Raster.DrawImage(self.SSize,self.vidh,"BGR","Normal",self.MarkMap.GetData())

		if self.Bitmap[self.IDX][3]:
			Raster.SetPosition(x+self.SSize*1+self.LSize, y)
			Raster.DrawImage(self.SSize,self.vidh,"BGR","Normal",self.MarkMap.GetData())

		if self.Bitmap[last][3]:
			Raster.SetPosition(x+self.SSize*2+self.LSize, y)
			Raster.DrawImage(self.SSize,self.vidh,"BGR","Normal",self.MarkMap.GetData())

		if self.GetHasFocus():
			Raster.SetPosition(x,y+self.MapH)
			Raster.DrawImage(self.LSize,self.vidh-2*self.MapH,"BGR","Normal",self.LeftMap.GetData())

			Raster.SetPosition(x+self.SSize*3+self.LSize, y+self.MapH)
			Raster.DrawImage(self.LSize,self.vidh-2*self.MapH,"BGR","Normal",self.RightMap.GetData())

			if int(time*5)%2 == 0:
				Raster.SetPosition(x+self.SSize*1+self.LSize, y)
				Raster.DrawImage(self.SSize,self.vidh,"BGR","Normal",self.SelMap.GetData())


		Raster.SetPosition(x+self.MapW+self.SSize*0+self.LSize, y+self.MapH)
		Raster.DrawImage(self.SSize-2*self.MapW,self.vidh-2*self.MapH,"BGR","Normal",self.Bitmap[first][0].GetData())


		Raster.SetPosition(x+self.MapW+self.SSize*1+self.LSize, y+self.MapH)
		Raster.DrawImage(self.SSize-2*self.MapW,self.vidh-2*self.MapH,"BGR","Normal",self.Bitmap[self.IDX][0].GetData())

		Raster.SetPosition(x+self.MapW+self.SSize*2+self.LSize, y+self.MapH)
		Raster.DrawImage(self.SSize-2*self.MapW,self.vidh-2*self.MapH,"BGR","Normal",self.Bitmap[last][0].GetData())

		self.DefDraw(x,y,time)

		LabelName = self.Bitmap[self.IDX][1]

	def IncMenuItem(self):
		self.IDX = self.IDX+1
		if self.IDX >= len(self.Bitmap):
			self.IDX = 0


	def DecMenuItem(self):
		self.IDX = self.IDX-1
		if self.IDX < 0:
			self.IDX = len(self.Bitmap)-1

	def ActivateItem(self,act):
		if not act:
			MenuWidget.B_MenuTreeItem.ActivateItem(self,act)
			return
		self.Bitmap[self.IDX][3] = not self.Bitmap[self.IDX][3]
		v = []
		for i in self.Bitmap:
			if i[3]:
				v.append(i[2])
		self.MapSetValue(v)


	def AcceptsFocus(self):
		return 1

def FullFillPassword(cad,char):
	res =""
	for x in range(len(cad)):
		res = res + char
	return res

#
#  Entrada de texto
#################################################
class B_InputBox(MenuWidget.B_MenuItemTextNoFX):
	def __init__(self,Parent,MenuDescr,StackMenu):
		MenuWidget.B_MenuItemTextNoFX.__init__(self,Parent,MenuDescr,StackMenu)
		mentirita = None

		self.Label    = MenuDescr["Name"]
		self.Input    = MenuDescr["GetInput"]()
		self.MaxSize  = MenuDescr["MaxSize"]
		self.SetInput = MenuDescr["SetInput"]

		self.IManager=BInput.GetInputManager()

		self.ListenerName=MenuDescr["Name"]+" Listener"
		self.Listener=BInput.B_InputListener(self.ListenerName) #No se puede heredar m�ltiple de una clase generada por SWIG
		self.Listener.SetPythonFunc(self.ListenDevice)
		self.Parent = Parent
		self.xx=-1

		if MenuDescr.has_key("PasswordChar"):
			self.PasswordChar = MenuDescr["PasswordChar"]
		else:
			self.PasswordChar = None

		try:
			self.Locked = MenuDescr["Locked"]()
		except:
			self.Locked = 0


	def Draw(self,x,y,time):
		cursor = ""
		if self.xx==-1:
			self.xx = x
			self.yy = y

		if self.GetVisible()==0:
			return

		#print "MenuItemText",self.Name()
		foc=self.GetHasFocus()
		if foc:
			self.SetColor(252,247,167)
			if not self.Locked:
				if((int(time*5)%2)==0):
					cursor = ">"
		else:
			self.SetColor(207,144,49)

		if self.PasswordChar:
			self.SetText(self.Label+" "+FullFillPassword(self.Input,self.PasswordChar)+cursor)
		else:
			self.SetText(self.Label+" "+self.Input+cursor)

		self.DefDraw(self.xx-self.MaxSize*3,self.yy,time)

	def SetHasFocus(self,foc):
		MenuWidget.B_MenuItemTextNoFX.SetHasFocus(self,foc)
		if self.Locked:
			return
		if(foc==1):
			self.BeginDefineKey()
		print "Let's Write!",foc

	def FinalRelease(self):
		self.Listener = None
		self.IManager = None
		self.Parent = None
		self.SetInput = None
		MenuWidget.B_MenuItemTextNoFX.FinalRelease(self)
		print "FinalRelease"

	def BeginDefineKey(self):
		keyb=self.IManager.GetAttachedDevice("Keyboard")
		keyb.AddListener(self.Listener)
		self.oldInputActionsSet=self.IManager.GetInputActionsSet()
		self.IManager.SetInputActionsSet("MenuRedefine")

	def EndDefineKey(self):
		self.IManager.SetInputActionsSet(self.oldInputActionsSet)
		self.oldInputActionsSet = None
		keyb=self.IManager.GetAttachedDevice("Keyboard")
		keyb.RemoveListener(self.ListenerName)

	def AddLetter(self,letra):
		if(len(self.Input)<self.MaxSize):
			self.Input = self.Input+letra

	def ActivateItem(self,act):
		if(act):
			self.Parent.NextFocus()
		MenuWidget.B_MenuItemTextNoFX.ActivateItem(self,act)

	def ListenDevice(self,x,y,z):
		if z==1.0:
			if x=="Enter":
				self.EndDefineKey()
				#self.Parent.NextFocus()
			elif x=="Down":
				self.EndDefineKey()
			elif x=="Tab":
				self.EndDefineKey()
			elif x=="Up":
				self.EndDefineKey()
			elif x=="Esc":
				self.EndDefineKey()
			elif x=="Backspace":
				largo = len(self.Input)
				if(largo!=0):
					self.Input = self.Input[0:largo-1]
			elif x=="Delete":
				self.Input = ""
			elif len(x)==1:
				self.AddLetter(x)
			elif x=="Decimal":
				self.AddLetter(".")
			elif x=="Period":
				self.AddLetter(".")
			elif x[0:6]=="Numpad":
				self.AddLetter(x[6])
			elif x[0:6]=="Space":
				self.AddLetter(" ")
			self.SetInput(self.Input)

	def __del__(self):
		print "Chau! input box"
		MenuWidget.B_MenuItemTextNoFX.__del__(self)


#
# Lista de servidores
###########################

LaListaDeServidores = None

class B_ServerListWidget(ListWidget.B_ListWidget):

	def __init__(self,Parent,Menudesc,StackMenu,VertPos=0):
		global LaListaDeServidores
		ListWidget.B_ListWidget.__init__(self,Parent,Menudesc,StackMenu,VertPos)
		self.StackMenu = StackMenu

		self.DownArrow.SetAlpha(1) # Parche, no funciona la llamada a AdjustScrollArrows() en AddMenuElement(),
		                           # hasta que lo averig�e.
		LaListaDeServidores = self
		self.SetDrawFunc(self.Draw)

	def Draw(self,x,y,time):
		#pdb.set_trace()
		self.SetClipDraw(1)
		self.DefDraw(x,y,time)

	def __del__(self):
		ListWidget.B_ListWidget.__del__(self)

	def FinalRelease(self):
		global LaListaDeServidores

		LaListaDeServidores = None
		self.StackMenu      = None
		ListWidget.B_ListWidget.FinalRelease(self)

	def SetList(self,lista):
		while(self.nWidgets()>0):
			self.RemoveWidget_Idx(0)

		self.nElements=0
		self.Position=0
		self.ListItems=[]
		self.VertPos=0
		self.ListSize=0
		self.WidgetsVPos=[]
		self.WidgetsHeights=[]

		self.Focus=None
		self.MenuItems=[]

		for i in lista:
			m_class=MenuWidget.B_MenuItemTextNoFX
			try:
				m_class=i["Kind"]
			except:
				pass

			wSubMenu=m_class(self,i,self.StackMenu)
			self.AddMenuElement(wSubMenu)

		self.SetFocus_Idx(0)

		self.UpArrow=BUIx.B_TextWidget(self,"UpArrow",chr(190),ScorerWidgets.font_server,Language.LetrasMenu)
		self.AddWidget(self.UpArrow,77,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
		                                 BUIx.B_FrameWidget.B_FR_AbsoluteTop,BUIx.B_FrameWidget.B_FR_Top)
		self.UpArrow.SetColor(207,144,49)
		self.UpArrow.SetAlpha(0.5)

		self.DownArrow=BUIx.B_TextWidget(self,"DownArrow",chr(191),ScorerWidgets.font_server,Language.LetrasMenu)
		self.AddWidget(self.DownArrow,77,0,BUIx.B_FrameWidget.B_FR_AbsoluteLeft,BUIx.B_FrameWidget.B_FR_Left,
		                                   BUIx.B_FrameWidget.B_FR_AbsoluteBottom,BUIx.B_FrameWidget.B_FR_Bottom)
		self.DownArrow.SetColor(207,144,49)
		self.DownArrow.SetAlpha(0.5)


class B_ServerLabel(MenuWidget.B_MenuItemTextNoFX):
	def __init__(self,Parent,MenuDescr,StackMenu,VertPos=0):

		MenuWidget.B_MenuItemTextNoFX.__init__(self,Parent,MenuDescr,StackMenu)

		self.name       = MenuDescr["Name"]
		self.NumPlayers = MenuDescr["NumPlayers"]
		self.MaxPlayers = MenuDescr["MaxPlayers"]
		self.Idx	= MenuDescr["Idx"]
		self.Join	= MenuDescr["Join"]

	def ActivateItem(self,act):
		if(act):
			self.Join(self.Name,self.NumPlayers,self.MaxPlayers,self.Idx)
		else:
			MenuWidget.B_MenuItemTextNoFX.ActivateItem(self,act)


	def Draw(self,x,y,time):

		if self.GetVisible()==0:
			return

		foc=self.GetHasFocus()
		if foc:
			self.SetColor(252,247,167)
		else:
			self.SetColor(207,144,49)

		self.SetText(self.name)
		self.DefDraw(x,y,time)

		if  self.MaxPlayers != 0:
			self.SetText(`self.NumPlayers`+" / "+`self.MaxPlayers`)
			self.DefDraw(x+250,y,time)
			self.SetText(self.name)

LabelName = ""

class B_DescriptorLabel(MenuWidget.B_MenuItemTextNoFX):
	def __init__(self,Parent,MenuDescr,StackMenu):
		MenuWidget.B_MenuItemTextNoFX.__init__(self,Parent,MenuDescr,StackMenu)
		self.SetDrawFunc(self.Draw)
		self.LastLevelName = ""
		self.Parent = Parent

	def Draw(self,x,y,time):
		global LabelName

		if self.GetVisible()==0:
			return

		if self.LastLevelName != LabelName:
			self.SetText(LabelName)
			self.Parent.RecalcLayout()
			self.LastLevelName = LabelName

		foc=self.GetHasFocus()
		if foc:
			self.SetColor(252,247,167)
		else:
			self.SetColor(207,144,49)
		self.SetAlpha(1.0)
		self.DefDraw(x,y,time)

	def AcceptsFocus(self):
		return 0
