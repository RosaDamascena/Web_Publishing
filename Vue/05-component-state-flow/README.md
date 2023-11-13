# Passing Props

-----

## 1. Passing Props

### 같은 데이터 하지만 다른 컴포넌트

- 공통된 부모 컴포넌트에서 관리하는 것이 효율적이다.

- 부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)

### Props

- 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성


  
### One-Way Data Flow

- 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성

- one-way-down binding


### Props 특징

- 부모 속성이 업데이트되면 자식으로 흐르지만 그 반대는 안됨
- 즉, 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능
- 또한 부모 컴포넌트가 업데이트 될 때마다 자식 컴포넌트의 모든 props가 최신 값으로 업데이트 됨


### Props 세부사항

1. Props Name Casing

2. Static Props & Dynamic Props


### 1. Props Name Casing

- 선언 및 템플릿 참조 시
: camelCase (JS)

- 자식 컴포넌트로 전달 시
: kebab-case (html)


### 2. Static Props & Dynamic Props

-----

## 2. Component Events

### Component Events

- 부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)

- 부모가 prop 데이터를 변경하도록 소리쳐야 한다.

### $emit()

- 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
