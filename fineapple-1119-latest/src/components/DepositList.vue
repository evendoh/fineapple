<template>
    <div>
      <h3>예금목록</h3>
      <DepositListItem />
      <!-- <DepositListItem
      v-for="item in store.depositProducts"
      :key="item.id"
      :item="item"
       /> -->
    </div>
  </template>
  
  <script setup>
  import { useCounterStore } from '@/stores/counter';
  import DepositListItem from '@/components/DepositListItem.vue';
  
  const store = useCounterStore()
  console.log(store.depositProducts)
  </script>
  