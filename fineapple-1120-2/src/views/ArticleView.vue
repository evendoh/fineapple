<!-- <template>
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
    font-size: 50px;
    margin-bottom: 10px;
    font-family: 'Courier New', Courier, monospace;
    font-weight: 600;
  }
  
  /* [글쓰기] 링크 스타일 */
  .write-link {
    color: #1E4B4C;
    text-decoration: none;
    font-size: 18px;
    transition: text-decoration 0.3s ease-in-out;
    font-family: 'Courier New', Courier, monospace;

  }
  
  .write-link:hover {
    text-decoration: underline;
  }
  </style>
   -->

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
    background-color: #1E4B4C;
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
  