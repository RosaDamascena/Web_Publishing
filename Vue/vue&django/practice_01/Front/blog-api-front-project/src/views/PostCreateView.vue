<template>
    <div>
      <h1>게시글 생성 페이지</h1>
      <!-- form -->
      <form @submit.prevent="createPost">
        <!-- 선택할 카테고리 목록 -->
        <label for="category">카테고리</label>
        <select id="category" v-model="data.category">
          <option 
          v-for="category in store.categoryList" 
          :key="category.id" 
          :value="category.id"
          >
            {{ category.name }}
          </option>
        </select>
        <!-- 제목 -->
        <label for="title">제목</label>
        <input type="text" id="title" v-model="data.title">
        <!-- 내용 -->
        <label for="content">내용</label>
        <input type="text" id="content" v-model="data.content">
        <!-- 버튼 : 게시글 생성 -->
        <button>게시글 생성</button>
      </form>
    </div>
</template>

<script setup>
  // input 태그에 입력한 내용을 담을 수 있는 객체
  // 카테고리 -> db에 있는 목록을 보여주어야 한다.
    // store에서 category 전체 목록 
    // axios 요청 보내서 응답 받은 데이터
  import axios from 'axios'
  import { ref } from 'vue'
  import { useCategoryStore } from '@/stores/category' 
  import { onMounted } from 'vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const store = useCategoryStore()

  onMounted(() => {
    store.getCategoryList()
  })

  const data = ref({
    title: '',
    content: '',
    category: 1,
  })
  // const title = ref('')
  // const content = ref('')
  // const category = ref(1)
  

  const createPost = () => {
    axios({
      method: 'POST',
      url: 'http://127.0.0.1:8000/api/v1/posts/',
      data: data.value,
      // data: {
      //   title: title.value,
      //   content: content.value,
      //   category: category.value,
      // }
    })
    .then(res => {
      router.push({name: 'detail', params:{pk: res.data.id}})
    })
    .catch(err => {
      console.log(err)
    })
  }

</script>

<style scoped>

</style>