<template>
    <div>
      <h1>게시글 상세 조회 페이지</h1>
    </div>
    <div>
      <p>id : {{ post.id }}</p>
      <p>title : {{ post.title }}</p>
      <p>content : {{ post.content }}</p>
      <p>created_at : {{ post.created_at }}</p>
      <p>updated_at : {{ post.updated_at }}</p>
    </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref } from 'vue'
  import { useRoute } from 'vue-router'

  const route = useRoute()
  const pk = route.params.pk

  const post = ref({})

  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
  })
  .then((res) => {
      console.log(res.data)
      post.value = res.data
    })
  .catch((err) => {
      console.log(err)
  })
</script>

<style scoped>

</style>