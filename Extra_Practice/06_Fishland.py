skumria_price = float(input())
caca_price = float(input())
midi_price = 7.50
palamud_price = skumria_price + (skumria_price * 0.6)
safrid_price = caca_price + (caca_price * 0.8)

kg_palamund = float(input())
kg_safrid = float(input())
kg_midi = int(input())

total_price = kg_palamund * palamud_price + kg_safrid * safrid_price + kg_midi * midi_price
print("{:.2f}".format(total_price))