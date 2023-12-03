<template>
  <div class="create-article-container">
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle" class="article-form">
      <div class="form-group">
        <label for="title">제목 :</label>
        <input type="text" id="title" v-model.trim="title" required />
      </div>
      <div class="form-group">
        <label for="content">내용 :</label>
        <textarea id="content" v-model.trim="content" required></textarea>
      </div>
      <button type="submit">작성 완료</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";

const title = ref("");
const content = ref("");

const store = useCounterStore();
const router = useRouter();

const createArticle = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      router.push({ name: "article" });
    })
    .catch((err) => {
      console.error(err);
    });
};
</script>

<style scoped>
.create-article-container {
  max-width: 100%;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #1e4b4c;
  font-size: 36px;
  margin-bottom: 20px;
  text-align: center;
}

.article-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-size: 16px;
  color: #333;
}

input,
textarea {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

button {
  background-color: #1e4b4c;
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
