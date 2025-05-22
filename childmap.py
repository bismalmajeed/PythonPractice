from ClassandObject import Calculator

class ChildIm1(Calculator):
    num2= 200
    def __init__(self):
        Calculator.__init__(self, 2,10)

    def getCompleteData(self):
        return self.num2+self.num+self.Summation()

obj=ChildIm1()
print(obj.getCompleteData())


""""
**Explanation:**  
1. **Inheritance**: `ChildIm1` inherits from `Calculator` and extends its functionality.  
2. **Parent Constructor**: The child class calls the parent constructor with `2` and `10` (initializing `firstNumber=2`, `secondNumber=10`).  
3. **Summation Logic**:  
   - `self.Summation()` computes `2 + 10 + 100 = 112`.  
4. **Final Calculation**:  
   - `self.num2 (200) + self.num (100) + self.Summation() (112) = 412`.
"""