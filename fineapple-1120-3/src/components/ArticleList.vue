<template>
    <div>
      <h3 class="listtitle">글 목록</h3>
      <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
      class="writelist"
       />
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter';
  import ArticleListItem from '@/components/ArticleListItem.vue';
  
  const store = useCounterStore()
  console.log(store.articles)
  </script>
  
  <style>
  .listtitle{
    color: #1E4B4C;
    text-decoration: none;
    font-size: 18px;
    transition: text-decoration 0.3s ease-in-out;
    font-family: 'Courier New', Courier, monospace;

  }
  .writelist {
    color: #1E4B4C;
    text-decoration: none;
    font-size: 18px;
    transition: text-decoration 0.3s ease-in-out;
    font-family: 'Courier New', Courier, monospace;

  }</style>