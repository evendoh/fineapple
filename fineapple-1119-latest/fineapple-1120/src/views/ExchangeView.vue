<template>
    <div>
        <h1>환율페이지</h1>
        <ExchangeRate />
    </div>
</template>

<script setup>
import ExchangeRate from '../components/ExchangeRate.vue';
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router'

const store=useCounterStore()
  onMounted(() => {
    store.getExchangeRates()
  })
</script>

<style scoped>

</style>