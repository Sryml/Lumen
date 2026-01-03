import Raster


Raster.SetDomeColor(225,225,225)


#-----------------------AGUA------------------------------------------------

fuente_vida=Bladex.CreateEntity("fuente_vida","Entity Water",6875,-1100,-2625)
fuente_vida.Reflection=-1
fuente_vida.Color=5,10,10

fuente_veneno=Bladex.CreateEntity("fuente_veneno","Entity Water",-54000,-1000,-22000)
fuente_veneno.Reflection=-0.5
fuente_veneno.Color=5,10,10

#en bagno venenoso
agua_ven=Bladex.CreateEntity("agua_monolito","Entity Water",-54000,0,500)
agua_ven.Reflection=-1
agua_ven.Color=0,0,0


#  EN MONOLITO

#antes de la llave
agua_monolito=Bladex.CreateEntity("agua_monolito","Entity Water",-25000,19100,57000)
agua_monolito.Reflection=-1
agua_monolito.Color=0,0,0




#despues de la llave
agua_sub=Bladex.CreateEntity("agua_sub","Entity Water",-25000,18880,17000)
agua_sub.Reflection=-1
agua_sub.Color=0,0,0


#en el camino al final
agua_sub4=Bladex.CreateEntity("agua_sub4","Entity Water",-98000,8300,-3000)
agua_sub4.Reflection=0
agua_sub4.Color=0,0,0


####agua en trampa de la palabra de dios

agua_god=Bladex.CreateEntity("agua_god","Entity Water",-58000,34000,142000)
agua_god.Reflection=0
agua_god.Color=0,0,0

####agua en el canal exterior

agua_canal=Bladex.CreateEntity("agua_canal","Entity Water",4000,12000,84000)
agua_canal.Reflection=0
agua_canal.Color=0,0,0


