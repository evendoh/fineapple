<template>
    <div>
        <h1>예적금페이지</h1>
    </div>
    <form action="">
    <select name="은행" id="bank">
        <option value="kukmin">국민은행</option>
        <option value="shinhan">신한은행</option>
        <option value="woori">우리은행</option>
        <option value="hana">하나은행</option>
        <option value="saneop">산업은행</option>
        <option value="nonghyeop">농협</option>
        <option value="saemaeul">새마을금고</option>
        <option value="shinhyeop">신협</option>
        <option value="post">우체국</option>
        <option value="kieop">기업은행</option>
        <option value="busan">부산은행</option>
        <option value="daegu">대구은행</option>
        <option value="kwangju">광주은행</option>
        <option value="kn">경남은행</option>
        <option value="jb">전북은행</option>
        <option value="jj">제주은행</option>
        <option value="sh">수협</option>
      </select>
      <select name="예치기간" id="term">
        <option value="6m">6개월</option>
        <option value="6m">12개월</option>
        <option value="6m">24개월</option>
        <option value="6m">36개월</option>

      </select>
      <input type="submit" value="찾기" />
    </form>
<DepositList />
<SavingList />
</template>

<script setup>

import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { RouterLink } from 'vue-router'
// import DepositList from '@/components/DepositList.vue';
// import SavingList from '@/components/SavingList.vue';

const store=useCounterStore()
  onMounted(() => {
    store.getDepositProducts()
    store.getSavingProducts()
    // console.log(store.depositProducts)
    // console.log(store.savingProducts)
  })

</script>

<style scoped>

</style>