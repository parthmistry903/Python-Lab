"""Exercise: 06"""
for h in range(24): suffix = 'AM' if h < 12 else 'PM'; if h == 0: print('12 Midnight'); elif h == 12: print('12 Noon'); else: print(f'{h % 12} {suffix}')