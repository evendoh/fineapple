<template>
    <div class="box">
      <p>{{ article.id }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <RouterLink :to = "{name:'DetailView', params: {id: article.id}}">
        [상세정보]
      </RouterLink>

    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  
  defineProps({
    article: Object
  })
  </script>
  <style>
.box {
  border: 1px solid;
  border-radius: 2px;
  padding: 10px;
}
</style>
  
<!-- 

   <template>
    <div class="article-list">
      <div v-for="article in articles" :key="article.id" class="article-box">
        <h2 class="article-title">{{ article.title }}</h2>
        <p class="article-content">{{ article.content }}</p>
        <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
          [상세정보]
        </RouterLink>
      </div>
    </div>
  </template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
<style scoped>
.article-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.article-box {
  width: 30%; /* 더 넓거나 좁게 조절하려면 이 값을 변경하세요 */
  padding: 16px;
  margin-bottom: 16px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.article-box:hover {
  transform: scale(1.05);
}

.article-title {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 8px;
}

.article-content {
  font-size: 1rem;
  color: #555;
}

RouterLink {
  color: #1e4b4c;
  text-decoration: none;
  font-weight: bold;
  display: inline-block;
}

RouterLink:hover {
  text-decoration: underline;
}
</style> -->
<!-- 
   <template>
    <div class="box">
      <p class="article-id">{{ article.id }}</p>
      <p class="article-title">제목 : {{ article.title }}</p>
      <p class="article-content">내용 : {{ article.content }}</p>
      <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
        [상세정보]
      </RouterLink>
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router';
  
  defineProps({
    article: Object,
  });
  </script>
  
  <style scoped>
  .box {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
    transition: transform 0.3s ease-in-out;
  }
  
  .box:hover {
    transform: scale(1.05);
  }
  
  .article-id {
    font-size: 14px;
    color: #333;
  }
  
  .article-title {
    font-size: 18px;
    font-weight: bold;
    color: #1e4b4c;
    margin-bottom: 8px;
  }
  
  .article-content {
    font-size: 16px;
    color: #555;
  }
  
  RouterLink {
    color: #1e4b4c;
    text-decoration: none;
    font-weight: bold;
    margin-top: 8px;
    display: inline-block;
  }
  
  RouterLink:hover {
    text-decoration: underline;
  }
  </style>
   -->
<!-- 
   <template>
    <div class="board-container">
      <h1 class="board-title">게시판</h1>
      <RouterLink :to="{ name: 'CreateView' }" class="write-link">
        [글쓰기]
      </RouterLink>
      <ArticleList />
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink } from 'vue-router';
  import ArticleList from '@/components/ArticleList.vue';
  
  const store = useCounterStore();
  
  onMounted(() => {
    store.getArticles();
  });
  </script>
  
  <style scoped>
  /* 게시판 스타일 */
  .board-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }
  
  .board-title {
    color: #1E4B4C;
    font-size: 28px;
    margin-bottom: 10px;
  }
  
  /* [글쓰기] 링크 스타일 */
  .write-link {
    color: #1E4B4C;
    text-decoration: none;
    font-size: 18px;
    transition: text-decoration 0.3s ease-in-out;
  }
  
  .write-link:hover {
    text-decoration: underline;
  }
  </style>
   -->
<!-- 
   <template>
    <div class="article-list">
      <div v-for="article in articles" :key="article.id" class="article-box">
        <h2 class="article-title">{{ article.title }}</h2>
        <p class="article-content">{{ article.content }}</p>
        <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
          [상세정보]
        </RouterLink>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink } from 'vue-router';
  import ArticleList from '@/components/ArticleList.vue';
  
  const store = useCounterStore();
  
  onMounted(() => {
    store.getArticles();
  });
  </script>
  
  <style scoped>
  .article-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  
  .article-box {
    width: 30%; /* 더 넓거나 좁게 조절하려면 이 값을 변경하세요 */
    padding: 16px;
    margin-bottom: 16px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease-in-out;
  }
  
  .article-box:hover {
    transform: scale(1.05);
  }
  
  .article-title {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 8px;
  }
  
  .article-content {
    font-size: 1rem;
    color: #555;
  }
  
  RouterLink {
    color: #1e4b4c;
    text-decoration: none;
    font-weight: bold;
    display: inline-block;
  }
  
  RouterLink:hover {
    text-decoration: underline;
  }
  </style>
   -->