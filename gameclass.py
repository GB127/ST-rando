class ROM:
    def __init__(self,data):
        """
        This constructor convert the game (that is only in bytes)
        into a byte array that is a mutable form.

        data should be in bytes
        """
        self.data = bytearray(data)
    def __getitem__(self,offset):
        return self.data[offset]
    def __setitem__(self,offset, value):
        self.data[offset] = value
        
    def setmulti(self,offset1,offset2,value):
        for i in range(offset1, offset2+1):
            self.data[i] = value