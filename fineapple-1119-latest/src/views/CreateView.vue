<template>
    <div>
      <h1>게시글 작성</h1>
      <form @submit.prevent="createArticle">
          제목 : <input type="text" v-model.trim="title">
          <br>
          내용 : <textarea v-model.trim="content"></textarea>
        <br>
        <input type="submit">
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios';
  import { useCounterStore } from '@/stores/counter';
  import { useRouter } from 'vue-router'
  
  const title = ref(null)
  const content = ref(null)
  
  const store = useCounterStore()
  const router = useRouter()
  
  const createArticle = function() {
    axios({
      method: 'post',
      url: `${store.API_URL}/articles/`,
      data: {
        title: title.value,
        content: content.value
      }
    }).then((res) => {
      console.log(res)
      router.push({ name: 'ArticleView' })
    }).catch((err) => {
      console.log(err)
    }
  )}
  
  </script>
  
  <style>
  
  </style>
  