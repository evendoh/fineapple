
<template>
  <div class="profile-update-container">
    <h1>프로필 정보 수정</h1>
    <form @submit.prevent="editProfile" class="profile-update-form">
      <label for="username" class="form-label">이름:</label>
      <input v-model.trim="name" disabled class="form-input" />

      <label for="age" class="form-label">나이:</label>
      <input v-model.trim="age" type="number" required class="form-input" />

      <label for="money" class="form-label">자산:</label>
      <input v-model.trim="money" type="number" required class="form-input" />

      <label for="saving_possible_money" class="form-label"
        >매달 저축 가능 금액:</label
      >
      <input
        v-model.trim="saving_possible_money"
        type="number"
        required
        class="form-input"
      />

      <label for="saving_possible_period" class="form-label"
        >저축 가능 기간: (개월)</label
      >
      <input
        v-model.trim="saving_possible_period"
        type="number"
        required
        class="form-input"
      />

      <label>원하는 금융 상품 유형:</label>
      <div>
        <input
          type="radio"
          id="예금"
          value="예금"
          v-model="financial_type"
          required
        />
        <label for="예금">예금</label>
        &nbsp;
        <input
          type="radio"
          id="적금"
          value="적금"
          v-model="financial_type"
          required
        />
        <label for="적금">적금</label>
        
        
      </div>
      <div class="button-container">
      <input type="submit" value="프로필 수정" class="submit-button" />
      </div>
    </form>
    <div class="button-container"></div>
    

    <button @click="withdrawMembership" class="withdraw-button">
      회원 탈퇴
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import router from "@/router";

const store = useCounterStore();

const name = store.userData.name; // 이름은 수정 불가능
const age = ref(store.userData.age);
const money = ref(store.userData.money);
const saving_possible_money = ref(store.userData.saving_possible_money);
const saving_possible_period = ref(store.userData.saving_possible_period);
const financial_type = ref(store.financial_type);

const editProfile = function () {
  const editedProfile = {
    age: age.value,
    money: money.value,
    saving_possible_money: saving_possible_money.value,
    saving_possible_period: saving_possible_period.value,
    financial_type: financial_type.value,
  };

  store.updateProfile(editedProfile);
};

const withdrawMembership = () => {
  if (confirm("정말로 회원 탈퇴하시겠습니까?")) {
    store.withdrawMembership();
  }
};
</script>

<style scoped>
.profile-update-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #1e4b4c;
  font-size: 28px;
  margin-bottom: 20px;
}

.profile-update-form {
  display: grid;
  gap: 10px;
}

.form-label {
  font-weight: bold;
}

.form-input {
  padding: 8px;
  width: 100%;
  box-sizing: border-box;
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.submit-button,
.withdraw-button {
  background-color: #1e4b4c;
  color: #fff;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover,
.withdraw-button:hover {
  background-color: #155c70;
}

.submit-button {
  flex: 1; /* 수정 버튼이 화면을 꽉 채우도록 설정 */
  margin-right: 10px; /* 수정 버튼과 회원 탈퇴 버튼 간격 조정 */
}

.withdraw-button {
  flex: 1; /* 회원 탈퇴 버튼이 화면을 꽉 채우도록 설정 */
}
</style>