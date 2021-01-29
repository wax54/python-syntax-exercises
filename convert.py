def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
    
    unit_in = unit_in.lower()
    unit_out = unit_out.lower()

    if unit_in == 'f':
      #temp is f let's find out what they want back
        if unit_out == 'f':
          #they want f back, heres the formula
          return temp
        elif unit_out == 'c':
          #they want c back, heres the formula
            return (temp - 32) * 5/9
        el
    elif unit_in == 'c':
        #temp is c let's find out what they want back
        if unit_out == 'c':
          #they want c back, heres the formula
            return temp
        elif unit_out == 'f':
          #they want f back, heres the formula
            return (temp * 9/5) + 32
    #I didn't understand the unit_in...
    else:
        return f"Invalid unit {unit_in}"
    #I understood the unit_in, but unit_out didn't match any units I know
    return f"Invalid unit {unit_out}"


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

