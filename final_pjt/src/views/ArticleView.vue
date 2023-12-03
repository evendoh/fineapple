<template>
  <div class="board-container">
    <h1 class="board-title">게시판</h1>
    <RouterLink :to="{ name: 'CreateView' }" class="write-link"> + </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
import ArticleList from "@/components/ArticleList.vue";
const store = useCounterStore();

onMounted(() => {
  store.getArticles();
});
</script>

<style scoped>
/* 게시판 스타일 */
.board-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.board-title {
  color: #333;
  font-size: 36px;
  margin-bottom: 20px;
  text-align: center;
}

/* [글쓰기] 링크 스타일 */
.write-link {
  display: inline-block;
  margin-bottom: 20px;
  padding: 10px 20px;
  color: #fff;
  background-color: #1e4b4c;
  text-decoration: none;
  font-size: 18px;
  font-weight: bold;
  border-radius: 5px;
  transition: background-color 0.3s ease-in-out;
}

.write-link:hover {
  background-color: #153737;
}
</style>
