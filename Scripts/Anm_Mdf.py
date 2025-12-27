#
# This file is to change the flags of an animations forever 
# It is appplied to preloaded animations AND animations Launched thoriguh


def Init():

    import Enm_Def
    import Bladex

    #                     Name      WUEA,MOD_Y,SOLF,COPY_ROT,BNG_MOV,HEADF
    # 
    # Cosita set
    #
    Bladex.AddAnimFlags("Cos_attack_f",0,0,0,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)
    Bladex.AddAnimFlags("Cos_g_01",1,0,1,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)
    Bladex.AddAnimFlags("Cos_fly",1,1,1,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ANM)
    Bladex.AddAnimFlags("Cos_dth_fly",1,1,1,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ANM)

    #                     Name      WUEA,MOD_Y,SOLF,COPY_ROT,BNG_MOV,HEADF
    # 
    # Spider set
    #
    Bladex.AddAnimFlags("Spd_g_01",1,0,1,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ENG)
    Bladex.AddAnimFlags("Cos_dth2",1,1,1,1,Enm_Def.BM_XYZ,Enm_Def.HEADF_ANM)
    #Bladex.AddAnimFlags("Bar_start_barbaros",1,0,0,0,Enm_Def.BM_XYZ,Enm_Def.HEADF_ANM)

