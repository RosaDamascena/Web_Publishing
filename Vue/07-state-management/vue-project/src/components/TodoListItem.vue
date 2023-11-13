<template>
    <div class="m-2">
      <span @click="store.updateTodo(todo.id)" :class="{'completed': todo.completed}">
        {{ todo.title }}
      </span>
      <button class="mx-1" @click="store.deleteTodo(todo.id)">Delete</button>
    </div>
</template>

<script setup>
  import { useCounterStore } from '@/stores/counter'
  
  const store = useCounterStore()

  defineProps({
    todo: Object,
  })
</script>

<style scoped>
  .completed {
    text-decoration: line-through;
  }
</style>