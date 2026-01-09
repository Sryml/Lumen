##///
##||| MATERIAL.PY TITANIUM
##||| Change list:
##||| * Added empty potions to the list for default materials.
##||| * Added random pitch.
##||| * Added  Barb_M1 and Orc_M9 bridges.
##||| * Metal torch is now actually metal.
##||| * Added reinforced boxes.
##||| * Added missing shields (KingShield, Barbarian Shield).
##||| * Added some other misc items to have a default material.
##||| * Added all missing weapons (amazon stuff, some special weapons, etc.)
##|||
##||| Lumen - Material.py
##||| * Fixed material assignment in `Maps/csv.dat`.
##\\\ 



def Init():
    import Bladex

    # **********************************
    # *           Materiales           *
    # **********************************


    # *** Creaci�n de sonidos ***

    s=Bladex.CreateSound('../../sounds/golpe-madera-ligera.wav', 'GolpeMaderaLigera')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -4000, 4000, 0, 0)
    mat=Bladex.CreateMaterial('madera ligera')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-madera-mediana.wav', 'GolpeMaderaMediana')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('madera mediana')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-madera-pesada.wav', 'GolpeMaderaPesada')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('madera pesada')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-metal-ligero.wav', 'GolpeMetalLigero')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('metal ligero')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-metal-mediano.wav', 'GolpeMetalMediano')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('metal mediano')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-metal-pesado.wav', 'GolpeMetalPesado')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('metal pesado')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-piedra-ligera.wav', 'GolpePiedraLigera')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('piedra ligera')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-piedra-mediana.wav', 'GolpePiedraMediana')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('piedra mediana')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-piedra-pesada.wav', 'GolpePiedraPesada')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('piedra pesada')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-generico2.wav', 'GolpeGenerico2')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('generico2')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-cristal.wav', 'GolpeCristal')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('cristal')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-hueso.wav', 'GolpeHueso')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -4000, 4000, 0, 0)
    mat=Bladex.CreateMaterial('hueso')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-ceramica-ligera.wav', 'GolpeCeramicaLigera')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -4000, 4000, 0, 0)
    mat=Bladex.CreateMaterial('ceramica ligera')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-ceramica-mediana.wav', 'GolpeCeramicaMediana')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -4000, 4000, 0, 0)
    mat=Bladex.CreateMaterial('ceramica mediana')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-ceramica-pesada.wav', 'GolpeCeramicaPesada')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('ceramica pesada')
    mat.HitSound=s

    s=Bladex.CreateSound('../../sounds/golpe-carne.wav', 'GolpeCarne')
    s.SendNotify=1
    s.MinDistance=1000
    s.MaxDistance=15000
    s.SetPitchVar(1, -8000, 8000, 0, 0)
    mat=Bladex.CreateMaterial('carne')
    mat.HitSound=s





















    # *** Asignaci�n de materiales ***


    # *** Madera ligera  ***

    Bladex.SetDefaultMaterial('Antorcha', 'madera ligera')
    Bladex.SetDefaultMaterial('Boingtotem2', 'madera ligera')
    Bladex.SetDefaultMaterial('Flecha', 'madera ligera')
    Bladex.SetDefaultMaterial('FlechaEnvenenada', 'madera ligera')
    Bladex.SetDefaultMaterial('FlechaFuego', 'madera ligera')
    Bladex.SetDefaultMaterial('PuenteFernando', 'madera ligera')
    Bladex.SetDefaultMaterial('Rama1', 'madera ligera')
    Bladex.SetDefaultMaterial('Rama2', 'madera ligera')
    Bladex.SetDefaultMaterial('Silla', 'madera ligera')
    Bladex.SetDefaultMaterial('VigaPlana', 'madera ligera')


    # *** Madera mediana ***
    Bladex.SetDefaultMaterial('Arco', 'madera mediana')
    Bladex.SetDefaultMaterial('Arco2', 'madera mediana')
    Bladex.SetDefaultMaterial('Arco3', 'madera mediana')
    Bladex.SetDefaultMaterial('Astillas1', 'madera mediana')
    Bladex.SetDefaultMaterial('Astillas2', 'madera mediana')
    Bladex.SetDefaultMaterial('Astillas3', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza1', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza2', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza3', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza4', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza5', 'madera mediana')
    Bladex.SetDefaultMaterial('BarrilPieza6', 'madera mediana')
    Bladex.SetDefaultMaterial('Baston3', 'madera mediana')
    Bladex.SetDefaultMaterial('Bo', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza1', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza2', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza3', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza4', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza5', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza6', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza7', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza8', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza9', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza10', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza11', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza12', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza13', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza14', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza15', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza16', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza17', 'madera mediana')
    Bladex.SetDefaultMaterial('CajonPieza18', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza1', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza2', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza3', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza4', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza5', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza6', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza7', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza8', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza9', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza10', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza11', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza12', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza13', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza14', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza15', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza16', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza17', 'madera mediana')
    Bladex.SetDefaultMaterial('CajamaPieza18', 'madera mediana')
    Bladex.SetDefaultMaterial('Cubo', 'madera mediana')
    Bladex.SetDefaultMaterial('Cofrepeque', 'madera mediana')
    Bladex.SetDefaultMaterial('CrushBo', 'madera mediana')
    Bladex.SetDefaultMaterial('Escudo2', 'madera mediana')
    Bladex.SetDefaultMaterial('Garropin', 'madera mediana')
    Bladex.SetDefaultMaterial('Garrote', 'madera mediana')
    Bladex.SetDefaultMaterial('Garrote2', 'madera mediana')
    Bladex.SetDefaultMaterial('Hoguera', 'madera mediana')
    Bladex.SetDefaultMaterial('Mesita', 'madera mediana')
    Bladex.SetDefaultMaterial('Palanca2', 'madera mediana')
    Bladex.SetDefaultMaterial('Taburete', 'madera mediana')
    Bladex.SetDefaultMaterial('Timon', 'madera mediana')
    Bladex.SetDefaultMaterial('Escudo9', 'madera mediana')      # Added -LeadHead
    Bladex.SetDefaultMaterial('Bichero', 'madera mediana')      #



    # *** Madera pesada  ***
    Bladex.SetDefaultMaterial('Arbolseco', 'madera pesada')
    Bladex.SetDefaultMaterial('Arbolseco2', 'madera pesada')
    Bladex.SetDefaultMaterial('ArbolNevado2', 'madera pesada')      # Added -LeadHead
    Bladex.SetDefaultMaterial('Armero', 'madera pesada')
    Bladex.SetDefaultMaterial('Barril', 'madera pesada')
    Bladex.SetDefaultMaterial('Cajama', 'madera pesada')
    Bladex.SetDefaultMaterial('Cajon', 'madera pesada')
    Bladex.SetDefaultMaterial('Cajon2', 'madera pesada')
    Bladex.SetDefaultMaterial('Cofre', 'madera pesada')
    Bladex.SetDefaultMaterial('Mesa', 'madera pesada')
    Bladex.SetDefaultMaterial('Meson', 'madera pesada')
    Bladex.SetDefaultMaterial('RhinoClub', 'madera pesada')
    Bladex.SetDefaultMaterial('Caja_i_i', 'madera pesada')          # Added
    Bladex.SetDefaultMaterial('Caja_i_r', 'madera pesada')          # 
    Bladex.SetDefaultMaterial('PuenteAurelio', 'madera pesada')     # 
    Bladex.SetDefaultMaterial('Puenteau_Plano', 'madera pesada')    #       -LeadHead





    # *** Metal ligero   ***
    Bladex.SetDefaultMaterial('Antorcha2', 'metal ligero')
    Bladex.SetDefaultMaterial('Amuletofantasma', 'metal ligero')
    Bladex.SetDefaultMaterial('Amuletoserpiente', 'metal ligero')
    Bladex.SetDefaultMaterial('Argolla', 'metal ligero')
    Bladex.SetDefaultMaterial('Caliz', 'metal ligero')
    Bladex.SetDefaultMaterial('Candil', 'metal ligero')
    Bladex.SetDefaultMaterial('Canica', 'metal ligero')
    Bladex.SetDefaultMaterial('Casco3', 'metal ligero')
    Bladex.SetDefaultMaterial('Casco5', 'metal ligero')
    Bladex.SetDefaultMaterial('Casco4', 'metal ligero')
    Bladex.SetDefaultMaterial('Corona', 'metal ligero')
    Bladex.SetDefaultMaterial('Cincel', 'metal ligero')
    Bladex.SetDefaultMaterial('Cuchillo', 'metal ligero')
    Bladex.SetDefaultMaterial('Crosspear', 'metal ligero')       # Added
    Bladex.SetDefaultMaterial('Daga', 'metal ligero')
    Bladex.SetDefaultMaterial('Dagarrojar', 'metal ligero')
    Bladex.SetDefaultMaterial('Farol', 'metal ligero')
    Bladex.SetDefaultMaterial('Farol2', 'metal ligero')
    Bladex.SetDefaultMaterial('Gancho', 'metal ligero')
    Bladex.SetDefaultMaterial('Garfio2', 'metal ligero')
    Bladex.SetDefaultMaterial('Garfio', 'metal ligero')
    Bladex.SetDefaultMaterial('Lampared', 'metal ligero')
    Bladex.SetDefaultMaterial('Llave', 'metal ligero')
    Bladex.SetDefaultMaterial('Llavecob', 'metal ligero')
    Bladex.SetDefaultMaterial('Llavecobox', 'metal ligero')
    Bladex.SetDefaultMaterial('Llavecutre', 'metal ligero')
    Bladex.SetDefaultMaterial('Llavedor', 'metal ligero')       # Added
    Bladex.SetDefaultMaterial('Llavepla', 'metal ligero')       #       -LeadHead
    Bladex.SetDefaultMaterial('Llavemaz', 'metal ligero')
    Bladex.SetDefaultMaterial('LlaveAmarilla', 'metal ligero')
    Bladex.SetDefaultMaterial('MartilloForja', 'metal ligero')
    Bladex.SetDefaultMaterial('Suriken', 'metal ligero')
    Bladex.SetDefaultMaterial('Candelpeque', 'metal ligero')   # Added
    Bladex.SetDefaultMaterial('Tacita', 'metal ligero')        #
    Bladex.SetDefaultMaterial('Cazo', 'metal ligero')          #        -LeadHead
    Bladex.SetDefaultMaterial('Chakram', 'metal ligero')       #
    Bladex.SetDefaultMaterial('Chakram2', 'metal ligero')      #
    Bladex.SetDefaultMaterial('DeathKatar', 'metal ligero')    #
    Bladex.SetDefaultMaterial('Katar', 'metal ligero')         #
    Bladex.SetDefaultMaterial('KatarDoble', 'metal ligero')    #
    Bladex.SetDefaultMaterial('KatarMoon', 'metal ligero')     #





    # *** Metal  mediano ***
    Bladex.SetDefaultMaterial('Antorchaenpared', 'metal mediano')   # Moved to metal from wood
    Bladex.SetDefaultMaterial('Axpear', 'metal mediano')            #
    Bladex.SetDefaultMaterial('Arpon', 'metal mediano')             #
    Bladex.SetDefaultMaterial('Candelabro', 'metal mediano')        # Added         -LeadHead
    Bladex.SetDefaultMaterial('Alabarda', 'metal mediano')
    Bladex.SetDefaultMaterial('Bloodbol', 'metal mediano')
    Bladex.SetDefaultMaterial('Brasero1', 'metal mediano')
    Bladex.SetDefaultMaterial('BladeSword', 'metal mediano')        # Added
    Bladex.SetDefaultMaterial('BladeSword2', 'metal mediano')        # Added
    Bladex.SetDefaultMaterial('BladeSwordBarbarian', 'metal mediano')        # Added
    Bladex.SetDefaultMaterial('BladeSword2Barbarian', 'metal mediano')        # Added
    Bladex.SetDefaultMaterial('CandilAurelio', 'metal mediano')
    Bladex.SetDefaultMaterial('Candil2', 'metal mediano')
    Bladex.SetDefaultMaterial('Cimitarra', 'metal mediano')
    Bladex.SetDefaultMaterial('Coraza1', 'metal mediano')
    Bladex.SetDefaultMaterial('Coraza2', 'metal mediano')
    Bladex.SetDefaultMaterial('Coraza3', 'metal mediano')
    Bladex.SetDefaultMaterial('CrushHammer', 'metal mediano')
    Bladex.SetDefaultMaterial('Dagesse', 'metal mediano')
    Bladex.SetDefaultMaterial('DeathBo', 'metal mediano')
    Bladex.SetDefaultMaterial('DoubleSword', 'metal mediano')
    Bladex.SetDefaultMaterial('DalShield', 'metal mediano')         # Added
    Bladex.SetDefaultMaterial('Espada', 'metal mediano')
    Bladex.SetDefaultMaterial('EgyptSword', 'metal mediano')
    Bladex.SetDefaultMaterial('Espadafilo', 'metal mediano')
    Bladex.SetDefaultMaterial('Espadacurva', 'metal mediano')
    Bladex.SetDefaultMaterial('Espadaelfica', 'metal mediano')
    Bladex.SetDefaultMaterial('EspadaMagica1', 'metal mediano')
    Bladex.SetDefaultMaterial('EspadaMagica2', 'metal mediano')
    Bladex.SetDefaultMaterial('EspadaMagica3', 'metal mediano')
    Bladex.SetDefaultMaterial('Espadaromana', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo1', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo3', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo4', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo5', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo6', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo7', 'metal mediano')
    Bladex.SetDefaultMaterial('Escudo8', 'metal mediano')
    Bladex.SetDefaultMaterial('KingShield', 'metal mediano')    # Added     -LeadHead
    Bladex.SetDefaultMaterial('FireAxe', 'metal mediano')
    Bladex.SetDefaultMaterial('FireSword', 'metal mediano')     # Added
    Bladex.SetDefaultMaterial('FireBo', 'metal mediano')
    Bladex.SetDefaultMaterial('Gancholamp', 'metal mediano')
    Bladex.SetDefaultMaterial('Gladius', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha2', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha3', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha4', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha5', 'metal mediano')
    Bladex.SetDefaultMaterial('Hacha6', 'metal mediano')
    Bladex.SetDefaultMaterial('Hachacuchilla', 'metal mediano')
    Bladex.SetDefaultMaterial('HookSword', 'metal mediano')
    Bladex.SetDefaultMaterial('Keysup', 'metal mediano')
    Bladex.SetDefaultMaterial('Katana', 'metal mediano')
    Bladex.SetDefaultMaterial('Lamparaegipto', 'metal mediano')
    Bladex.SetDefaultMaterial('LamparaMiguel', 'metal mediano')
    Bladex.SetDefaultMaterial('LamparaNegra', 'metal mediano')
    Bladex.SetDefaultMaterial('Lamparacobra', 'metal mediano')
    Bladex.SetDefaultMaterial('LamparaMiguelsinpeana', 'metal mediano')
    Bladex.SetDefaultMaterial('LamparaAurelio', 'metal mediano')
    Bladex.SetDefaultMaterial('Lampcolg', 'metal mediano')
    Bladex.SetDefaultMaterial('Lanza', 'metal mediano')
    Bladex.SetDefaultMaterial('LanzaAncha', 'metal mediano')    # Added
    Bladex.SetDefaultMaterial('LightEdge', 'metal mediano')
    Bladex.SetDefaultMaterial('Martillo', 'metal mediano')
    Bladex.SetDefaultMaterial('Martillo2', 'metal mediano')
    Bladex.SetDefaultMaterial('Martillo3', 'metal mediano')
    Bladex.SetDefaultMaterial('Maza', 'metal mediano')
    Bladex.SetDefaultMaterial('Maza2', 'metal mediano')
    Bladex.SetDefaultMaterial('Maza3', 'metal mediano')
    Bladex.SetDefaultMaterial('MazaDoble', 'metal mediano')
    Bladex.SetDefaultMaterial('Naginata', 'metal mediano')
    Bladex.SetDefaultMaterial('Naginata2', 'metal mediano')
    Bladex.SetDefaultMaterial('Ninjato', 'metal mediano')
    Bladex.SetDefaultMaterial('Orksword', 'metal mediano')
    Bladex.SetDefaultMaterial('QueenSword', 'metal mediano')
    Bladex.SetDefaultMaterial('KingSword', 'metal mediano')     # Added -LeadHead
    Bladex.SetDefaultMaterial('Reja', 'metal mediano')
    Bladex.SetDefaultMaterial('Rastrillo', 'metal mediano')
    Bladex.SetDefaultMaterial('Semipuxero', 'metal mediano')
    Bladex.SetDefaultMaterial('SteelFeather', 'metal mediano')
    Bladex.SetDefaultMaterial('TaiSword', 'metal mediano')
    Bladex.SetDefaultMaterial('Tridente', 'metal mediano')
    Bladex.SetDefaultMaterial('Varilla', 'metal mediano')
    Bladex.SetDefaultMaterial('Varillaancha', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita1', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita2', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita5', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita6', 'metal mediano')
    Bladex.SetDefaultMaterial('Varita7', 'metal mediano')
    Bladex.SetDefaultMaterial('VampWeapon', 'metal mediano')







    # *** Metal pesado   ***
    Bladex.SetDefaultMaterial('Alfanje', 'metal pesado')
    Bladex.SetDefaultMaterial('BarroteAurelio', 'metal pesado')
    Bladex.SetDefaultMaterial('BigSword', 'metal pesado')
    Bladex.SetDefaultMaterial('Chaosword', 'metal pesado')
    Bladex.SetDefaultMaterial('DalBlade', 'metal pesado')
    Bladex.SetDefaultMaterial('DalWeapon', 'metal pesado')
    Bladex.SetDefaultMaterial('DeathSword', 'metal pesado')
    Bladex.SetDefaultMaterial('Eclipse', 'metal pesado')
    Bladex.SetDefaultMaterial('FireBigSword', 'metal pesado')
    Bladex.SetDefaultMaterial('FlatSword', 'metal pesado')
    Bladex.SetDefaultMaterial('Guadanya', 'metal pesado')
    Bladex.SetDefaultMaterial('Hacha2hojas', 'metal pesado')
    Bladex.SetDefaultMaterial('Hacharrajada', 'metal pesado')
    Bladex.SetDefaultMaterial('LeonBronce', 'metal pesado')
    Bladex.SetDefaultMaterial('LongSword', 'metal pesado')
    Bladex.SetDefaultMaterial('PinchoManuel', 'metal pesado')
    Bladex.SetDefaultMaterial('Sablazo', 'metal pesado')
    Bladex.SetDefaultMaterial('SawSword', 'metal pesado')
    Bladex.SetDefaultMaterial('Yunque', 'metal pesado')
    Bladex.SetDefaultMaterial('Escudon', 'metal pesado')        # Added 



    # *** Piedra ligera  ***
    Bladex.SetDefaultMaterial('CristalMineral', 'piedra ligera')
    Bladex.SetDefaultMaterial('Gema', 'piedra ligera')


    # *** Piedra mediana ***
    Bladex.SetDefaultMaterial('Bloque', 'piedra mediana')
    Bladex.SetDefaultMaterial('Gozne', 'piedra mediana')
    Bladex.SetDefaultMaterial('Palanca', 'piedra mediana')


    # *** Piedra pesada  ***
    Bladex.SetDefaultMaterial('AntorchaAtlante', 'piedra pesada')
    Bladex.SetDefaultMaterial('Cabezon', 'piedra pesada')
    Bladex.SetDefaultMaterial('Cebolla', 'piedra pesada')
    Bladex.SetDefaultMaterial('Columna', 'piedra pesada')
    Bladex.SetDefaultMaterial('Columnaestrecha', 'piedra pesada')
    Bladex.SetDefaultMaterial('Halcon', 'piedra pesada')
    Bladex.SetDefaultMaterial('Halcon2', 'piedra pesada')
    Bladex.SetDefaultMaterial('LapidaManuel', 'piedra pesada')
    Bladex.SetDefaultMaterial('Monjema', 'piedra pesada')
    Bladex.SetDefaultMaterial('Peanapiedra', 'piedra mediana')
    Bladex.SetDefaultMaterial('Roca1', 'piedra pesada')
    Bladex.SetDefaultMaterial('Roca2', 'piedra pesada')
    Bladex.SetDefaultMaterial('Roca3', 'piedra pesada')
    Bladex.SetDefaultMaterial('Roca1Aurelio', 'piedra pesada')
    Bladex.SetDefaultMaterial('Roca2Aurelio', 'piedra pesada')
    Bladex.SetDefaultMaterial('Tronoliso', 'piedra pesada')
    Bladex.SetDefaultMaterial('TronoEscarabeu', 'piedra pesada')



    # *** Hueso          ***
    Bladex.SetDefaultMaterial('Cracorn1', 'hueso')
    Bladex.SetDefaultMaterial('CraneoCornudo3', 'hueso')
    Bladex.SetDefaultMaterial('CraneoCornudo4', 'hueso')
    Bladex.SetDefaultMaterial('Femur', 'hueso')
    Bladex.SetDefaultMaterial('Restos', 'hueso')
    Bladex.SetDefaultMaterial('Skull', 'hueso')


    # *** Cristal        ***
    Bladex.SetDefaultMaterial('Botella', 'cristal')
    Bladex.SetDefaultMaterial('Botella2', 'cristal')
    Bladex.SetDefaultMaterial('BotellaVerde', 'cristal')
    Bladex.SetDefaultMaterial('IceWand', 'cristal')   ### Added -LeadHead
    Bladex.SetDefaultMaterial('IceAxe', 'cristal')
    Bladex.SetDefaultMaterial('IceHammer', 'cristal')
    Bladex.SetDefaultMaterial('IceSword', 'cristal')
    Bladex.SetDefaultMaterial('Pocima100', 'cristal')
    Bladex.SetDefaultMaterial('Pocima50', 'cristal')
    Bladex.SetDefaultMaterial('Pocima25', 'cristal')
    Bladex.SetDefaultMaterial('Pocima200', 'cristal')
    Bladex.SetDefaultMaterial('PocimaTodo', 'cristal')
    Bladex.SetDefaultMaterial('PowerPotion', 'cristal')
    
    Bladex.SetDefaultMaterial('Antidoto', 'cristal')
    Bladex.SetDefaultMaterial('LlaveBlanca', 'cristal')
    
    Bladex.SetDefaultMaterial('Pocima25_E', 'cristal') ### Empty potions -LeadHead
    Bladex.SetDefaultMaterial('Pocima50_E', 'cristal')
    Bladex.SetDefaultMaterial('Pocima100_E', 'cristal')
    Bladex.SetDefaultMaterial('Pocima200_E', 'cristal')
    Bladex.SetDefaultMaterial('PocimaTodo_E', 'cristal')
    Bladex.SetDefaultMaterial('PowerPotion_E', 'cristal')    
    
    
    
    # *** Ceramica ligera***    
    # Even though the material was created, it was completely unused -LeadHead
    Bladex.SetDefaultMaterial('Jarra', 'ceramica ligera')
    Bladex.SetDefaultMaterial('BotellaSagrada', 'ceramica ligera') # Added -LeadHead
    
    
    # *** Ceramica mediana***

    Bladex.SetDefaultMaterial('Mortero', 'ceramica mediana')
    Bladex.SetDefaultMaterial('Palangana', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza1', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza2', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza3', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza4', 'ceramica mediana')
    Bladex.SetDefaultMaterial('TinajaPieza5', 'ceramica mediana')
    
    # *** Ceramica pesada***
    Bladex.SetDefaultMaterial('Tinaja', 'ceramica pesada')




    # *** Carne          ***
    Bladex.SetDefaultMaterial('VampShield', 'carne')

    # *** Generico       ***
    Bladex.SetDefaultMaterial('Alforjas', 'generico2')
    Bladex.SetDefaultMaterial('Cirio', 'generico2')
    Bladex.SetDefaultMaterial('Libro', 'generico2')
    Bladex.SetDefaultMaterial('Libro2', 'generico2')    # Added
    Bladex.SetDefaultMaterial('Libro3', 'generico2')    #       -LeadHead
    Bladex.SetDefaultMaterial('Saquito', 'generico2')
    Bladex.SetDefaultMaterial('RollodeCuerda', 'generico2')     # Added
    Bladex.SetDefaultMaterial('Cantimplora','generico2')        #

    # by Sryml: start
    Bladex.SetDefaultMaterial("Libroabierto", "carne")

    Bladex.SetDefaultMaterial("Gemaazul", "cristal")
    Bladex.SetDefaultMaterial("Gemapurpura", "cristal")
    Bladex.SetDefaultMaterial("Gemaroja", "cristal")
    Bladex.SetDefaultMaterial("Pivote", "cristal")

    Bladex.SetDefaultMaterial("Camapaja", "generico2")
    Bladex.SetDefaultMaterial("Camavampiro", "generico2")
    Bladex.SetDefaultMaterial("Carcaj", "generico2")
    Bladex.SetDefaultMaterial("Cuerda", "generico2")
    Bladex.SetDefaultMaterial("CuerdaLarguisima", "generico2")
    Bladex.SetDefaultMaterial("Fuelle", "generico2")
    Bladex.SetDefaultMaterial("Libroabierto2", "generico2")
    Bladex.SetDefaultMaterial("Pendon1", "generico2")
    Bladex.SetDefaultMaterial("Pendon2", "generico2")
    Bladex.SetDefaultMaterial("Pendon3", "generico2")
    Bladex.SetDefaultMaterial("Pendon4", "generico2")
    Bladex.SetDefaultMaterial("Pergamino2", "generico2")
    Bladex.SetDefaultMaterial("Pergamino", "generico2")
    Bladex.SetDefaultMaterial("Pluma", "generico2")
    Bladex.SetDefaultMaterial("Tapiz", "generico2")
    Bladex.SetDefaultMaterial("Tapiz2", "generico2")
    Bladex.SetDefaultMaterial("Tapiz3", "generico2")
    Bladex.SetDefaultMaterial("Velon", "generico2")

    Bladex.SetDefaultMaterial("Costilla", "hueso")
    Bladex.SetDefaultMaterial("Cracorn2", "hueso")

    Bladex.SetDefaultMaterial("Armero2", "madera ligera")
    Bladex.SetDefaultMaterial("Armero2Pieza1", "madera ligera")
    Bladex.SetDefaultMaterial("Armero2Pieza2", "madera ligera")
    Bladex.SetDefaultMaterial("Armero2Pieza3", "madera ligera")
    Bladex.SetDefaultMaterial("Armero2Pieza4", "madera ligera")
    Bladex.SetDefaultMaterial("Armero2Pieza5", "madera ligera")
    Bladex.SetDefaultMaterial("ArmeroPieza1", "madera ligera")
    Bladex.SetDefaultMaterial("ArmeroPieza2", "madera ligera")
    Bladex.SetDefaultMaterial("ArmeroPieza3", "madera ligera")
    Bladex.SetDefaultMaterial("ArmeroPieza4", "madera ligera")
    Bladex.SetDefaultMaterial("Atril", "madera ligera")
    Bladex.SetDefaultMaterial("Baston", "madera ligera")
    Bladex.SetDefaultMaterial("Baston2", "madera ligera")
    Bladex.SetDefaultMaterial("LlaveMarron", "madera ligera")
    Bladex.SetDefaultMaterial("ButacaMago", "madera ligera")
    Bladex.SetDefaultMaterial("Camabad", "madera ligera")
    Bladex.SetDefaultMaterial("Camastro", "madera ligera")
    Bladex.SetDefaultMaterial("Carretilla", "madera ligera")
    Bladex.SetDefaultMaterial("Cepo", "madera ligera")
    Bladex.SetDefaultMaterial("Cerbatana", "madera ligera")
    Bladex.SetDefaultMaterial("CofrePieza1", "madera ligera")
    Bladex.SetDefaultMaterial("CofrePieza2", "madera ligera")
    Bladex.SetDefaultMaterial("CofrePieza3", "madera ligera")
    Bladex.SetDefaultMaterial("Dardo", "madera ligera")
    Bladex.SetDefaultMaterial("MesaPieza1", "madera ligera")
    Bladex.SetDefaultMaterial("MesaPieza2", "madera ligera")
    Bladex.SetDefaultMaterial("MesaPieza3", "madera ligera")
    Bladex.SetDefaultMaterial("MesaPieza4", "madera ligera")
    Bladex.SetDefaultMaterial("MesaPieza5", "madera ligera")
    Bladex.SetDefaultMaterial("MesitaPieza1", "madera ligera")
    Bladex.SetDefaultMaterial("MesitaPieza2", "madera ligera")
    Bladex.SetDefaultMaterial("MesitaPieza3", "madera ligera")
    Bladex.SetDefaultMaterial("MesitaPieza4", "madera ligera")
    Bladex.SetDefaultMaterial("MesonPieza1", "madera ligera")
    Bladex.SetDefaultMaterial("MesonPieza2", "madera ligera")
    Bladex.SetDefaultMaterial("Mesonroto", "madera ligera")
    Bladex.SetDefaultMaterial("Palancatortura", "madera ligera")
    Bladex.SetDefaultMaterial("Panoplia", "madera ligera")
    Bladex.SetDefaultMaterial("Pivote2", "madera ligera")
    Bladex.SetDefaultMaterial("Plataforma", "madera ligera")
    Bladex.SetDefaultMaterial("Polea", "madera ligera")
    Bladex.SetDefaultMaterial("PuenteAdolfoDerecho", "madera ligera")
    Bladex.SetDefaultMaterial("PuenteAdolfoIzquierdo", "madera ligera")
    Bladex.SetDefaultMaterial("PuertaFernando", "madera ligera")
    Bladex.SetDefaultMaterial("RamaNevada", "madera ligera")
    Bladex.SetDefaultMaterial("Tablatortura", "madera ligera")
    Bladex.SetDefaultMaterial("Tocon", "madera ligera")
    Bladex.SetDefaultMaterial("Tronco", "madera ligera")
    Bladex.SetDefaultMaterial("TroncoNevado", "madera ligera")
    Bladex.SetDefaultMaterial("Trono", "madera ligera")
    Bladex.SetDefaultMaterial("TronoManuel", "madera ligera")
    Bladex.SetDefaultMaterial("Viga", "madera ligera")
    Bladex.SetDefaultMaterial("Vigaro1", "madera ligera")
    Bladex.SetDefaultMaterial("Vigaro2", "madera ligera")

    Bladex.SetDefaultMaterial("Agarramanos", "metal ligero")
    Bladex.SetDefaultMaterial("Agarrapies", "metal ligero")
    Bladex.SetDefaultMaterial("Amuleto", "metal ligero")
    Bladex.SetDefaultMaterial("Armadura", "metal ligero")
    Bladex.SetDefaultMaterial("ArmaduraBlade", "metal ligero")
    Bladex.SetDefaultMaterial("LlaveNegra", "metal ligero")
    Bladex.SetDefaultMaterial("BlasonAurelio", "metal ligero")
    Bladex.SetDefaultMaterial("Blason1", "metal ligero")
    Bladex.SetDefaultMaterial("Blason2", "metal ligero")
    Bladex.SetDefaultMaterial("Blason3", "metal ligero")
    Bladex.SetDefaultMaterial("Blason4", "metal ligero")
    Bladex.SetDefaultMaterial("Blason5", "metal ligero")
    Bladex.SetDefaultMaterial("Blason6", "metal ligero")
    Bladex.SetDefaultMaterial("LlaveAzul", "metal ligero")
    Bladex.SetDefaultMaterial("Brazalete", "metal ligero")
    Bladex.SetDefaultMaterial("Campana", "metal ligero")
    Bladex.SetDefaultMaterial("Carburo", "metal ligero")
    Bladex.SetDefaultMaterial("Casco1", "metal ligero")
    Bladex.SetDefaultMaterial("Casco2", "metal ligero")
    Bladex.SetDefaultMaterial("Cerradura", "metal ligero")
    Bladex.SetDefaultMaterial("Dragonsw", "metal ligero")
    Bladex.SetDefaultMaterial("EscudoBlade2", "metal ligero")
    Bladex.SetDefaultMaterial("EscudoBlade", "metal ligero")
    Bladex.SetDefaultMaterial("Escudobollado1", "metal ligero")
    Bladex.SetDefaultMaterial("Escudobollado2", "metal ligero")
    Bladex.SetDefaultMaterial("Eslabon1", "metal ligero")
    Bladex.SetDefaultMaterial("Eslabon2", "metal ligero")
    Bladex.SetDefaultMaterial("Eslabon3", "metal ligero")
    Bladex.SetDefaultMaterial("GanchoAurelio", "metal ligero")
    Bladex.SetDefaultMaterial("Garfio3", "metal ligero")
    Bladex.SetDefaultMaterial("Globo", "metal ligero")
    Bladex.SetDefaultMaterial("Grifoserpiente", "metal ligero")
    Bladex.SetDefaultMaterial("Hornacina", "metal ligero")
    Bladex.SetDefaultMaterial("Jaula", "metal ligero")
    Bladex.SetDefaultMaterial("Lamparatecho", "metal ligero")
    Bladex.SetDefaultMaterial("LamparaMiguelSinPeana", "metal ligero")
    Bladex.SetDefaultMaterial("LapidaAmazona", "metal ligero")
    Bladex.SetDefaultMaterial("Pala", "metal ligero")
    Bladex.SetDefaultMaterial("Pelele", "metal ligero")
    Bladex.SetDefaultMaterial("PeleleNevado", "metal ligero")
    Bladex.SetDefaultMaterial("Perola", "metal ligero")
    Bladex.SetDefaultMaterial("Pico", "metal ligero")
    Bladex.SetDefaultMaterial("PinchoMiguel", "metal ligero")
    Bladex.SetDefaultMaterial("Pinchos", "metal ligero")
    Bladex.SetDefaultMaterial("PinchoSotano", "metal ligero")
    Bladex.SetDefaultMaterial("Soporteantorcha", "metal ligero")
    Bladex.SetDefaultMaterial("Telescopio", "metal ligero")
    Bladex.SetDefaultMaterial("Tintero", "metal ligero")
    Bladex.SetDefaultMaterial("Trillo", "metal ligero")
    Bladex.SetDefaultMaterial("Vagoneta", "metal ligero")
    Bladex.SetDefaultMaterial("Xkorpyon", "metal ligero")

    Bladex.SetDefaultMaterial("Alfeizar", "piedra ligera")
    Bladex.SetDefaultMaterial("BloqueTallado", "piedra ligera")
    Bladex.SetDefaultMaterial("BoladePiedra", "piedra ligera")
    Bladex.SetDefaultMaterial("CabezaFernando", "piedra ligera")
    Bladex.SetDefaultMaterial("CabezaSerpiente", "piedra ligera")
    Bladex.SetDefaultMaterial("ColaSerpiente", "piedra ligera")
    Bladex.SetDefaultMaterial("Elefante", "piedra ligera")
    Bladex.SetDefaultMaterial("Esquirla", "piedra ligera")
    Bladex.SetDefaultMaterial("Estalact1", "piedra ligera")
    Bladex.SetDefaultMaterial("Estalact2", "piedra ligera")
    Bladex.SetDefaultMaterial("GargolaFernando", "piedra ligera")
    Bladex.SetDefaultMaterial("GargolaNevada", "piedra ligera")
    Bladex.SetDefaultMaterial("ElefantePartido", "piedra ligera")
    Bladex.SetDefaultMaterial("LamparaKongo", "piedra ligera")
    Bladex.SetDefaultMaterial("Lapida", "piedra ligera")
    Bladex.SetDefaultMaterial("Obelisco", "piedra ligera")
    Bladex.SetDefaultMaterial("Lapida3", "piedra ligera")
    Bladex.SetDefaultMaterial("LapidaBarbaro", "piedra ligera")
    Bladex.SetDefaultMaterial("LapidaCaballero", "piedra ligera")
    Bladex.SetDefaultMaterial("Monjecaliz", "piedra ligera")
    Bladex.SetDefaultMaterial("Monjescudo", "piedra ligera")
    Bladex.SetDefaultMaterial("Monjespada", "piedra ligera")
    Bladex.SetDefaultMaterial("ObeliscoGrande", "piedra ligera")
    Bladex.SetDefaultMaterial("ObeliscoNevado", "piedra ligera")
    Bladex.SetDefaultMaterial("PiedraNevada", "piedra ligera")
    Bladex.SetDefaultMaterial("PiedraNevadaCortada", "piedra ligera")
    Bladex.SetDefaultMaterial("PlacaTallada", "piedra ligera")
    Bladex.SetDefaultMaterial("ReinaAurelio", "piedra ligera")
    Bladex.SetDefaultMaterial("Reyaurelio", "piedra ligera")
    Bladex.SetDefaultMaterial("Tronera", "piedra ligera")
    Bladex.SetDefaultMaterial("Tumbacobra", "piedra ligera")
    Bladex.SetDefaultMaterial("Lapidareina", "piedra ligera")
    Bladex.SetDefaultMaterial("Lapidarey", "piedra ligera")
    # by Sryml: end
