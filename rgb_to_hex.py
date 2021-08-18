    def RGBtoHex(vals, rgbtype=1):
      """Converts RGB values in a variety of formats to Hex values.

         @param  vals     An RGB/RGBA tuple
         @param  rgbtype  Valid valus are:
                              1 - Inputs are in the range 0 to 1
                            256 - Inputs are in the range 0 to 255

         @return A hex string in the form '#RRGGBB' or '#RRGGBBAA'
    """

      if len(vals)!=3 and len(vals)!=4:
        raise Exception("RGB or RGBA inputs to RGBtoHex must have three or four elements!")
      if rgbtype!=1 and rgbtype!=256:
        raise Exception("rgbtype must be 1 or 256!")

      #Convert from 0-1 RGB/RGBA to 0-255 RGB/RGBA
      if rgbtype==1:
        vals = [255*x for x in vals]

      #Ensure values are rounded integers, convert to hex, and concatenate
      return '#' + ''.join(['{:02X}'.format(int(round(x))) for x in vals])