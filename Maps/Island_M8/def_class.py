import Enm_Def
import Bladex
import Reference

#############################################
#     Definicion de la clase Prisionero     #
#############################################


class Prisoner(Enm_Def.StupidNPCPerson):
  def __init__(self, person):
    Enm_Def.StupidNPCPerson.__init__(self, person)
    self.Agonizando=0
    self.Muerto=0
    self.Desmaya(self.Name)

    self.agonia1prs=Bladex.CreateSound("../../Sounds/prisoner-cough2.wav", "Agonia1Prs")
    self.agonia1prs.Volume=1
    self.agonia1prs.Scale=1.112
    self.agonia1prs.MinDistance=500
    self.agonia1prs.MaxDistance=45000

    self.agonia2prs=Bladex.CreateSound("../../Sounds/killme.wav", "Agonia2Prs")
    self.agonia2prs.Volume=1
    self.agonia2prs.Scale=1.112
    self.agonia2prs.MinDistance=200
    self.agonia2prs.MaxDistance=45000

    self.muerteprs=Bladex.CreateSound("../../Sounds/knight-die.wav", "MuertePrs")
    self.muerteprs.Volume=1
    self.muerteprs.Scale=1.112
    self.muerteprs.MinDistance=1000
    self.muerteprs.MaxDistance=45000

  def Agoniza(self, entity_name):
    #print "Agoniza..."+entity_name
    if self.Muerto:
      return
    if self.Desmayado:
      self.Desmayado=0
    person=Bladex.GetEntity(entity_name)
    if entity_name=="PrisioneroVivo1":
      person.Wuea=Reference.WUEA_ENDED
      person.LaunchAnimation("Prs_agony01")
      person.SetOnFloor()
      agonia1prs.Play(person.Position[0], person.Position[1], person.Position[2], 0)
      self.Agonizando=1
    else:
      person.Wuea=Reference.WUEA_ENDED
      person.LaunchAnimation("Prs_agony02")
      person.SetOnFloor()
      agonia2prs.Play(person.Position[0], person.Position[1], person.Position[2], 0)
      self.Agonizando=2
    person.AnmEndedFunc=self.Desmaya

  def Desmaya(self, entity_name):
    #print "Desmayado..."+entity_name
    if self.Muerto:
      return
    self.Desmayado=1
    if self.Agonizando:
      self.Agonizando=0
    person=Bladex.GetEntity(entity_name)
    person.SetTmpAnmFlags(1, 1, 0, 0, 1, 1)
    if entity_name=="PrisioneroVivo1":
      person.Wuea=Reference.WUEA_ENDED
      person.LaunchAnimation("Prs_rlx_01")
      person.SetOnFloor()
    else:
      person.Wuea=Reference.WUEA_ENDED
      person.LaunchAnimation("Prs_rlx_02")
      person.SetOnFloor()

  def Muere(self, entity_name):
    print "Muere..."+entity_name
    if self.Desmayado:
      self.Desmayado=0
    if self.Agonizando:
      if self.Agonizando==1:
        agonia1prs.Stop()
      else:
        agonia2prs.Stop()
      self.Agonizando=0
    person=Bladex.GetEntity(entity_name)
    person.Wuea=Reference.WUEA_ENDED
    person.LaunchAnimation("Prs_dth")
    person.SetOnFloor()
    muerteprs.Play(person.Position[0], person.Position[1], person.Position[2], 0)
    self.Muerto=1
