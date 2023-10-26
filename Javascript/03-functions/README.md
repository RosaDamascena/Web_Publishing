# JavaScript Reference data types

-----

## 1. 함수

### ▶︎ Function

- 참조 자료형에 속하며 모든 함수는 Fuction object

### ▶︎ 참조 자료형 (Reference type)

- 객체의 주소가 저장되는 자료형 (가변, 주소가 복사)

### ▶︎ 함수 구조

- 함수의 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statement
- return 값이 없다면 undefined를 반환

### ▶︎ 함수 정의 2가지 방법

- 선언식 (function declaration)
  - 익명 함수 사용 불가능
  - 호이스팅 있음

```js
function add(num1, num2) {
  return num1 + num2
}

add(1, 2) // 3
```

- 표현식 (function expression)
  - 익명 함수 사용 가능
  - 호이스팅 없음
  - 사용 권장

```js
const sub = function (num1, num2) {
  return num1 - num2
}

sub(2, 1) //1
```

### ▶︎ 함수 표현식 특징

- 함수 이름이 없는 '익명 함수'를 사용할 수 있음
- 선언식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음

### ▶︎ 매개 변수

#### 1. 기본 함수 매개변수

- 값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

```js
const greeting = function (name= 'Anonymous') {
  return `Hi ${name}`
}

greeting()  // Hi Anonymous
```

#### 2. 나머지 매개 변수

- 임의의 수의 인자를 '배열'로 허용하여 가변 인자를 나타내는 방법
- 함수 정의 시 나머지 매개변수 하나만 작성할 수 있음
- 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함

```js
const myFunc = function (param1, param2, ...restParams) {
  return [param1, param2, restParams]
}

myFunc(1, 2, 3, 4, 5) //[1,2, [3, 4, 5]]
myFunc(1, 2)  // [1, 2, []]
```

### ▶︎ 매개변수와 인자의 개수 불일치

- 매개변수 개수 > 인자 개수
- 누락된 인자는 undefined로 할당

```js
const threeArgs = function (param1, param2, param3) {
  return [param1, param2, param3]
}

threeArgs()   // [undefined, undefined, undefined]
threeArgs(1)  // [1, undefined, undefined]
threeArgs(2, 3) //  [2, 3, undefined]
```

- 매개변수 < 인자 개수
- 초과 입력한 인자는 사용하지 않음

```js
const noArgs = function () {
  return 0
}

noArgs(1, 2, 3)   // 0

const twoArgs = function (param1, param2) {
  return [param1, param2]
}
threeArgs(1, 2, 3) //  [1, 2]
```

### ▶︎ Spread Syntax

- '...' (Spread syntax) : 전개 구문
- 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것(확장, 전개)
- 전개 대상에 따라 역할이 다름
  - 배열이나 객체의 요소를 개별적인 값으로 분리하거나 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등

#### 1. 함수와의 사용
- 함수 호출 시 인자 확장
- 나머지 매개변수(압축)

#### 2. 객체와의 사용
- 객체 파트에서 진행

#### 3. 배열과의 활용
- 배열 파트에서 진행


### ▶︎ 화살표 함수

#### 화살표 함수 표현식
- 함수 표현식의 간결한 표현법

#### 화살표 함수 작성 과정

1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성
   
2. 함수의 매개변수가 하나 뿐이라면, 매개변수의 '()' 제거 가능 (단, 생략하지 않는 것을 권장)
   
3. 함수 본문의 표현식이 한 줄이라면, '{}', 'return' 제거 가능


```js
const arrow1 = function (name) {
  return `hello, ${name}`
}

// 1. function 키워드 삭제 후 화살표 작성
const arrow2 = (name) => { return `hello, ${name}` }

// 2. 인자가 1개일 경우에만 () 생략 가능
const arrow3 = name => { return `hello, ${name}` }

// 3. 함수 본문이 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
const arrow4 = name => `hello, ${name}`
```

### ▶︎ 화살표 함수 심화

-----

## 2. 객체

### ▶ Object

- 키로 구분된 데이터 집합을 저장하는 자료형

### ▶ 객체 구조

- 중괄호를 이용해 작성
- 중괄호 안에는 key:value 쌍으로 구성된 속성을 여러 개 작성 가능
- key는 문자형만 허용
- value는 모든 자료형 허용

### ▶ 속성 참조

- 점(.) 또는 대괄호([])로 객체 요소 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

### ▶ in 연산자

- 속성이 객체에 존재하는지 여부를 확인

### ▶ Method

- 객체 속성에 정의된 함수
- object.method() 방식으로 호출
- 메서드는 객체를 '행동'할 수 있게 함

```js
console.log(user.greeting())  // hello
```

### ▶ this

- 'this' 키워드를 사용해 객체에 대한 특정한 작업을 수행 할 수 있음

### ▶ this keyword

- 함수나 메서드를 호출한 객체를 가리키는 키워드
- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

```js
const person = {
  name: 'Alice',
  greeting: function () {
    return `Hello my name is ${this.name}`
  },
}

console.log(person.greeting())
// Hello my name is Alice
```

