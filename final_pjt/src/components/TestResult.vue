<template>
  <section id="banner" class="text-center">
    <div class="container">
      <div class="card">
        <div class="card-body">
          <header class="header__">
            <h1 class="icon fa-tag">
              {{ store.userData.name }}님의 FMTI 타입은
              {{ data.type }} 입니다!<br />
            </h1>
            <h2 class="icon fa-tag">
              {{ data.tag }}
            </h2>
          </header>
          <hr />
          <p>{{ data.explain }}</p>
          <hr />
          <span class="image object">
          <img :src="`src/assets/images/${data.type}.jpg`" alt="" class="card-img-top" style="width: 200px; height: 200px" />
        </span>
          <ul class="actions row">
            <oi class="12u$">&nbsp;</oi>
            <template v-if="store.isLogin">
              <oi class="6u">
                <button class="btn btn-success btn-lg" @click="save">
                  FMTI 저장
                </button>
              </oi>
            </template>
            <oi>&nbsp;</oi>
            <oi class="6u$">
              <button
                class="btn btn-success btn-lg"
                @click="$router.push({ name: 'test-main' })"
              >
                다시 검사하기
              </button>
            </oi>
            <oi class="12u$">&nbsp;</oi>
          </ul>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useFinancialTypeTestStore } from "@/stores/financialTypeTest";
import { useCounterStore } from "@/stores/counter";

const route = useRoute();
const url = location.href;
const state = ref(false);

const store = useCounterStore();
const store2 = useFinancialTypeTestStore();
const { resultSet } = store2;
const data = ref("");
const mbti = ref(store2.resultType);
console.log("1", mbti);
resultSet.forEach((ele) => {
  console.log("ele", ele);
  console.log("resultType", store2.resultType);
  // console.log('route', route);
  if (ele.type == mbti.value) {
    data.value = ele;
  }
  console.log("data", data.value);
});

const save = () => {
  store.updateMbti(mbti.value);
};
console.log(route.params.type);
</script>

<style scoped>
.header__{
  background-color: white;
}
.icon{
  color: rgb(0, 75, 76);
}
.text-center {
  text-align: center;
}

.card {
  padding: 2em;
  background-color: #d4edda; /* 연한 초록색 배경색 */
  border-radius: 0;
}

h1 {
  font-size: 2.5em;
  margin-bottom: 0.5em;
}

h3 {
  font-size: 1.5em;
  margin-bottom: 1em;
}

p {
  font-size: 1.2em;
  margin-bottom: 1em;
}

.actions {
  margin-top: 2em;
}

.btn {
  border-radius: 0;
}

.btn-success {
  background-color: rgb(0, 75, 76);
  color: #fff;
  font-size: 1.2em;
}
</style>
