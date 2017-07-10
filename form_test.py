from singleton_form import *
from monomial_form import *
from polynomial_form import *
from sympy import *
from sympy.abc import x,y,z

import unittest
'''
    NOTE: Sympy doesn't honor expression flag evaluate=False
        for the identity property. This may be a crippling problem, that needs
        to be handled by whatever implements this library
        Test a12 has been left in there just in case the issue is resolved
'''
class TestSymp(unittest.TestCase):
    def setUp(self):
        self.a1 = Pow(x, 2)
        self.a2 = Add(x, y,evaluate=False)
        self.a3 = Mul(x,y,2,3,evaluate=False)
        self.a4 = Mul(Pow(x,3),y,4,evaluate=False)
        self.a5 = Pow(3, 5,evaluate=False)
        self.a6 = Pow(3, pi,evaluate=False)
        self.a7 = Mul(Pow(x,4),Pow(x,9),evaluate=False)
        self.a8 = Mul(Pow(y,3),Pow(x,2),evaluate=False)
        self.a9 = Mul(Pow(y,pi),Pow(x,10),evaluate=False)
        self.a10 = Add(3,pi,pi,evaluate=False)
        self.a11 = Add(1,9,pi,evaluate=False)
        #self.a12 = Add(0,1,evaluate=False)
        self.a13 = Add(152, pi,evaluate=False)
        self.a14 = Add(3, pi,evaluate=False)
        self.a15 = Add(3, Mul(4, pi),evaluate=False)
        self.a16 = Mul(3,pi,evaluate=False)
        self.a17 = Mul(Pow(x,3),Pow(y,2),z,Pow(2,-1),evaluate=False)
        self.a18 = Mul(Mul(Pow(x,3),Pow(y,2),z),Pow(2,-1,evaluate=False),evaluate=False)
        self.a19 = Mul(Pow(Integer(2), Integer(-1)), Pow(Symbol('m'), Integer(3)),evaluate=False)
        self.a20 = sin(x)
        self.a21 = Mul(sin(x),3,Pow(2,-1,evaluate=False),evaluate=False)
        self.a22 = Add(Pow(x,4),Pow(x,3),Pow(x,2),x,1,evaluate=False)
        self.a23 = Add(Mul(2,pi),Mul(3,pi),evaluate=False)
        self.a24 = Pow(Add(x,1),2,evaluate=False)
        self.a25 = Mul(3,Add(3,x),evaluate=False) #N
        self.a26 = Add(Mul(3,Pow(x,2)),Pow(x,1),5,evaluate=False) #N - Exponent 1
        self.a26 = Add(Mul(3,Pow(x,2)),Pow(x,0),5,evaluate=False) #N - Exponent 0
        self.a27 = Add(Mul(0,Pow(x,2)),Pow(x,0),5,evaluate=False) #N - 0*x
        self.a28 = Mul(2,Pow(4,-1,evaluate=False),evaluate=False) #N - 2/4
        self.a29 = Add(x, Mul(2,Pow(4,-1,evaluate=False),evaluate=False),evaluate=False) #N - x + 2/4
        self.a30 = Add(x, Mul(-1,Pow(3,-1,evaluate=False),evaluate=False))
        self.a31 = Mul(pi,Pow(pi,-1,evaluate=False),evaluate=False) #N - pi/pi
        self.a32 = Mul(pi,Pow(pi,-2,evaluate=False),evaluate=False) #N - pi/pi^2



    def test_singleton(self):
        self.assertTrue(is_singleton_form(x)[0])
        self.assertTrue(is_singleton_form(y)[0])
        self.assertTrue(is_singleton_form(z)[0])
        self.assertFalse(is_singleton_form(self.a1)[0])
        self.assertFalse(is_singleton_form(self.a2)[0])
        self.assertFalse(is_singleton_form(self.a3)[0]) #N
        self.assertFalse(is_singleton_form(self.a4)[0])
        self.assertFalse(is_singleton_form(self.a5)[0]) #N
        self.assertTrue(is_singleton_form(self.a6)[0])
        self.assertFalse(is_singleton_form(self.a7)[0])
        self.assertFalse(is_singleton_form(self.a8)[0])
        self.assertFalse(is_singleton_form(self.a9)[0])
        self.assertFalse(is_singleton_form(self.a10)[0]) #N
        self.assertFalse(is_singleton_form(self.a11)[0]) #N
        #self.assertFalse(is_singleton_form(self.a12)[0]) #N
        self.assertTrue(is_singleton_form(self.a13)[0])
        self.assertTrue(is_singleton_form(self.a14)[0]) 
        self.assertTrue(is_singleton_form(self.a15)[0])
        self.assertTrue(is_singleton_form(self.a16)[0])
        self.assertFalse(is_singleton_form(self.a17)[0])
        self.assertFalse(is_singleton_form(self.a18)[0])
        self.assertFalse(is_singleton_form(self.a19)[0])
        self.assertTrue(is_singleton_form(self.a20)[0])
        self.assertFalse(is_singleton_form(self.a21)[0])
        self.assertFalse(is_singleton_form(self.a22)[0])
        self.assertFalse(is_singleton_form(self.a23)[0]) #N
        self.assertFalse(is_singleton_form(self.a24)[0])
        self.assertFalse(is_singleton_form(self.a25)[0]) #N
        self.assertFalse(is_singleton_form(self.a26)[0]) #N
        self.assertFalse(is_singleton_form(self.a27)[0]) #N
        self.assertFalse(is_singleton_form(self.a28)[0]) #N
        self.assertFalse(is_singleton_form(self.a29)[0]) #N
        self.assertFalse(is_singleton_form(self.a30)[0])
        self.assertFalse(is_singleton_form(self.a31)[0]) #N
        self.assertFalse(is_singleton_form(self.a32)[0]) #N


    def test_expanded_monomial(self):
        self.assertTrue(is_monomial_form(x)[0])
        self.assertTrue(is_monomial_form(y)[0])
        self.assertTrue(is_monomial_form(z)[0])
        self.assertTrue(is_monomial_form(self.a1)[0])
        self.assertFalse(is_monomial_form(self.a2)[0])
        self.assertFalse(is_monomial_form(self.a3)[0]) #N
        self.assertTrue(is_monomial_form(self.a4)[0])
        self.assertFalse(is_monomial_form(self.a5)[0]) #N
        self.assertTrue(is_monomial_form(self.a6)[0])
        self.assertFalse(is_monomial_form(self.a7)[0])
        self.assertTrue(is_monomial_form(self.a8)[0])
        self.assertTrue(is_monomial_form(self.a9)[0])
        self.assertFalse(is_monomial_form(self.a10)[0]) #N
        self.assertFalse(is_monomial_form(self.a11)[0]) #N
        #self.assertFalse(is_monomial_form(self.a12)[0]) #N
        self.assertTrue(is_monomial_form(self.a13)[0])
        self.assertTrue(is_monomial_form(self.a14)[0]) 
        self.assertTrue(is_monomial_form(self.a15)[0])
        self.assertTrue(is_monomial_form(self.a16)[0])
        self.assertTrue(is_monomial_form(self.a17)[0])
        self.assertTrue(is_monomial_form(self.a18)[0])
        self.assertTrue(is_monomial_form(self.a19)[0])
        self.assertTrue(is_monomial_form(self.a20)[0])
        self.assertTrue(is_monomial_form(self.a21)[0])
        self.assertFalse(is_monomial_form(self.a22)[0])
        self.assertFalse(is_monomial_form(self.a23)[0]) #N
        self.assertFalse(is_monomial_form(self.a24)[0])
        self.assertFalse(is_monomial_form(self.a25)[0]) #N
        self.assertFalse(is_monomial_form(self.a26)[0]) #N
        self.assertFalse(is_monomial_form(self.a27)[0]) #N
        self.assertFalse(is_monomial_form(self.a28)[0]) #N
        self.assertFalse(is_monomial_form(self.a29)[0]) #N
        self.assertFalse(is_monomial_form(self.a30)[0])
        self.assertFalse(is_monomial_form(self.a31)[0]) #N
        self.assertFalse(is_monomial_form(self.a32)[0]) #N

    def test_expanded_polynomial(self):
        self.assertTrue(is_fully_expanded_polynomial(x)[0])
        self.assertTrue(is_fully_expanded_polynomial(y)[0])
        self.assertTrue(is_fully_expanded_polynomial(z)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a1)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a2)[0])
        self.assertFalse(is_fully_expanded_polynomial(self.a3)[0]) #N
        self.assertTrue(is_fully_expanded_polynomial(self.a4)[0])
        self.assertFalse(is_fully_expanded_polynomial(self.a5)[0]) #N
        self.assertTrue(is_fully_expanded_polynomial(self.a6)[0])
        self.assertFalse(is_fully_expanded_polynomial(self.a7)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a8)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a9)[0])
        self.assertFalse(is_fully_expanded_polynomial(self.a10)[0]) #N
        self.assertFalse(is_fully_expanded_polynomial(self.a11)[0]) #N
        #self.assertFalse(is_fully_expanded_polynomial(self.a12)[0]) #N
        self.assertTrue(is_fully_expanded_polynomial(self.a13)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a14)[0]) 
        self.assertTrue(is_fully_expanded_polynomial(self.a15)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a16)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a17)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a18)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a19)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a20)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a21)[0])
        self.assertTrue(is_fully_expanded_polynomial(self.a22)[0])
        self.assertFalse(is_fully_expanded_polynomial(self.a23)[0]) #N
        self.assertFalse(is_fully_expanded_polynomial(self.a24)[0])
        self.assertFalse(is_fully_expanded_polynomial(self.a25)[0]) #N
        self.assertFalse(is_fully_expanded_polynomial(self.a26)[0]) #N
        self.assertFalse(is_fully_expanded_polynomial(self.a27)[0]) #N
        self.assertFalse(is_fully_expanded_polynomial(self.a28)[0]) #N
        self.assertFalse(is_fully_expanded_polynomial(self.a29)[0]) #N
        self.assertTrue(is_fully_expanded_polynomial(self.a30)[0])
        self.assertFalse(is_fully_expanded_polynomial(self.a31)[0]) #N
        self.assertFalse(is_fully_expanded_polynomial(self.a32)[0]) #N
    
    def test_factored_polynomial(self):
        self.assertTrue(is_fully_factored_polynomial(x)[0])
        self.assertTrue(is_fully_factored_polynomial(y)[0])
        self.assertTrue(is_fully_factored_polynomial(z)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a1)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a2)[0])
        self.assertFalse(is_fully_factored_polynomial(self.a3)[0]) #N
        self.assertTrue(is_fully_factored_polynomial(self.a4)[0])
        self.assertFalse(is_fully_factored_polynomial(self.a5)[0]) #N
        self.assertTrue(is_fully_factored_polynomial(self.a6)[0])
        self.assertFalse(is_fully_factored_polynomial(self.a7)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a8)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a9)[0])
        self.assertFalse(is_fully_factored_polynomial(self.a10)[0]) #N
        self.assertFalse(is_fully_factored_polynomial(self.a11)[0]) #N
        #self.assertFalse(is_fully_factored_polynomial(self.a12)[0]) #N
        self.assertTrue(is_fully_factored_polynomial(self.a13)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a14)[0]) 
        self.assertTrue(is_fully_factored_polynomial(self.a15)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a16)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a17)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a18)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a19)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a20)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a21)[0])
        self.assertFalse(is_fully_factored_polynomial(self.a22)[0])
        self.assertFalse(is_fully_factored_polynomial(self.a23)[0]) #N
        self.assertTrue(is_fully_factored_polynomial(self.a24)[0])
        self.assertTrue(is_fully_factored_polynomial(self.a25)[0]) #N
        self.assertFalse(is_fully_factored_polynomial(self.a26)[0]) #N
        self.assertFalse(is_fully_factored_polynomial(self.a27)[0]) #N
        self.assertFalse(is_fully_factored_polynomial(self.a28)[0]) #N
        self.assertFalse(is_fully_factored_polynomial(self.a29)[0]) #N
        self.assertTrue(is_fully_factored_polynomial(self.a30)[0])
        self.assertFalse(is_fully_factored_polynomial(self.a31)[0]) #N
        self.assertFalse(is_fully_factored_polynomial(self.a32)[0]) #N

if __name__ == '__main__':
    unittest.main()
