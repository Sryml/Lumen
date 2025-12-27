

import BBLib
import Raster
import Bladex






def ShowImage(background_image,remove_backimage=1):

  back_image=BBLib.B_BitMap24()
  if back_image.ReadFromFile(background_image):
    w,h=back_image.GetDimension()
##    Raster.DrawImage(w,h,"RGB","Strecht",back_image.GetData())
    Raster.SetBackgroundImage(w,h,"RGB","Normal","VerticalStretch",back_image.GetData())
    Raster.Cls(0,0,0)
    Raster.SwapBuffers()
    if remove_backimage:
      Raster.RemoveBackgroundImage()
  else:
    print "ERROR in ShowImage(): can not open file",background_image






