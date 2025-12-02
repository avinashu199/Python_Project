#creating my own module
#my module name is hero

#contsants/values
movie="Bahubali"
collections=2000

#functions
def prabhas(movie):
    match movie:
        case "Bahubali":
            print("Industry hit with 2000 collections")
        case "Salar":
            print("Most viewed in OTT")
        case "Mirchi":
            print("first 40cr for Prabhas")
        case "Kalki":
            print("First 1000cr for Vyjayanthi Movies")
        case "Spirit":
            print("All time industry hit-2027")
        case _:
            print("Data not available")
        