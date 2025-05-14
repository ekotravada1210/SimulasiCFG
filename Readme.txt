Cara Penggunaan

Simulator Aturan Produksi CFG
Masukkan aturan produksi (contoh: S -> aSb | ε). Ketik 'selesai' untuk mengakhiri.
Aturan produksi: S->bcaS|aS|b
Aturan produksi: selesai
Masukkan string yang akan diperiksa: bcaaaab

Proses Derivation:
Langkah 1: Start | Simbol: 'S'
Langkah 2: S → bcaS | Simbol: 'bcaS'
Langkah 3: S → aS | Simbol: 'aaS'
Langkah 4: S → b | Simbol: 'aab'
...
Langkah 27: S → b | Simbol: 'bcaaaab'

Output: Diterima
Derivasi Berhasil:
1. S → bcaS
2. S → aS
3. S → aS
4. S → aS
5. S → b