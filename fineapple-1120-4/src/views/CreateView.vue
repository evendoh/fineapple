<!-- <template>
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
   -->

   <template>
    <div class="create-article-container">
      <h1>게시글 작성</h1>
      <form @submit.prevent="createArticle" class="article-form">
        <label for="title">제목 :</label>
        <input type="text" id="title" v-model.trim="title" required>
        <label for="content">내용 :</label>
        <textarea id="content" v-model.trim="content" required></textarea>
        <button type="submit">작성 완료</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useCounterStore } from '@/stores/counter';
  import { useRouter } from 'vue-router';
  
  const title = ref('');
  const content = ref('');
  
  const store = useCounterStore();
  const router = useRouter();
  
  const createArticle = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/articles/`,
      data: {
        title: title.value,
        content: content.value,
      },
    })
      .then((res) => {
        console.log(res);
        router.push({ name: 'ArticleView' });
      })
      .catch((err) => {
        console.error(err);
      });
  };
  </script>
  
  <style scoped>
  .create-article-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  
  h1 {
    color: #1E4B4C;
    font-size: 36px;
    margin-bottom: 20px;
  }
  
  .article-form {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-top: 10px;
    font-size: 16px;
    color: #333;
  }
  
  input,
  textarea {
    padding: 10px;
    margin: 5px 0 15px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
  }
  
  button {
    background-color: #1E4B4C;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  button:hover {
    background-color: #153737;
  }
  </style>
  