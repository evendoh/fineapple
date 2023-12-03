<template>
<div class="calculator-container">
  <h1 class="calculator-title">외화로 환산</h1>

  <div class="form-group">
    <label for="exchangeRate">통화 선택:</label>
    <select
      v-model="selectedExchangeRate"
      id="exchangeRate"
      @change="updateSelectedExchangeRate"
      class="form-control"
    >
      <option
        v-for="item in store.exchangeRates"
        :key="item.id"
        :value="item"
      >
        {{ item.cur_nm }} - {{ item.cur_unit }} - {{ item.deal_bas_r }}
      </option>
    </select>
  </div>

  <div
    v-if="amount !== null && selectedExchangeRate"
    class="form-group"
    id="app"
  >
    <label for="amount">금액 입력: ( ₩ )</label>
    <input
      v-model="amount"
      type="number"
      id="amount"
      placeholder="금액을 입력하세요"
      class="form-control"
    />
  </div>

  <div
    v-if="amount !== null && selectedExchangeRate"
    class="result-container"
  >
    <p class="result">
      {{ calculateExchange() }}
      {{ selectedExchangeRate.cur_unit.slice(0, 3) }}
    </p>
  </div>
</div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const selectedExchangeRate = ref(null);
const amount = ref(0);

store.getExchangeRates()


const updateSelectedExchangeRate = () => {
console.log(selectedExchangeRate.value.deal_bas_r);
};

const calculateExchange = () => {
const exchangeRate = selectedExchangeRate.value.deal_bas_r;
const exchangeRate2 =
  exchangeRate < 4 ? exchangeRate : exchangeRate.replace(/,/g, "");
console.log("string", String(selectedExchangeRate.value.cur_unit).length);
const result =
  String(selectedExchangeRate.value.cur_unit).length >= 4
    ? (Number(amount.value) / Number(exchangeRate2)) * 100
    : Number(amount.value) / Number(exchangeRate2);

console.log("result", result);
return result.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
};
</script>
<style scoped>
.calculator-container {
max-width: 400px;
margin: auto;
padding: 40px;
text-align: center;
border: 1px solid #ddd;
border-radius: 10px;
background-color: #f9f9f9;
position: absolute;
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
}

.calculator-title {
text-align: center;
color: rgb(0, 75, 76);
}

.form-group {
margin-bottom: 20px;
}

.form-control {
width: 100%;
padding: 12px;
font-size: 1rem;
border: 1px solid #ccc;
border-radius: 5px;
box-sizing: border-box;
}

.result-container {
margin-top: 30px;
padding: 20px;
border: 1px solid #ddd;
border-radius: 8px;
background-color: #4b8b8e;
}

.result {
font-size: 1.2rem;
color: #fff;
margin: 0;
}
</style>