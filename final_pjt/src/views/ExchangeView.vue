<template>
  <div class="container">
    <button @click="toggleCalculator">↔️</button>
    <div v-if="currentCalculator === 'calculator1'">
      <Calculator1 />
    </div>
    <div v-else>
      <Calculator2 />
    </div>
  </div>
</template>

<script setup>
import Calculator1 from "@/components/ExchangeRate.vue";
import Calculator2 from "@/components/ExchangeRate2.vue";
import { ref } from "vue";

const currentCalculator = ref("calculator1");

const toggleCalculator = () => {
  currentCalculator.value =
    currentCalculator.value === "calculator1" ? "calculator2" : "calculator1";
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.calculator-container {
  width: 100%; /* Adjust the width as needed */
  box-sizing: border-box;
  margin: 10px;
}

.container > button {
  position: absolute;
  width: 400px;
  bottom: 20%;
  transform: translate(-48%,-35%);
  left: 50%;
  border: none;
  border-radius: .5rem;
  box-shadow: 2px 2px 2px black;
}
/* button {
  width: 50%;
  height: 25%;
} */
</style>