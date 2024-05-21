#Create a model of a class that defines a parcel of land


#Ask for input
print("Owner: ", name)
    name = input("Name: ")

print("Area: ", lotsize)
    lotsize = input("Area(in sq. meters): ")

class Parcel:
    
    def ___getClassification___(size):
        areasize = int(lotsize)

        # Classify lot sizes
        if areasize < 10000 :
            classify = 'Residential'
        elif areasize > 10000 and areasize < 120000 :
            classify = 'Private Agricultural'
        elif areasize > 120000 :
            classify = 'Public Agricultural'
        else:
            classify = 'INVALID'

        return classify
    
print("A parcel of land owned by ", name , " with an area of ", lotsize , " square meters")    
print("Consolidated lot of ", selfname , " and ", othername , " with a total area of ", sumofareas)   






print("Owner: ", name)
    name = input("Name: ")

print("Area: ", lotsize)
    lotsize = input("Area(in sq. meters): ")

print("Type": ", landtype)
    landtype = input("Type: ")

class Riparian:

    
    def ___getAdjoiningWaterbody___(name):
        typeofland = int(landtype)

        #Typing of Adjoining Body of Water
        if typeofland = 1 :
            typing = 'Adjacent to River - can be subject to titling'
        elif typeofland = 2 :
            typing = 'Adjacent to Ocean (Littoral) - cannot be subject to titling'
        else:
            typing = 'Invalid Riparian Parcel'
        
        return typing

