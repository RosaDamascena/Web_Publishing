<!-- ParentChild.vue -->

<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild 
      :my-msg="myMsg"
      @update-name="updateName"
    />
    <!-- 동적 바인딩 -->
    <button @click="$emit('someEvent')">클릭 1</button>
    <button @click="buttonClick">클릭 2</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
  import ParentGrandChild from '@/components/ParentGrandChild.vue'

  // 1. 문자열 배열 선언 방식
  // defineProps(['myMsg'])

  // 2. 객체 선언 방식(권장)
  // defineProps({
  //   myMsg: String,
  //   // myMsg: {
  //   //   type: String,
  //   //   required: true,
  //   // }
  // })

  // const props = defineProps({
  //   myMsg: String,
  //   dynamicProps: String,
  // })

  // console.log(props)
  // console.log(props.myMsg)

  // 3. 다양한 객체 선언 방식
  defineProps({
    myMsg: {
      type: String,
      required: true,
      // validator(value) {
      //   return ['success', 'warning', 'danger'].includes(value)
      // }
      validator(value) {
        const validValues =  ['success', 'warning', 'danger']
        if (!validValues.includes(value)) {
          console.error('에러입니다!')
          return false
        }
        return true
      }
    }
  })

  // emit 선언 방식
  const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])
  // const emit = defineEmits()


  const buttonClick = function () {
    emit('someEvent')
  }

  const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
  }

  const updateName = function () {
    emit('updateName')
  }

</script>

<style scoped>

</style>