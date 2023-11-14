import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const usePostStore = defineStore('post', () => {
  // 벡엔드 서버에 post 전체 목록 GET 요청
  const postList = ref([])
  const getPostList = () => {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/posts/'
    })
    .then(res => {
        postList.value = res.data
        console.log(res.data)
      })
    .catch(err => {
        console.log(err)
      })
    }

  return { getPostList, postList }
})
