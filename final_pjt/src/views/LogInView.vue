<template>
  <div class="login-container">
    <h1>로그인</h1>
    <form @submit.prevent="logIn" class="login-form">
      <label for="username">아이디:</label>
      <input type="text" id="username" v-model.trim="username" required><br>

      <label for="password">비밀번호:</label>
      <input type="password" id="password" v-model.trim="password" required><br>

      <input type="submit" value="로그인">
      <RouterLink :to="{name: 'SignUpView'}">회원가입</RouterLink>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const username = ref('');
const password = ref('');

const store = useCounterStore();

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload)
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #1E4B4C;
  font-size: 28px;
  margin-bottom: 20px;
}

.login-form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
  font-size: 16px;
  color: #333;
}

input {
  padding: 10px;
  margin: 5px 0 15px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

input[type="submit"] {
  background-color: #1E4B4C;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

input[type="submit"]:hover {
  background-color: #153737;
}
</style>
