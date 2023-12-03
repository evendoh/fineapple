<template>
  <section>
    <div>
      &nbsp;
    </div>
    <h2 class="icon fa-hand-peace-o" id="w">
      &nbsp; 16가지의 FMTI를 소개합니다~~!
    </h2>
    <div id="w">
      <p><strong>FMTI 란?</strong></p>
      <p>
        Financial Management Type Indicator의 약자로 mbti와 유사한 금융 관리
        유형 지표 입니다!
      </p>
      <ul>
        <li>A I 외향 내향 ( 자산 규모 및 거래양 확대 가능성 보유 )</li>
        <li>P B 전문가, 초보자 ( 투자 상품 가입 경험 )</li>
        <li>M W 집중형, 분산형 (선호 투자 상품 유형, 투자지역 분석)</li>
        <li>L C 자유형, 신중형 ( 금융 거래 선호 채널, 금융앱 사용여부)</li>
        <p>4가지 기준을 토대로 각 유형별로 총 16가지의 FMTI를 제공합니다.</p>
    </ul>
    </div>
    <div class="card-container">
      <div v-for="result in resultSet" :key="result.type" class="card">
        <img :src="`src/assets/images/${result.type}.jpg`" alt="" class="card-img-top" style="width: 200px; height: 200px" />
        <div class="card-body">
          <h3 class="card-title">{{ result.type }}</h3>
          <h4 class="card-subtitle">{{ result.tag }}</h4>
        </div>
        <hr class="my-2" />
      </div>
    </div>
    <article>
      <ul class="actions" style="text-align: center">
        <li>
          <button class="big custom-button" @click="$router.push({ name: 'test-test' })">
            검사하기!
          </button>
        </li>
      </ul>
    </article>
  </section>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useFinancialTypeTestStore } from "@/stores/financialTypeTest";

const route = useRoute();

const store = useFinancialTypeTestStore();
const { resultSet } = store;

const getImagePath = (type) => {
  return `@/assets/images/${type}.jpg`;
};
</script>

<style scoped>
.intro {
  max-width: 800px;
  margin: 0 auto;
  text-align: justify;
  line-height: 1.6;
  display: flex;
  text-align: center;
  justify-content: center; /* 수평 정렬 */
  align-items: center; /* 수직 정렬 */
}
#w {
  display: flex;
  text-align: center;
  justify-content: center; /* 수평 정렬 */
  align-items: center; /* 수직 정렬 */
}

.intro p {
  margin-bottom: 10px;
}
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  width: 200px;
  margin: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.card:hover {
  transform: scale(1.05);
}

.card-img-top {
  width: 100%;
  height: auto;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.card-body {
  text-align: center;
}

.card-title {
  font-size: 1.5rem;
  margin: 0.5rem 0;
}

.card-subtitle {
  font-size: 1rem;
  color: #666;
  margin: 0.5rem 0;
}

.big {
  font-size: 1.5rem;
}
.custom-button {
  background-color: #fff;
  color: #333; /* 버튼 텍스트 색상 */
  border: 2px solid #333; /* 테두리 선 색상 */
  padding: 10px 20px;
  transition: background-color 0.3s ease, color 0.3s ease; /* 호버 효과에 대한 전환 효과 */
}

.custom-button:hover {
  background-color: #333; /* 호버 시 배경색 변경 */
  color: #fff; /* 호버 시 텍스트 색상 변경 */
}
</style>