### ▶ this 호출 방법에 따른 대상

1. 단순 호출
  - 대상 : 전역 객체

```js
const myFunc = function () {
  return this
}
console.log(myFunc()) // window
```

2. 메서드 호출
  - 대상 : 메서드를 호출한 객체 

```js
const myObj = {
  data: 1,
  myFunc: function () {
    return this
  }
}
console.log(myObj.myFunc()) // myObj
```

### ▶ 중첩된 함수에서의 this 문제점과 해결책

- forEach의 인자로 작성된 콜백 함수는 일반적인 함수호출이기 때문에 this가 전역 객체를 가리킴
```js
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      console.log(this) // window
    })
  }
}
console.log(myObj2.myFunc())
```

- 해결책
  - 화살표 함수는 자신만의 this를 가지지 않기 때문에 외부(상위) 함수에서의 this 값을 가져옴

```js
const myObj3 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach((number) => {
      console.log(this) // myObj3
    })
  }
}
console.log(myObj3.myFunc())
```

### ▶ JavaScript 'this' 정리

- js에서 this는 함수가 호출되는 방식에 따라 결정되는 현재 객체를 나타냄
- js의 함수는 호출될 때 this를 암묵적으로 전달 받음
- Python의 self와 java의 this가 선언 시 값이 이미 정해지는 것에 비해 js의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨(동적 할당)

### ▶ 추가 객체 문법

#### 1. 단축 속성
- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우
- 단축 구문을 사용할 수 있음

#### 2. 단축 메서드
- 메서드 선언 시 function 키워드 생략 가능

#### 3. 계산된 속성 (Computed property name)
- 키가 대괄호([])로 둘러쌓여 있는 속성
- 고정된 값이 아닌 변수 값을 사용할 수 있음

#### 4. 구조 분해 할당 (destructing assignment)
- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

```js
const userInfo = {
  firstName: 'Alice',
  userId: 'alice123',
  email: 'alice123@gmail.com'

// const firstName = userInfo.name
// const userId = userInfo.userId
// const email = userInfo.emai
// const { firstName } = userInfo
// const { firstName, userId } = userInfo
const { firstName, userId, email } = userInfo

console.log(firstName, userId, emai)
// Alice alice123 alice123@gmail.com
}
```

- 함수의 매개변수로 객체 구조 분해 할당 활용 가능

```js
function printInfo({ name, age, city }) {
  console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
}

const person = {
  name: 'Bob',
  age: 35,
  city: 'London',
}

// 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
printInfo(person) 
// '이름: Bob, 나이: 35, 도시: London'
```

#### 5. Object with '전개 구문'
- 객체 복사
  - 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능

```js
const obj = { b: 2, c: 3, d: 4 }
const newObj = { a: 1, ...obj, e: 5 }
console.log(newObj) 
// {a: 1, b: 2, c: 3, d: 4, e: 5}
```

#### 6. 유용한 객체 메서드
- Object.keys()
- Object.values()

```js
const profile = {
  name: 'Alice',
  age: 30,
}

console.log(Object.keys(profile)) 
// ['name', 'age']

console.log(Object.values(profile)) 
// ['Alice', 30]
```

#### 7. Optional chaining ('?.')
- 속성이 없는 중첩 객체를 에러 없이 접근 할 수 있음
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생한 것 대신 평가를 멈추고 undefined를 반환

```js
const user = {
  name: 'Alice',
  greeting: function () {
    return 'hello'
  }
}

console.log(user.address.street) 
// Uncaught TypeError: Cannot read properties of undefined (reading 'street')
console.log(user.address?.street) // undefined

console.log(user.nonMethod()) 
// Uncaught TypeError: user.nonMethod is not a function
console.log(user.nonMethod?.()) // undefined

```

- Optional chaning이 없다면 다음과 같이 '&&' 연산자를 사용해야 함

```js
const user = {
  name: 'Alice',
  greeting: function () {
    return 'hello'
  }
}

console.log(user.address && user.address.street) // undefined
```

- Optional chaing 주의사항

1. Optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야 함(남용 X)
  - 왼쪽 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용

```js
// Bad
user?.address?.street

// Good
user.address?.street

// 위 예시 코드 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
// user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문에
```

2. Optional chaining 앞의 변수는 반드시 선언되어 있어야 함

```js
console.log(myObj?.address) 
// Uncaught ReferenceError: myObj is not defined
```


### ▶ JSON

- JavaScript Object Notation
- key-value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 '문자열'
- JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함

### ▶ Object <-> JSON 변환하기

```js
const jsObject = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
}

// Object -> JSON
const objToJson = JSON.stringify(jsObject)
console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
console.log(typeof objToJson)  // string

// JSON -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
console.log(typeof jsonToObj)  // object
```

### ▶ new 연산자

#### 상황
- JS에서 객체를 하나 생성한다고 한다면?
  - 하나의 객체를 선언하여 생성

- 동일한 형태의 객체를 또 만든다면?
  - 또 다른 객체를 선언하여 생성해야 함

