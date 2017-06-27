from sympy import *
from monomial_form import *

'''
    is_polynomial(expr): checks to see if the polynomial given is well formed.
    a polynomial can either be a monomial or a sum of monomials with no common bases
    TODO: Implement "no common bases" better ((x^2)(2x)) + (2x^3)(x^2) will
            incorrectly pass
    returns:    true if the polynomial is well formed
                false otherwise
'''
def is_polynomial(expr):
    #If the expression is a monomial or a singleton
    if is_monomial(expr):
        return True
    
    #If the monomial test fails with < 2 terms
    elif not isinstance(expr, Add):
        return False

    #Make sure each term in the polynomial is a monomial
    else:
        for i in range(0, len(expr.args)):
            if not is_monomial(expr.args[i]):
                print(srepr(expr))
                return False
    return not duplicate_monomials(expr)



'''
    duplicate_monomials(expr) - determines if any of the monomials in a
        polynomial can be combined.
    preconditions: polynomial is otherwise well formed
    returns:    true if there are any monomials that could be combined
                false otherwise
'''
def duplicate_monomials(expr):
    monomials = []
    
    #collect the bases if there's an exponent, just look
    #at the base
    for i in range(0, len(expr.args)):
        if isinstance(expr.args[i], Pow):
            monomials.append(expr.args[i].args[0])
        else:
            monomials.append(expr.args[i])
        #Check to see if any of the other monomials
        #are divisible with integer quotient and 0
        #remainder
        if i <= len(expr.args) - 2:
            for j in range(i+1, len(expr.args)):
                if(const_divisible(expr.args[i], expr.args[j])):
                    print(expr.args[i], expr.args[j])
                    return True

    print("what")
    #Check for any duplicates 
    return len(monomials) != len(set(monomials))

'''
    const_divisible(expr1, expr2) - returns whether the quotient of two
        expressoins is a constant with no remainder
        returns:    true if division produces constant w/no remainder
                    false otherwise
'''
def const_divisible(expr1, expr2):
    q, r = div(expr1, expr2, domain='ZZ')
    return isinstance(q, Number) or \
            isinstance(q, NumberSymbol) and \
            r == 0

