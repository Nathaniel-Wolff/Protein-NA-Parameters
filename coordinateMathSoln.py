Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#!/usr/bin/env python3 
# Name: Nathaniel Wolff
# Group Members: None

'''
The docstrings are given stepwise, since this program is very intensive. This a a choice for clarity, and for readability.
'''

import math
class Triad:
    """
    Calculate angles and distances among a triad of points.
 
    Author: David Bernick
    Date: March 21, 2013
    Points can be supplied in any dimensional space as long as they are consistent.
    Points are supplied as tupels in n-dimensions, and there should be three
    of those to make the triad. Each point is positionally named as p,q,r
    and the corresponding angles are then angleP, angleQ and angleR.
    Distances are given by dPQ(), dPR() and dQR()
 
    Required Modules: math
    initialized: 3 positional tuples representing Points in n-space
             p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,1,0) )
    attributes: p,q,r the 3 tuples representing points in N-space
    methods:  angleP(), angleR(), angleQ() angles measured in radians
          dPQ(), dPR(), dQR() distances in the same units of p,q,r
 
    """
    def __init__(self,p,q,r) :
        """ Construct a Triad. 
        
        Example construction:
            p1 = Triad( p=(1.,0.,0.), q=(0.,0.,0.), r=(0.,0.,0.) ). 
        """
        self.p = p
        self.q = q
        self.r = r
# private helper methods
    def dSquared (self,a,b) : # calculate square of the distance of point a to b in 3 space
        return float(sum((ia-ib)*(ia-ib) for  ia,ib in zip (a,b))) #what is i???
    
    def dotProduct (self,a,b) : # dotProd of standard vectors a,b
        return float(sum(ia*ib for ia,ib in zip(a,b)))
    
    def ndot (self,a,b,c) : # dotProd of vec. a,c standardized to b
        return float(sum((ia-ib)*(ic-ib) for ia,ib,ic in zip (a,b,c)))
    
# calculate lengths(distances) of segments PQ, PR and QR
    def dPQ (self):
        """ Provides the distance between point p and point q """
        return math.sqrt(self.dSquared(self.p,self.q)) ##
    
    def dPR (self):
        """ Provides the distance between point p and point r """
        return math.sqrt(self.dSquared(self.p,self.r))
    
    def dQR (self):
        """ Provides the distance between point q and point r """
        return math.sqrt(self.dSquared(self.q,self.r))
    
    def angleP (self) :
        """ Provides the angle made at point p by segments pq and pr (radians). """
        return math.acos(self.ndot(self.q,self.p,self.r) /   math.sqrt(self.dSquared(self.q,self.p)*self.dSquared(self.r,self.p)))
    
    def angleQ (self) :
        """ Provides the angle made at point q by segments qp and qr (radians). """
        return math.acos(self.ndot(self.p,self.q,self.r) /  math.sqrt(self.dSquared(self.p,self.q)*self.dSquared(self.r,self.q)))
 
    def angleR (self) :
        """ Provides the angle made at point r by segments rp and rq (radians). """
        return math.acos(self.ndot(self.p,self.r,self.q) /  math.sqrt(self.dSquared(self.p,self.r)*self.dSquared(self.q,self.r)))

coordinatesAll = input ("Give the coordinates of the each atom.")
#q = coordinatesAll.find("(")
#r = coordinatesAll.find(")")
#noParenthesesSlicedCoordinates = coordinatesAll.replace("(", ",")

version1 = coordinatesAll.replace("C = ", " ")
version2 = version1.replace("N = ", " ")
version3 = version2.replace("Ca = ", " ")
version4 = version3.replace("(", " ")
version5 = version4.replace (")", " ")
version6 = version5.replace ("    ", ",")
#print(version6)

"""The original coordinates are cleaned up to make them into a string that only contains floats and commas, which
is a design choice that makes it easier to split up"""
splitCoordinates = version6.split(",")
#print(splitCoordinates)

"""Here's the splitting, by each inserted and original comma."""

Cx = float(splitCoordinates[0])
Cy = float(splitCoordinates[1])
Cz = float(splitCoordinates[2])
Nx = float(splitCoordinates[3])
Ny = float(splitCoordinates[4])
Nz = float(splitCoordinates[5])
Cax = float(splitCoordinates[6])
Cay = float(splitCoordinates[7])
Caz = float(splitCoordinates[8])

"""It's easier to convert the list's elements to floats in one step, there are fewer objects to work with this way."""

CCoords = (Cx, Cy, Cz)
#print(CCoords)
NCoords = (Nx, Ny, Nz)
CaCoords = (Cax, Cay, Caz)

"""You may notice there are periodic prints. These ensure the program is running properly and makes it easier to debug.
This is my way of desining code, and for reference I leave them in there."""

usersTriad = Triad (CCoords, NCoords, CaCoords)
cNBondLength=usersTriad.dPQ()
print("C-N bond length is"+" "+str(cNBondLength))
nCABondLength = usersTriad.dPR()
print("Ca-N bond length is"+" "+str(nCABondLength))
cNCabondangle = usersTriad.angleQ()*(360/(2*3.14)) #CONVERTED TO RADIANS (3 sig figs)
#print(type(usersTriad.angleQ()))
print("C-N-Ca bond angle is"+" "+str(cNCabondangle))