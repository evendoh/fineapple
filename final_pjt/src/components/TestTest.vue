<template>
  <div class="loading-container" v-if="wait">
    <img src="@/assets/images/loading!.gif" />
  </div>
  <section class="text-center">
    <div>
      &nbsp;
    </div>
    <h2>자신의 금융 가치관에 더 가까운 반응을 선택해주세요!</h2>
    <div class="features row">
      <div class="12u$">
        <div class="card">
          <div class="card-body">
            <h2>
              <span class="icon fa-spinner" id="smaller"></span> &nbsp;{{ cnt }}
              / 12
            </h2>
            <h2>{{ data[0] }}</h2>
          </div>
        </div>
      </div>
      <hr class="12u$" />
      <div class="12u$">
        <ul class="actions">
          <li id="row">
            <button
              class="btn btn-outline-custom btn-lg"
              id="smaller"
              @click="next(0)"
            >
              {{ data[1] }}
            </button>
          </li>
          <li>
            <button class="btn btn-custom btn-lg" id="smaller" @click="next(1)">
              {{ data[2] }}
            </button>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useFinancialTypeTestStore } from "@/stores/financialTypeTest";
import { storeToRefs } from "pinia";

const router = useRouter();
const store = useFinancialTypeTestStore();
const { startTest, endTest } = store;
const { typeA, typeB, typeC, typeD, resultType } = storeToRefs(store);
const cnt = ref(0);
const data = ref(typeA.value.question[0]);
const wait = ref(false);
const waitting = (time) => new Promise((resolve) => setTimeout(resolve, time));
const next = (n) => {
  if (cnt.value % 4 == 0) {
    typeA.value.count += n;
  } else if (cnt.value % 4 == 1) {
    typeB.value.count += n;
  } else if (cnt.value % 4 == 2) {
    typeC.value.count += n;
  } else if (cnt.value % 4 == 3) {
    typeD.value.count += n;
  }
  cnt.value++;
};

onMounted(() => {
  startTest();
});

watch(cnt, async () => {
  if (cnt.value == 12) {
    wait.value = true;
    endTest();
    await waitting(2000);
    wait.value = false;
    router.push({ name: "test-result", params: { type: resultType.value } });
    return;
  }

  if (cnt.value % 4 == 0) {
    data.value = typeA.value.question[Math.floor(cnt.value / 4)];
  } else if (cnt.value % 4 == 1) {
    data.value = typeB.value.question[Math.floor(cnt.value / 4)];
  } else if (cnt.value % 4 == 2) {
    data.value = typeC.value.question[Math.floor(cnt.value / 4)];
  } else if (cnt.value % 4 == 3) {
    data.value = typeD.value.question[Math.floor(cnt.value / 4)];
  }
});
</script>

<style scoped>
#smaller {
  font-size: medium;
}
.loading-container {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 0;
}

.text-center {
  text-align: center;
}

.features {
  margin-top: 2rem;
}

.card {
  padding: 1rem;
  background: #fff;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  border-radius: 0;
  z-index: -1;
}

.actions {
  list-style: none;
  padding: 0;
}

.actions li {
  display: inline-block;
  margin: 0 10px;
}

.btn-outline-custom {
  background-color: transparent;
  border-color: rgb(0, 75, 76);
  color: rgb(0, 75, 76);
}

.btn-custom {
  background-color: rgb(0, 75, 76);
  border-color: rgb(0, 75, 76);
  color: #fff;
}

.btn {
  border-radius: 5;
}
</style>