<template>
    <div>
      <p>{{ article.id }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <RouterLink :to = "{name:'DetailView', params: {id: article.id}}">
        [Detail]
      </RouterLink>
      <hr>
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  
  defineProps({
    article: Object
  })
  </script>
  