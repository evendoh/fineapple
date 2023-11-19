<template>
    <div>
      <h1>게시판</h1>
      <RouterLink :to="{name: 'CreateView'}">
        [글쓰기]
      </RouterLink>
      <ArticleList />
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink } from 'vue-router'
  import ArticleList from '@/components/ArticleList.vue';
  import ArticleListItem from '@/components/ArticleListItem.vue';
  
  const store=useCounterStore()
  onMounted(() => {
    store.getArticles()
  })
  </script>
  
  <style>
  
  </style>
  