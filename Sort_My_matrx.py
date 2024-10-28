import math

mtrx = [
    [2, 0, 33, -1, -21],
    [78, -7, -4, 3, 11],
    [-2, -7, -1, -9, 0],
    [13, 61, 60, 42, -10],
    [1, 0, 4, 0, 16]
]

def slct_sort_colu(mtrx):
    rows = len(mtrx)
    cols = len(mtrx[0])

    for col in range(cols):
        for i in range(rows):
            min_idx = i
            for j in range(i + 1, rows):
                if mtrx[j][col] < mtrx[min_idx][col]:
                    min_idx = j
            if min_idx != i:
                mtrx[i][col], mtrx[min_idx][col] = mtrx[min_idx][col], mtrx[i][col]
    
    return mtrx

def row_sums(mtrx):
    return [sum(row) for row in mtrx]

def geom_mean(val): #Geom sr ar = ( x * y * z ) / n
    prdct = 1
    n = len(val)
    for val in val:
        prdct *= abs(val)
    return prdct ** (1 / n) if n > 0 else 0

srtd_mtrx = slct_sort_colu(mtrx)

row_sums_rslt = row_sums(srtd_mtrx)
print(f"Summ - {row_sums_rslt}")

geom_mean_rslt = geom_mean(row_sums_rslt)
print(f"Ser geom -  {geom_mean_rslt}")

srtd_mtrx = slct_sort_colu(mtrx)

print("Sorted lol :")
for row in srtd_mtrx:
    print(row)

