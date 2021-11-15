"""Haystack and needle function"""

def main()-> None:
    """Programs entry point"""
    names: list[str] = ["Kris","Kaki"]
    print(contains("Kevin",names))

def contains(needle: str, haystack: list[str]) -> bool:
    """To identify if the needle is present"""
    count: int = 0
    j: int = 0
    while j < len(haystack):
        if(haystack[j] == needle):
            count += 1
        j += 1
    if(count == 0):
        return False
    else:
        return True 


if __name__ == "__main__":
    main() 
            
