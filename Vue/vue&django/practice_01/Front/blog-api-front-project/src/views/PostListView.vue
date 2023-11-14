<template>
    <div>
      <RouterLink :to="{name: 'postCreate'}">게시글 생성하기</RouterLink>
      <h1>게시글 목록 페이지</h1>
      <hr>
    </div>
    <div
    v-for="post in store.postList"
    :key="post.pk"
    @click="goToDetail(post.pk)"
    class="post-link"
    >
      <h3>{{ post.pk }} 번 글 | {{ post.title }}</h3>
      <hr>
    </div>
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  import { onMounted } from 'vue'
  import { usePostStore } from '@/stores/post'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const store = usePostStore()
  
  onMounted(() => {
    store.getPostList()
  })
// 현재 컴포넌트가 마운트 되고 난 후에, axios 요청을 보낼 것


  const goToDetail = (pk) => {
    router.push({name: 'detail', params: {pk: pk}})
  }
</script>

<style scoped>
  .post-link {
    cursor: pointer;
  }

  .post-link :hover {
    background-color: gray;
    transition: 3s;
  }
</style>