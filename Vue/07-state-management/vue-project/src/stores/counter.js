import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // state
  // const count = ref(100)

  // getters
  // const doubleCount = computed(() => count.value * 2)

  // actions
  // function increment() {
  //   count.value++
  // }

  // return { count, doubleCount, increment }


  let id = 0
  const todos = ref([
    {
      id: id++,
      title: 'Todo 1',
      completed: false
    },
    {
      id: id++,
      title: 'Todo 2',
      completed: false
    },
    {
      id: id++,
      title: 'Todo 3',
      completed: false
    },
    {
      id: id++,
      title: 'Todo 4',
      completed: false
    },
    {
      id: id++,
      title: 'Todo 5',
      completed: false
    },
  ])

  const addTodo = (todoText) => {
    todos.value.push({
      id: id++,
      title: todoText,
      completed: false
    })
  }

  const deleteTodo = (todoId) => {
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    todos.value.splice(index, 1)
  }

  const updateTodo = (todoId) => {
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        todo.completed =!todo.completed
      }
      return todo
    })
  }

  const doneTodosCount = computed(() => {
    return todos.value.filter((todo) => todo.completed).length
  })

  return {
    todos,
    addTodo,
    deleteTodo,
    updateTodo,
    doneTodosCount,
  }
})
