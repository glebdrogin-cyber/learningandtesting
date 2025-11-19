from mathutils import add, multiply, divide

def main():
    print("=" * 50)
    print("Testing mathutils Package")
    print("=" * 50)
    
    # Test Addition
    print("\n--- Test: Addition ---")
    result = add(10, 5)
    print(f"add(10, 5) = {result}")
    
    result = add(-3, 7)
    print(f"add(-3, 7) = {result}")
    
    # Test Multiplikation
    print("\n--- Test: Multiplikation ---")
    result = multiply(4, 6)
    print(f"multiply(4, 6) = {result}")
    
    result = multiply(2.5, 4)
    print(f"multiply(2.5, 4) = {result}")
    
    # Test Division (erfolgreiche Fälle)
    print("\n--- Test: Division (erfolgreich) ---")
    result = divide(20, 4)
    print(f"divide(20, 4) = {result}")
    
    result = divide(15, 3)
    print(f"divide(15, 3) = {result}")
    
    # Test Division durch Null (Fehlerfall)
    print("\n--- Test: Division durch Null (Fehlerbehandlung) ---")
    try:
        result = divide(10, 0)
        print(f"divide(10, 0) = {result}")
    except ValueError as e:
        print(f"Fehler abgefangen: {e}")
    
if __name__ == "__main__":
    main()