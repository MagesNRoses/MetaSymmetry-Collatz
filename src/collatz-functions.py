def collatz_sequence(n):
    """Genera secuencia de Collatz para un número n"""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def classify_region(x, epsilon=0.1, log23=1.58496):
    """Clasifica el punto en las regiones A,B,C,D"""
    if x > epsilon > log23:
        return 'A'
    elif epsilon > x > log23:
        return 'B'
    elif log23 > x > epsilon:
        return 'C'
    elif log23 > epsilon > x:
        return 'D'
    return 'U'  # No clasificado

def analyze_trajectory(n):
    """Analiza una trayectoria completa"""
    seq = collatz_sequence(n)
    regions = []
    j, k = 0, 0  # Contadores de operaciones
    
    for i in range(1, len(seq)):
        # Determinar tipo de operación
        if seq[i] == 3 * seq[i-1] + 1:
            j += 1
            op = '3n+1'
        else:
            k += 1
            op = 'n/2'
        
        # Calcular razón x
        total_ops = j + k
        x = j / total_ops if total_ops > 0 else 0
        
        # Clasificar región
        region = classify_region(x)
        regions.append((seq[i-1], op, x, region))
    
    return {
        'n': n,
        'steps': len(seq) - 1,
        'sequence': seq,
        'regions': regions
    }

# Optimización: Manejo robusto de división por cero
def analyze_trajectory(n):
    # ... código existente ...
    for i in range(1, len(seq)):
        # ...
        total_ops = j + k
        # SOLUCIÓN: Evitar división por cero
        x = j / total_ops if total_ops > 0 else 0.0  # ← Corregido