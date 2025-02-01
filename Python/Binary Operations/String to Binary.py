class Solution:
    # Method to add two binary numbers represented as strings
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings 'a' and 'b' to decimal using int(value,2), add them, then convert the sum back to binary using bin().
        # The bin() function returns a string starting with '0b', so we slice [2:] to remove the '0b' prefix and return the binary result.
        # We use 2 as second argument because a and b are both in binary i.e. base 2 and we need to tell python explicitly to interpret them as binary because
        # by default int() function assumes the first argment passed is in base 10.
        return bin(int(a, 2) + int(b, 2))[2:]
