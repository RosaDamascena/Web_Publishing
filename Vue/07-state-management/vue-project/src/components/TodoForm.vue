<template>
    <div>
      <form @submit.prevent="createTodo(todoText)" ref="formElem">
        <input type="text" v-model="todoText">
        <input type="submit">
      </form>
    </div>
</template>

<script setup>
  import { useCounterStore } from '@/stores/counter'
  import { ref } from 'vue'

  const store = useCounterStore()
  const todoText =ref('')
  const formElem = ref(null)

  const createTodo = (todoText) => {
    store.addTodo(todoText)
    formElem.value.reset()
  }

</script>

<style scoped>

</style>