import math

AB = int(input())
BC = int(input())

AC = math.sqrt((AB*AB) + (BC*BC))


angleC = (math.acos(((BC*BC) + (AB*AB) - (AC*AC))/(2*BC*AB)))*180*7/(22)
