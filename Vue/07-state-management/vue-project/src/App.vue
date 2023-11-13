<template>
    <div class="m-3">
      <h1>Todo Project</h1>
      <hr>
      <h3>완료된 Todo : {{ store.doneTodosCount }} / {{ store.todos.length }} 개</h3>
      <hr>
      <TodoList />
      <TodoForm class="my-3"/>
    </div>
</template>

<script setup>
 import { useCounterStore } from '@/stores/counter.js'
 import TodoForm from '@/components/TodoForm.vue'
 import TodoList from '@/components/TodoList.vue'

  const store = useCounterStore()

</script>
 
<style scoped>

</style>