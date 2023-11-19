<!-- <template>
    <div>
      <h1>Detail</h1>
      <div v-if="article">
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <p>{{ article.created_at }}</p>
      <p>{{ article.updated_at }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { onMounted, ref } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { useRoute } from 'vue-router';
  
  const store = useCounterStore()
  const route = useRoute()
  const article = ref(null)
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/articles/${route.params.id}/`
  })
  .then((res) => {
    console.log(res.data)
    article.value = res.data
  })
  .catch((error) => {
    console.log(error)
  })
  })
  </script>
  
  <style>
  
  </style> -->

  <template>
    <div>
      <h1>Detail</h1>
      <div v-if="article">
        <div class="article-details">
          <h2>{{ article.title }}</h2>
          <p class="article-metadata">
            <span>Created at: {{ formatDate(article.created_at) }}</span>
            <span>Updated at: {{ formatDate(article.updated_at) }}</span>
          </p>
          <p class="article-content">{{ article.content }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { onMounted, ref } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { useRoute } from 'vue-router';
  
  const store = useCounterStore();
  const route = useRoute();
  const article = ref(null);
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/articles/${route.params.id}/`,
    })
      .then((res) => {
        console.log(res.data);
        article.value = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  });
  
  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };
  </script>
  
  <style scoped>
  .article-details {
    background-color: #f8f8f8;
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
  }
  
  .article-metadata {
    color: #555;
    font-size: 0.8em;
  }
  
  .article-content {
    margin-top: 10px;
  }
  </style>
  