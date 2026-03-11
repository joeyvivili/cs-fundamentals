(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (index-val i s)
    (if (null? s) nil
      (cons (list i (car s)) (index-val (+ i 1) (cdr s)))
    )
  )
  (index-val 0 s)
)
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists S1 and S2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? s1 s2)
  ; BEGIN PROBLEM 16
  (cond
    ((null? s1) s2)
    ((null? s2) s1)
    (else (let 
              (
                (e1 (car s1))
                (e2 (car s2))
              )
              (cond
                  ((ordered? e1 e2) (cons e1 (merge ordered? (cdr s1) s2)))
                  ((ordered? e2 e1) (cons e2 (merge ordered? s1 (cdr s2))))
                  (else (cons e1 (merge ordered? (cdr s1) (cdr s2))))
              )
    ))
  )
)
  ; END PROBLEM 16

;; Optional Problem 2

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
; logic for let -> lambda
; let variable names = lambda parameters
; let values corresponding to each variable = lambda arguments
; let body = lambda body
; let format: (let ( (name-1 val-1) (name-2 val-2) ...) (body/return value))
; lambda format:((lambda (name-1 name2 ...) (body/return value)) argument-1 argument-2)
(define (let-to-lambda expr)
  (cond ((atom? expr) expr)

        ((quoted? expr) expr)

        ((lambda? expr)
         (cons 'lambda
               (cons (cadr expr)
                     (map let-to-lambda (cddr expr)))))

        ((define? expr)
         (cons 'define
               (cons (cadr expr)
                     (map let-to-lambda (cddr expr)))))

        ((let? expr)
         (let ((bindings (cadr expr))
                (body (cddr expr)))
                (let ((vars (car (zip bindings)))
                      (vals (cadr (zip bindings))))
           (cons (cons 'lambda
                       (cons vars
                             (map let-to-lambda body)))
                 (map let-to-lambda vals)))))

        (else
         (map let-to-lambda expr))))

; Some utility functions that you may find useful to implement for let-to-lambda

(define (zip pairs)
  (if (null? pairs)
      (cons nil (cons nil nil))   ; (() ())
      (cons (map car pairs)
            (cons (map cadr pairs) nil)))
)



