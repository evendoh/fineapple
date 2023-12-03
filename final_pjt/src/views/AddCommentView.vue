<template>
    <div>
      <h1 class="comment-title">댓글 작성</h1>
      <form @submit.prevent="submitComment">
        <div>
          <label for="comment">댓글 내용:</label>
          <textarea v-model="comment" id="comment" rows="4"></textarea>
        </div>
        <button type="submit">댓글 작성</button>
      </form>
  

  
      <RouterLink :to="{ name: 'DetailView', params: { id: route.params.id } }">뒤로 가기</RouterLink>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue';
  import axios from 'axios';
  import { ref } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';

  const store = useCounterStore();
  const router = useRouter();
  const route = useRoute();
  const comment = ref('');
  
  
  // 댓글 작성 함수
  const submitComment = async () => {
    try {
      await axios.post(`${store.API_URL}/articles/${route.params.id}/comment/`, {
        comment: comment.value,
      }, {
        headers: {
          Authorization: `Token ${store.token}`,
        },
      });
      alert('댓글이 작성되었습니다.');
      router.push({ name: 'DetailView', params: { id: route.params.id } });
    } catch (error) {
      console.error(error.response.data);
      alert('댓글 작성 중 오류가 발생했습니다.');
    }
  };
  
  </script>

  <style scoped>
  .comment-title {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  form {
    margin-bottom: 20px;
  }
  
  textarea {
    width: 100%;
    resize: vertical;
  }
  
  button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 10px 15px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
    border-radius: 4px;
  }
  </style>
  