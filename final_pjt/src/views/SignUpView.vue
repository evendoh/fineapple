<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <label for="username">아이디:</label>
      <input type="text" id="username" v-model.trim="username" required><br>
      
      <label for="password1">비밀번호:</label>
      <input type="password" id="password1" v-model.trim="password1" required><br>

      <label for="password2">비밀번호 확인:</label>
      <input type="password" id="password2" v-model.trim="password2" required><br>

      <label for="name">이름:</label>
      <input type="text" id="name" v-model.trim="name" required><br>

      <label for="age">나이:</label>
      <input type="number" id="age" v-model.trim="age" required><br>

      <label for="money">자산:</label>
      <input type="text" id="money" v-model.trim="money" required><br>
      
      <label for="saving_possible_money">매달 저축 가능 금액:</label>
      <input type="number" id="saving_possible_money" v-model.trim="saving_possible_money" required><br>

      <label for="saving_possible_period">저축 가능 기간: (개월)</label>
      <input type="number" id="saving_possible_period" v-model.trim="saving_possible_period" required><br>

      <label>원하는 금융 상품 유형:</label>
      <div>
        <input type="radio" id="예금" value="예금" v-model="financial_type" required>
        <label for="예금">예금</label>
        &nbsp;
        <input type="radio" id="적금" value="적금" v-model="financial_type" required>
        <label for="적금">적금</label>
      </div>

      <input type="submit" value="가입하기">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const username = ref('');
const password1 = ref('');
const password2 = ref('');
const name = ref('');
const age = ref(0);
const money = ref('');
const saving_possible_money = ref('');
const saving_possible_period = ref('');
const financial_type = ref('');

const store = useCounterStore();
const signUp = function () {
  if (password1.value !== password2.value) {
    console.error('비밀번호가 일치하지 않습니다.');
    alert('비밀번호가 일치하지 않습니다')
    return;
  }

  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    name: name.value,
    age: age.value,
    money: money.value,
    saving_possible_money: saving_possible_money.value,
    saving_possible_period: saving_possible_period.value,
    financial_type: financial_type.value,
  };

  store.signup(payload)
};
</script>

<style scoped>
.signup-container {
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

.signup-form {
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
