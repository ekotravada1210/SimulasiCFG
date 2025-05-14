from collections import deque

print("Simulator Aturan Produksi CFG")
print("Masukkan aturan produksi (contoh: S -> aSb | ε). Ketik 'selesai' untuk mengakhiri.")
rules = {}
start_symbol = None

while True:
    line = input("Aturan produksi: ").strip()
    if line.lower() == 'selesai':
        if not rules:
            print("Harap masukkan setidaknya satu aturan produksi.")
            continue
        break
    if '->' not in line:
        print("Format tidak valid. Gunakan ' -> ' untuk memisahkan sisi kiri dan kanan.")
        continue
    left, right = line.split('->', 1)
    left = left.strip()
    if not left:
        print("Simbol non-terminal tidak boleh kosong.")
        continue
    
    productions = []
    for prod in right.split('|'):
        prod = prod.strip()
        if prod == 'ε':
            productions.append('')
        else:
            productions.append(prod)
    
    if left in rules:
        rules[left].extend(productions)
    else:
        rules[left] = productions
    
    if start_symbol is None:
        start_symbol = left

input_string = input("Masukkan string yang akan diperiksa: ").strip()

def bfs_derivation(target):
    target_len = len(target)
    queue = deque()
    queue.append(([start_symbol], []))
    visited = set()
    step_counter = 0
    
    print("\nProses Derivation:")
    
    while queue:
        current, steps = queue.popleft()
        current_str = ''.join(current)
        step_counter += 1
        
        print(f"Langkah {step_counter}: {' -> '.join(steps) if steps else 'Start'} | Simbol: '{current_str}'")
        
        # Cek jika semua terminal
        if all(symbol not in rules for symbol in current):
            if current_str == target:
                return True, steps
            continue
            
        # Batasan panjang untuk optimasi
        if len(current) > target_len * 2:
            continue
            
        # Temukan dan ekspansi non-terminal pertama
        expanded = False
        for i, symbol in enumerate(current):
            if symbol in rules:
                for production in rules[symbol]:
                    new_symbols = current[:i] + list(production) + current[i+1:]
                    new_steps = steps + [f"{symbol} → {production if production != '' else 'ε'}"]
                    
                    # Optimasi panjang
                    if len(new_symbols) > target_len * 2:
                        continue
                        
                    # Cegah pengulangan state
                    state_key = ''.join(new_symbols)
                    if state_key not in visited:
                        visited.add(state_key)
                        queue.append((new_symbols, new_steps))
                
                expanded = True
                break  # Hanya proses non-terminal pertama
        
        if not expanded:
            continue
    
    return False, None

accepted, steps = bfs_derivation(input_string)

if accepted:
    print("\nOutput: Diterima")
    print("Derivasi Berhasil:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")
else:
    print("\nOutput: Tidak diterima")
    print("String tidak dapat dihasilkan oleh CFG yang diberikan")