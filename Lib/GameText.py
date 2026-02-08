#  _    _   _ __  __ _____ _   _
# | |  | | | |  \/  | ____| \ | |
# | |  | | | | |\/| |  _| |  \| |
# | |__| |_| | |  | | |___| |\  |
# |_____\___/|_|  |_|_____|_| \_|
#
# Change list:
# * Improve Map List
# * Change the loading method of `../../Data/Text`
#

import Lumenx
import Bladex
import os
import Interpolator
import string

#
import typing
if typing.TYPE_CHECKING:
    apply = lambda fn, args=(), kwds={}: None
    execfile = lambda filename, globals=None, locals=None: None

Textos={}
MapList = {}
ComboNames = {
              "Knight_N"   : {},
              "Barbarian_N": {},
              "Amazon_N"   : {},
              "Dwarf_N"    : {},
              "Default"    : {},
             }
             
FADE_TIME=1.0

current_language=None

def SetLanguage(lang):
  global current_language
  # global MapList
  global ComboNames
  if lang != current_language:
    current_language= lang
    print "Setting language",lang
    # by Sryml
    lumen_root = Lumenx.GetLumenRoot()
    root = "Data/Locale/" + lang
    # files = []
    # for i in range(1,18):
    #    files.append("M%d.py" % i)
    # files = files + ["Combos.py","tutor.py"] # "map2D.py", "casa.py"
    # print "Executing files: ",files
    for file in ["Combos.py","GTexts.py"]:
      filepath = os.path.join(lumen_root, root, file)
      execfile(filepath, globals(), globals())

    if Lumenx.GetCurrentMod() != "":
      filepath = os.path.join(Lumenx.GetModRoot(), root, "Combos.py")
      if os.path.isfile(filepath):
        name_space = {}
        execfile(filepath, name_space, name_space)
        for k in ComboNames.keys():
          ComboNames[k].update(name_space["ComboNames"].get(k, {}))
    #


def MapDescriptor(map):
  import MenuText
  return MenuText.GetMenuText(Lumenx.GetMapListItem(map, ""))
  # if MapList.has_key(string.upper(map)):
  #   return MapList[string.upper(map)]
  # else:
  #   return map

FadeTextInstance = None # type: FadeText # type: ignore

class FadeText(Interpolator.LinearInt):
  def __init__(self,init_val,end_val):
    # by Sryml
    global FadeTextInstance
    if FadeTextInstance is not None:
      FadeTextInstance.Interpolator.Actions = []
      FadeTextInstance.Interpolator.__del__ = lambda: None
    FadeTextInstance = self
    #
    Interpolator.LinearInt.__init__(self,init_val,end_val)
    self.Interpolator=Interpolator.Interp("FadeText", 0)
    time=Bladex.GetTime()
    self.Interpolator.AddAction(time,time+FADE_TIME,self)
    self.end_val=end_val


  def Execute(self,value):
    import Scorer
    ret=Interpolator.LinearInt.Execute(self,value)
    Scorer.wGameText.SetAlpha(ret)


  def EndExecute(self):
    import Scorer
    self.Interpolator.Kill()
    Scorer.wGameText.SetAlpha(self.end_val)
    if self.end_val==0:
      Scorer.wGameText.SetText("")



def ClearText():
  FadeText(1,0)


def AbortText():
  import Scorer
  Bladex.RemoveScheduledFunc("ClearText")
  Bladex.RemoveScheduledFunc("NextText")
  Scorer.wGameText.SetAlpha(0)
  Scorer.wGameText.SetText("")



def WriteTextAux(txt,duration,init_r,init_g,init_b,next_text,ypos=None,patch=None):
  import Scorer
##  if not patch:
  if Scorer.VISIBLE==0:
    Scorer.wFrame.SetSize(10,10)
    Scorer.wFrame.RecalcLayout()
  
  Scorer.wGameText.SetColor(init_r,init_g,init_b)

  Scorer.wGameText.SetText(txt)
  if ypos!=None:
    Scorer.wFrame.MoveWidgetTo("GameTextWidget",0.5,ypos);
  else:
    Scorer.wFrame.MoveWidgetTo("GameTextWidget",0.5,27);
  Scorer.wFrame.RecalcLayout()

  FadeText(0,1)
  now=Bladex.GetTime()

  if next_text==[]:
    Bladex.AddScheduledFunc(now+duration,ClearText,(),"ClearText")
  else:
    Bladex.AddScheduledFunc(now+duration,ClearText,(),"ClearText")
    Bladex.AddScheduledFunc(now+duration+FADE_TIME,WriteTextAux,(next_text[0],duration,init_r,init_g,init_b,next_text[1:],ypos),"NextText")



def WriteText(txt_id,ypos=None):
  if not Bladex.GetSubtitlesEnable():
    return

  try:
    _txt=Textos[txt_id]
    txt=_txt[4]
  except:
    print "Error: can't print message",txt_id
    return

  nLines=string.count(txt,"\n")+1
  nParagraphs=(nLines/5)+1

  paragraphs=[]
  if nParagraphs>1:
    l=string.split(txt,"\n")
    counter=0
    t_str=""
    for i in l:
      t_str=t_str+i+"\n"
      counter=counter+1
      if counter==5:
        paragraphs.append(t_str)
        t_str=""
        counter=0
    if t_str!="":
      paragraphs.append(t_str)

    WriteTextAux(paragraphs[0],_txt[0],_txt[1],_txt[2],_txt[3],paragraphs[1:],ypos)
  else:
    WriteTextAux(txt,_txt[0],_txt[1],_txt[2],_txt[3],[],ypos)


def ShowMessage(message="",r=255,g=255,b=255):
	import Scorer
	Scorer.wGameText.SetText(message)
	Scorer.wGameText.SetAlpha(1.0)
	Scorer.wGameText.SetColor(r,g,b)
##	Scorer.wFrame.MoveWidgetTo("GameTextWidget",0.5,5)
	Scorer.wFrame.RecalcLayout()

def HideMessage():
	ShowMessage()

def GetComboName(EntityName,ComboId):
	kindName = Bladex.GetEntity(EntityName).Kind
	try:
		return ComboNames[kindName][ComboId]
	except:
		try:
			return ComboNames["Default"][ComboId]
		except:
			return None

