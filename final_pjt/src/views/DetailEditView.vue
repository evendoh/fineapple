<template>
    <div>
      <h1 class="detail-title">게시글 수정</h1>
      <div v-if="article" class="article-details">
        <p>글 번호 : {{ article.id }}</p>
        <label for="title" class="article-label">제목:</label>
        <input v-model="editedArticle.title" id="title" class="article-input" />
        <label for="content" class="article-label">내용:</label>
        <textarea v-model="editedArticle.content" id="content" class="article-input"></textarea>
        <button @click="saveChanges" class="save-button">저장</button>
        <button @click="deleteArticle" class="delete-button">삭제</button>
      </div>
      <RouterLink :to="{ name: 'DetailView', params: { id: route.params.id }}">
      뒤로가기
    </RouterLink>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { onMounted, ref } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  import { useRoute, useRouter } from 'vue-router';
  
  const store = useCounterStore();
  const route = useRoute();
  const router = useRouter();
  const article = ref(null);
  const editedArticle = ref({ title: '', content: '' });
  console.log(route);
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/articles/${route.params.id}/`,
    })
      .then((res) => {
        console.log(res.data);
        article.value = res.data;
        // 수정할 내용을 초기화합니다.
        editedArticle.value.title = res.data.title;
        editedArticle.value.content = res.data.content;
      })
      .catch((error) => {
        console.log(error);
      });
  });
  
  const saveChanges = () => {
    axios({
      method: 'put',
      url: `${store.API_URL}/articles/${route.params.id}/`,
      data: {
        title: editedArticle.value.title,
        content: editedArticle.value.content,
      },
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then((response) => {
        console.log('게시글 수정 성공');
        console.log(response.data);
        // 수정 후에 게시글 상세 페이지로 리다이렉트합니다.
        router.push({ name: 'DetailView', params: { id: route.params.id } });
      })
      .catch((error) => {
        console.log(error.response.data);
      });
  };
  
  const deleteArticle = () => {
    const confirmDelete = confirm('정말로 이 게시글을 삭제하시겠습니까?');
    if (confirmDelete) {
      axios({
        method: 'delete',
        url: `${store.API_URL}/articles/${route.params.id}/`,
        headers: {
          Authorization: `Token ${store.token}`,
        },
      })
        .then(() => {
          console.log('게시글 삭제 성공');
          // 삭제 후에 게시글 목록 페이지로 리다이렉트합니다.
          router.push({ name: 'article' });
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    }
  };
  </script>
  
  <style scoped>
  .detail-title {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .article-details {
    background-color: #f8f8f8;
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
  }
  
  .article-label {
    font-size: 18px;
    margin-top: 10px;
  }
  
  .article-input {
    width: 100%;
    margin-top: 5px;
    padding: 8px;
    font-size: 16px;
  }
  
  .save-button {
    background-color: #3498db; /* 파란색 */
    border: none;
    color: white;
    padding: 10px 15px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin-top: 10px;
    cursor: pointer;
    border-radius: 4px;
  }
  
  .delete-button {
    background-color: #e74c3c; /* 빨간색 */
    border: none;
    color: white;
    padding: 10px 15px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin-top: 10px;
    margin-left: 10px;
    cursor: pointer;
    border-radius: 4px;
  }
  </style>
  