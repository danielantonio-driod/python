# hola_descuentos.py

# Paso 1-2: Lectura de entradas
num_productos   = int(input("¿Cuántos productos compraste? "))
compras_previas = int(input("¿Cuántas compras previas tienes? "))
monto_compra    = float(input("¿Cuál es el monto total de la compra en USD? "))
respuesta       = input("¿Es día de promoción especial? (s/n): ")
dia_promocion   = (respuesta.lower() == 's')

# Verificación rápida
print(f"Productos: {num_productos}, Compras previas: {compras_previas}, "
      f"Monto: ${monto_compra:.2f}, Promoción: {dia_promocion}")

# Paso 3-7: Cálculo del descuento
descuento = 0

# 3) Descuento por cantidad de productos (borde: exactamente 10 → no aplica)
if num_productos > 10:
    descuento += 10
else:
    # demostración de else
    print("No aplica descuento por cantidad de productos.")

print(f"→ Descuento tras cantidad: {descuento}%")

# 4) Descuento por cliente frecuente (borde: exactamente 5 → no aplica)
if compras_previas > 5:
    descuento += 5
elif compras_previas == 5:
    # subcondición: justo en el límite se informa pero no añade
    print("Has alcanzado el límite de compras para cliente frecuente.")
else:
    print("No aplica descuento por compras previas.")

print(f"→ Descuento tras compras previas: {descuento}%")

# 5) Descuento por monto de compra (borde: exactamente 500 → no aplica)
if monto_compra > 500:
    descuento += 7
elif monto_compra == 500:
    print("Estuviste justo en el límite de descuento por monto.")
else:
    print("No aplica descuento por monto de compra.")

print(f"→ Descuento tras monto de compra: {descuento}%")

# 6) Descuento por día de promoción (subcondición compuesta)
if dia_promocion:
    descuento += 15
else:
    print("Hoy no es día de promoción especial.")

print(f"→ Descuento tras promoción especial: {descuento}%")

# 7) Condiciones anidadas y tope máximo
# Si el cliente compró más de 20 productos Y es día de promoción, informamos
if num_productos > 20 and dia_promocion:
    print("¡Cliente VIP en día de promoción! Aplicando todas las reglas…")

# Tope del 30%
if descuento > 30:
    descuento = 30
    print("Descuento recortado al máximo permitido: 30%")

print(f"→ Descuento final: {descuento}%")

# Paso 8: Total a pagar
total_a_pagar = monto_compra * (1 - descuento / 100)
print(f"Total a pagar: ${total_a_pagar:.2f} USD")
