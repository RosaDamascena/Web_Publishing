# Controlling Event

-----

## 1. 이벤트

### ▶︎ 웹에서의 이벤트

- 버튼을 클릭했을 때 팝업 창이 출력되는 것
- 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
- 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것

=> 일상에서의 이벤트처럼 웹에서도 이벤트를 통해 특정 동작을 수행함

### ▶︎ event

- 무언가 일어났다는 신호, 사건
- 모든 DOM 요소는 이러한 event를 만들어 냄

### ▶︎ event object

- DOM에서 이벤트가 발생하였을 때 생성되는 객체
- DOM 요소는 event를 받고 받은 event를 처리 할 수 있음


### ▶︎ event handler

- 이벤트가 발생하였을 때 실행되는 함수
- 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것

### ▶︎ .addEventListener()

- 대표적인 이벤트 핸들러 중 하나
- 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출
- 대상에 특정 Event가 발생하면 지정한 이벤트를 받아 할 일을 등록함

```js
EventTarget.addEventListener(type, handler)
```

- type
  - 수신할 이벤트 이름

- handler
  - 발생한 이벤트 객체를 수신하는 콜백 함수
  - 콜백함수는 발생한 Event object를 유일한 매개변수로 받음


### ▶︎ 버블링(Bubbling)

- 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상

- 가장 최상단의 조상 요소(document)를 만날 때까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작

=> 이벤트가 제일 깊은 곳에 있는 요소에서 시작해 부모 요소를 거슬러 올라가며 발생하는 것이 마치 물 속 거품과 닮았기 때문


-----

## 2. event handler 활용

### ▶︎ currentTarget 주의사항

- console.log()로 event 객체를 출력할 경우 currentTarget 키의 값은 null을 가짐

- currentTarget은 이벤트가 처리되는 동안에만 사용할 수 있기 때문

- 대신 console.log(event.currentTarget)을 사용하여 콘솔에서 확인 가능

