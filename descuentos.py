
num_productos   = int(input("¿Cuántos productos compraste? "))
compras_previas = int(input("¿Cuántas compras previas tienes? "))
monto_compra    = float(input("¿Cuál es el monto total de la compra en USD? "))
respuesta       = input("¿Es día de promoción especial? (s/n): ")
dia_promocion   = (respuesta.lower() == 's')

print(f"Productos: {num_productos}, Compras previas: {compras_previas}, "
      f"Monto: ${monto_compra:.2f}, Promoción: {dia_promocion}")


descuento = 0

if num_productos > 10:
    descuento += 10
else:
    print("No aplica descuento por cantidad de productos.")

print(f"→ Descuento tras cantidad: {descuento}%")

if compras_previas > 5:
    descuento += 5
elif compras_previas == 5:
    print("Has alcanzado el límite de compras para cliente frecuente.")
else:
    print("No aplica descuento por compras previas.")

print(f"→ Descuento tras compras previas: {descuento}%")

if monto_compra > 500:
    descuento += 7
elif monto_compra == 500:
    print("Estuviste justo en el límite de descuento por monto.")
else:
    print("No aplica descuento por monto de compra.")

print(f"→ Descuento tras monto de compra: {descuento}%")

if dia_promocion:
    descuento += 15
else:
    print("Hoy no es día de promoción especial.")

print(f"→ Descuento tras promoción especial: {descuento}%")

if num_productos > 20 and dia_promocion:
    print("¡Cliente VIP en día de promoción! Aplicando todas las reglas…")

if descuento > 30:
    descuento = 30
    print("Descuento recortado al máximo permitido: 30%")

print(f"→ Descuento final: {descuento}%")

total_a_pagar = monto_compra * (1 - descuento / 100)
print(f"Total a pagar: ${total_a_pagar:.2f} USD")
