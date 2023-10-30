# Asynchronous JavaScript

------

## 1. 비동기

### Synchronous (동기)

- 프로그램의 실행 흐름이 순차적으로 진행
- 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식

### Asynchronous (비동기)

- 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식
- 작업의 완료 여부를 신경 쓰지 않고 동시에 다른 작업들을 수행할 수 있음
- 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 줄 수 있음

### Asynchronous 특징

- 병렬적 수행
- 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

------

## 2. JavaScript와 비동기

### Thread

- 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미
- Single Thread 언어, JavaScript

### JavaScript

- JS는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어로 동시에 여러 작업을 처리할 수 없음

### 브라우저 환경에서의 JavaScript 비동기 처리 동작 방식

1. 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리된다.
2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도로 처리하도록 한다.
3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue(FIFO)에 순서대로 들어간다.
4. Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된 작업을 Call Stack으로 보낸다.


### 비동기 처리 동작 요소

1. Call Stack
  - 요청이 들어올 때마다 순차적으로 처리하는 Stack(LIFO)
  - 기본적인 JS의 Single Thread 작업 처리

2. Web API
  - JS 엔진이 아닌 브라우저에서 제공하는 runtime 환경
  - 시간이 소요되는 작업을 처리
  - setTimeout, DOM Event, AJAX 요청 등

3. Task Queue (Callback Queue)
  - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)

4. Event Loop
  - Task(작업)가 들어오길 기다렸다가 Task가 들어오면 이를 처리하고, 처리할 작업이 없는 경우엔 잠드는, 끊임없이 돌아가는 자바스크립트 내 루프
  - Call Stack과 Task Queue를 지속적으로 모니터링
  - Call Stack이 비어 있는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push


------

## 3. AJAX

### AJAX (Asynchronous JavaScript + XML)

- JS의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술

### XMLHttpRequest 객체

- 서버와 상호작용할 때 사용하며 페이지의 새로고침 없이도 URL에서 데이터를 가져올 수 있음
- 사용자의 작업을 방해하지 않고 페이지의 일부를 업데이트
- 주로 AJAX 프로그래밍에 많이 사용됨

### Axios

- JavaScript에서 사용되는 Promise 기반 HTTP 클라이언트 라이브러리
- 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구

### Axios 구조

- get, post 등 여러 http request method 사용 가능
- then 메서드를 사용하여 '성공하면 수행할 로직'을 작성
- catch 메서드를 사용하여 '실패하면 수행할 로직'을 작성

-------

## 4. Callback과 Promise

### 비동기 처리의 단점  
- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리한다는 것
- 코드의 실행 순서가 불명확하다는 단점 존재

### 비동기 콜백
- 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
- 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작 할 수 있게 함
- 작업의 순서와 동작을 제어하거나 결과를 처리하는 데 사용

### 비동기 콜백의 한계

- 비동기 콜백 함수는 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용됨
- 콜백 지옥 발생 할 수 있음

### Promise (프로미스)

- JS에서 비동기 작업의 결과를 나타내는 객체
- 비동기 작업이 완료되었을 때 결과 값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능을 제공
- 콜백 지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- Promise 기반의 클라이언트가 바로 이전에 사용한 Axios 라이브러리
  - 성공 시 then()
  - 실패 시 catch()
  - default 값 finally()

```js
let likePizza = true
const pizza = new Promise((resolve, reject) =>{
  if (likePizza)
    resolve('피자를 주문합니다.')
  else
    reject('피자를 주문하지 않습니다.')
})

pizza
  .then(
    result => console.log(result)
  )
  .catch(
    err => console.log(err)
  )
  .finally (
    () => console.log('완료')
  )
```

### Promise가 보장하는 것

- 콜백 함수는 JS의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
- 반면 Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
- 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 호출 순서를 보장하며 동작
- .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음
- 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
- Chaning은 Promise의 가장 뛰어난 장점

-----
