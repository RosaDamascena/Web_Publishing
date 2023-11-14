<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" v-model.trim="content"></textarea><br>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'

  const router = useRouter()
  const store = useCounterStore()

  const title = ref(null)
  const content = ref(null)

  const createArticle = () => {
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/articles/`,
      data: {
        title: title.value,
        content: content.value
      },
    }).then(() => {
      router.push({name: 'ArticleView'})
    }).catch((err) => console.log(err))
  }
</script>

<style>

</style>
