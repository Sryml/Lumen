


import Scorer
import Bladex
import os
import Interpolator
import string


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
  global MapList
  global ComboNames
  if lang != current_language:
    current_language= lang
    print "Setting language",lang
    l_path="../../Data/Text/"+lang
    if not os.path.exists(l_path):
      return

    files=os.listdir(l_path)    
    for i in files:      
      file=l_path+"/"+str(i)
      if file[len(file)-3:]=='.py':
        execfile(file)

def MapDescriptor(map):
	if MapList.has_key(string.upper(map)):
		return MapList[string.upper(map)]
	else:
		return map


class FadeText(Interpolator.LinearInt):
  def __init__(self,init_val,end_val):
    Interpolator.LinearInt.__init__(self,init_val,end_val)
    self.Interpolator=Interpolator.Interp("FadeText")
    time=Bladex.GetTime()
    self.Interpolator.AddAction(time,time+FADE_TIME,self)
    self.end_val=end_val


  def Execute(self,value):
    ret=Interpolator.LinearInt.Execute(self,value)
    Scorer.wGameText.SetAlpha(ret)


  def EndExecute(self):
    self.Interpolator.Kill()
    Scorer.wGameText.SetAlpha(self.end_val)
    if self.end_val==0:
      Scorer.wGameText.SetText("")



def ClearText():
  FadeText(1,0)


def AbortText():
  Bladex.RemoveScheduledFunc("ClearText")
  Bladex.RemoveScheduledFunc("NextText")
  Scorer.wGameText.SetAlpha(0)
  Scorer.wGameText.SetText("")



def WriteTextAux(txt,duration,init_r,init_g,init_b,next_text,ypos=None,patch=None):

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

