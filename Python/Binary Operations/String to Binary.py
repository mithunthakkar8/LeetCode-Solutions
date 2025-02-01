class Solution:
    # Method to add two binary numbers represented as strings
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings 'a' and 'b' to decimal using int(), add them, then convert the sum back to binary using bin().
        # The bin() function returns a string starting with '0b', so we slice [2:] to remove the '0b' prefix and return the binary result.
        return bin(int(a, 2) + int(b, 2))[2:]
