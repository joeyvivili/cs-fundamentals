; to run the scheme code in this file:
;       option 1: use the online cs61a Scheme interpreter at: https://code.cs61a.org/
;       option 2: to load a Scheme file called f.scm, type "python3 scheme -i f.scm" in terminal
;       option 3: type "python3 editor" in a terminal, and the web-based scheme editor will open in a browser window (at http://127.0.0.1:31415/)
;                   The Run button loads the current assignment's .scm file and opens a Scheme interpreter, allowing you to try evaluating different Scheme expressions.


; (trace (sum 5))
(define-macro (trace expr)
    (let ((fn (car expr))
        (arg (car (cdr expr))))
        `(begin
            (define original ,fn)
            (define ,fn 
                (lambda (n) 
                    (begin (print ',fn n) (original n))))
            (define result (,fn ,arg))
            (define ,fn original)
            result
        )
    )
)

(define (square n) (* n n))
; def pow_exp(base, exp):
;     """Return the result of raising base to the power of exp
    
;     >>> pow_exp(2, 15)
;     32768
;     >>> pow_exp(3, 7)
;     2187
;     """
;     if exp == 0:
;         return 1
;     elif exp % 2 == 0:
;         return square(pow_exp(base, exp / 2))
;     else:
;         return base * pow_exp(base, exp - 1)
(define (pow-expr base exp)
    (cond ((zero? exp) '1)
        ((even? exp) (list 'square (pow-expr base (/ exp 2))))
        ((odd? exp) (list '* base (pow-expr base (- exp 1))))
    )
)

; discussion_12
; def up(n):
;     """Takes a positive integer n and return a linked list rope containing the digits of n 
;     that is the shortest rope in which each pair of adjacent numbers in the same list are in increasing order.

;     >>> s = up(314152667899)
;     >>> scheme_print(s)
;     (3 (1 4 (1 5 (2 6 (6 7 8 9 (9))))))
;     """
;     power = math.floor(math.log10(n))   # scheme equivalent: (/ (log x) (log 10))
;     first_digit, rest = n // 10**power, n % 10**power
;     second_digit = rest // 10**(power-1)
;     if n < 10:
;         return Link(n)
;     else:
;         if first_digit < second_digit:
;             return Link(first_digit, up(rest))
;         else:
;             return Link(first_digit, Link(up(rest)))
(define (up n)
  (if (< n 10)
      (list n)
      (let ((power (floor (/ (log n) (log 10)))))
        (let ((first-digit (quotient n (expt 10 power)))
              (rest (modulo n (expt 10 power)))
              (second-digit (quotient (modulo n (expt 10 power))
                                      (expt 10 (- power 1)))))
          (if (< first-digit second-digit)
              (cons first-digit (up rest))
              (list first-digit (up rest))))))
)