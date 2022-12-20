class TestClass:
    var1 = "hello"
    
    def __init__(self):
        self.var2 = "computer"
        self.var_type = type(self.var2)
        
    def test_incrementor(self,x):
        return x+1
        
test = TestClass()
print(test.__dict__)
incrementor = test.test_incrementor(1)
setattr(test,"var2",incrementor)
print(test,__dict__)