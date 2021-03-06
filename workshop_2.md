# Basics

პითონში 2 + 2 -ს ქვია *expression* (გამოსახულება), რომელიც არის ყველაზე საბაზისო ინსტრუქცია კომპიუტერისთვის. 

გამოსახულება (*expression*) შედგება რამდენიმე კომპონენტისგან: 
- მნიშვნელობები (*values*) (მაგ. 2) 
- ოპერტაორები (*operators*) (მაგ. +)
- შეფასება (*evaluate*), რაც ნიშნავს, რომ ერთ მნიშვნელობამდე დაიყვანება გამოსახულება

2 + 2 შეფასდება და მივიღებთ ერთ მნიშვნელობას 4 -ს, ერთი მნიშვნელობა ოპერატორების გარეშე ისევ გამოსახულებაა, რომელიც თავის თავად შეფასდება.
მაგ. 2 არის 2

Operator (ოპერატორი) | Operation (ოპერაცია) | Example (მაგალითი) | Evaluates to (ფასდება) . . .
--- | --- | --- | --- 
| ** | Exponent (ახარისხება) | 2 ** 3 | 8
| %  | Modulus/remainder (მოდულუსი, ნაშთის ოპერატორი)  | 22 % 8 | 6
| // | Integer; division/floored; quotient | 22 // 8 | 2
| /  | Division | 22 / 8 | 2.75
| *  | Multiplication | 3 * 5 | 15
| -  | Subtraction | 5 - 2 | 3
| +  | Addition | 2 + 2 | 4

ოპერაციების თანმიმდევრობა იგივეა როგორც მათემატიკაში, ფრჩხილებით შეგიძლიათ მიანიჭოთ უპირატესობა expression -ს 

```python
>>> 2 + 3 * 6
20

>>> (2 + 3) * 6
30
```


# Syntax

როგორც ჩვეულებრივ ენაში, ისევე პროგრამირებაში გვაქვს "გრამატიკა", რომელსაც სინტაქსს ვუწოდებთ, შესაბამისად თუ კოდს არასწორად დაწერთ, კომპიუტერს ამით ვერაფერს გაუფუჭებთ, პითონი ამაზე გეტყვით, რომ სინტაქსური პრობლემა გაქვთ კოდში.

მაგ. 2 +  (SyntaxError: invalid syntax) არის შეცდომა, რადგან ოპერატორის შემდეგ სხვა მნიშვნელობა არ წერია 