#### 해결
- 사용자 정의 객체 타입을 생성
- 매개 변수
  - 1. constructor : 객체 인스턴스의 타입을 기술(명세)하는 함수
  - 2. arguments : constructor와 함께 호출될 값 목록

```js
new constructor[([arguments])]
```

### ▶ new 연산자 활용

```js
function Member(name, age, sId) {
  this.name = name
  this.age = age
  this.sId = sId
}

const member3 = new Member('Bella', 21, 20226543)

console.log(member3) // Member { name: 'Bella', age: 21, sId: 20226543 }
console.log(member3.name) // Bella
```

-----

## 3. 배열

### ▶ Object

- 키로 구분된 데이터 집합(data collection)을 저장하는 자료형

### ▶ Array

- 순서가 있는 데이터 집합을 저장하는 자료구조

### ▶ 배열 구조

- 대괄호([])를 이용해 작성
- 배열 요소 자료형 : 제약 없음
- length 속성을 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음

### ▶ 주요 메서드

- push / pop
  - 배열 끝 요소를 추가 / 제거

- unshift / shift
  - 배열 앞 요소를 추가 / 제거

### ▶ Array Helper Methods

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 함수를 받는 것이 특징(콜백 함수)

### ▶ forEach

- 인자로 주어진 함수(콜백함수)를 백열 요소 각각에 대해 실행

```js
arr.forEach(callback(item[, index[, array]]))

arr.forEach(function(item, index, array) {
  // do something
})
```
- 콜백함수는 3가지 매개변수로 구성
  - 1. item : 처리할 배열의 요소
  - 2. index : 처리할 배열 요소의 인데스(선택 인자)
  - 3. array : forEach를 호출한 배열(선택 인자)

- 반환값 : undefined

```js
const names = ['Alice', 'Bella', 'Cathy',]

// 일반 함수
names.forEach(function (item, index, array) {
  console.log(`${item} / ${index} / ${array}`)
})

// 화살표 함수
names.forEach((item, index, array) => {
  console.log(`${item} / ${index} / ${array}`)
})
```

### ▶ 콜백 함수(Callback function)

- 다음 함수에 인자로 전달되는 함수
- 외부 함수내에서 호출되어 일존의 루틴이나 특정 작업을 진행

```js
// 1번
const numbers1 = [1, 2, 3,]
numbers.forEach(function (num) {
  console.log(num ** 2)
})
// 1
// 4
// 9

// 2번
const numbers2 = [1, 2, 3,]
const callBackFunction = function (num) {
  console.log(num ** 2)
}
// 1
// 4
// 9

numbers.forEach(callBackFunction)
```

### ▶ map

- 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출하고, 함수 호출 결과를 모아 새로운 배열을 반환

```js
arr.map(callback(item[, index[, array]]))

const newArr = array.map(function(item, index, array) {
  // do something
})
```

- map 구조
  - 1. item : 처리할 배열의 요소
  - 2. index : 처리할 배열 요소의 인데스(선택 인자)
  - 3. array : forEach를 호출한 배열(선택 인자)

- 반환값 : 배열의 각 요소에 대해 실행한 callback의 결과를 모든 새로운 배열
- 기본적으로 forEach 동작 원리와 같지만 forEach와 달리 새로운 배열을 반환함

```js
// 1번
const names = ['Alice', 'Bella', 'Cathy',]

const result1 = names.map(function (name) {
  return name.length
})

const result2 = names.map((name) => {
  return name.length
})

console.log(result1) // [5, 5, 5]
console.log(result2) // [5, 5, 5]


// 2번
const numbers = [1, 2, 3,]

const doubleNumber = numbers.map((number) => {
    return number * 2
})

console.log(doubleNumber) // [2, 4, 6]
```


### ▶ 배열 순회 종합

#### for loop
- 배열의 인덱스를 이용하여 각 요소에 접근
- break, continue 사용 가능

#### for...of
- 배열 요소에 바로 접근 가능
- break, continue 사용 가능

#### forEach
- 간결하고 가독성이 높음
- callback 함수를 이용하여 각 요소를 조작하기 용이
- break, continue 사용 불가능
- 사용 권장

```js
const names = ['Alice', 'Bella', 'Cathy',]

// for loop
for (let idx = 0; idx < names.length; idx++) {
  console.log(idx, names[idx])
}

// for...of
for (const name of names) {
  console.log(name)
}

// forEach
names.forEach((name, idx) => {
  console.log(idx, name)
})
```

### ▶ 추가 배열 문법

#### 1. Array with '전개 구문'
- 배열 복사

```js
let parts = ['어깨', '무릎']
let lyrics = ['머리', ...parts, '발']

console.log(lyrics)
// ['머리', '어깨', '무릎', '발']
```

#### 2. 기타 Array Helper Methods

- filter
  - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

- find
  - 콜백 함수의 반환 값이 참이면 해당 요소를 반환

- some
  - 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환

- every
  - 배열의 모든 요소가 판별 함수를 통과하면 참을 반환


-----