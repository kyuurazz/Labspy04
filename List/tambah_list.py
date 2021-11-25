# Tambah element list
## Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

b.append(a[0:2])
print(b)

## tambah list B dengan nilai string
print()
b.append("11")
print(b)

## tambah list B dengan 3 nilai
print()
print(b + [12, 13, 14])

## gabungkan list B dengan list A
print()
print(a + b)