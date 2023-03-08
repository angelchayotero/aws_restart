#
#Se necesita un programa que calcule el precio final de un producto que cuenta con el 15% de
#descuento.
#Input: Precio del producto (float > 0)
#Output: Precio total con descuento (float > 0)

precio_sin_descuento = input("Indique el precio del producto")

print("Hay una oferta, el precio con un 15% de descuento es:", (float(precio_sin_descuento)*.85))
