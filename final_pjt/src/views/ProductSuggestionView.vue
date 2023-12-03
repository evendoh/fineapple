<template>
  <div class="profile-container">
    <h1>{{ store.userData.name }}님의 추천 금융 상품</h1>
    <p class="mi">
      {{ store.userData.name }}님의 FMTI를 기반으로 고객님과 유사한 FMTI를 가진
      사람들이 선택한 상품들입니다.
    </p>

    <div class="product-list-container">
      <h2 class="center">추천 상품 리스트</h2>
      <div class="product-category">
        <h3 class="center">예금 상품</h3>
        <div v-for="(product, index) in depositList" :key="product.id">
          <ProfileDepositListItem :item="product" :idx="index + 1" />
        </div>
      </div>

      <div class="product-category">
        <h3 class="center">적금 상품</h3>
        <div v-for="(product, index) in savingList" :key="product.id">
          <ProfileSavinglistItem :item="product" :idx="index + 1" />
        </div>
      </div>
      <div v-if="!store.userData.mbti">
        <p>추천 상품이 없으신가요?? </p>
        <p>추천을 받으시려면 먼저 FMTI 검사를 실행해주세요!</p>
        <button
          class="button special"
          @click="$router.push({ name: 'test-main' })"
        >
        FMTI 검사하기!
        </button>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import ProfileSavinglistItem from "@/components/ProfileSavinglistItem.vue";
import ProfileDepositListItem from "@/components/ProfileDepositListItem.vue";

const store = useCounterStore();
store.getProductByMbti()

const depositList = computed(() => {
  return store.depositProducts.filter((ele) => {
    return store.recommendedProduct.includes(ele.fin_prdt_cd);
  });
});

const savingList = computed(() => {
  return store.savingProducts.filter((ele) => {
    return store.recommendedProduct.includes(ele.fin_prdt_cd);
  });
});
</script>

<style scoped>
.profile-container {
  max-width: 700px;
  margin: 0 auto;
  padding: 20px;
}
.mi {
  text-align: center;
}
h1 {
  color: #1e4b4c;
  font-size: 28px;
  margin-bottom: 20px;
}

p {
  color: #333;
  margin-bottom: 20px;
}

.product-list-container {
  margin-top: 20px;
}

.product-category {
  margin-bottom: 40px;
}

.center {
  text-align: center;
}
</style>