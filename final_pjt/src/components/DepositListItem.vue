<template>
  <div class="table-container">
    <table class="styled-table">
      <tr>
        <td class="label">
          {{ item.id }}
        </td>
        <td class="bank">
          {{ item.kor_co_nm }}
        </td>
        <td class="product">
          <span @click="toggleDetails">{{ item.fin_prdt_nm }}</span>
        </td>
        <td class="option1">
          <p>
            {{
              options
                .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                .filter((option) => option.save_trm === 6)[0]
                ? options
                    .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                    .filter((option) => option.save_trm === 6)[0].intr_rate
                : "-"
            }}
          </p>
        </td>
        <td class="option2">
          <p>
            {{
              options
                .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                .filter((option) => option.save_trm === 12)[0]
                ? options
                    .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                    .filter((option) => option.save_trm === 12)[0].intr_rate
                : "-"
            }}
          </p>
        </td>
        <td class="option3">
          <p>
            {{
              options
                .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                .filter((option) => option.save_trm === 24)[0]
                ? options
                    .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                    .filter((option) => option.save_trm === 24)[0].intr_rate
                : "-"
            }}
          </p>
        </td>
        <td class="option4">
          <p>
            {{
              options
                .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                .filter((option) => option.save_trm === 36)[0]
                ? options
                    .filter((option) => option.fin_prdt_cd === item.fin_prdt_cd)
                    .filter((option) => option.save_trm === 36)[0].intr_rate
                : "-"
            }}
          </p>
        </td>
      </tr>
      <tr v-if="showDetails">
        <td colspan="7">
          <table class="details-table">
            <tr>
              <td class="td1">금융상품설명</td>
              <td>{{ item.etc_note }}</td>
            </tr>
            <tr>
              <td class="td1">가입제한</td>
              <td>
                <span v-if="item.join_deny === 1">제한 없음</span>
                <span v-else-if="item.join_deny === 2">서민전용</span>
                <span v-else-if="item.join_deny === 3">일부제한</span>
              </td>
            </tr>
            <tr>
              <td class="td1">가입대상</td>
              <td>{{ item.join_member }}</td>
            </tr>
            <tr>
              <td class="td1">가입방법</td>
              <td>{{ item.join_way }}</td>
            </tr>
            <tr>
              <td class="td1">우대조건</td>
              <td>{{ item.spcl_cnd }}</td>
            </tr>
            <tr>
              <td class="td1">만기 후 이자율</td>
              <td>{{ item.mtrt_int }}</td>
            </tr>
            <tr>
              <td class="td1">최고한도</td>
              <td>{{ item.max_limit }}</td>
            </tr>
          </table>
          <button @click="handleButtonClick">{{ showDetails2 ? '해지하기' : '가입하기' }}</button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useCounterStore } from "@/stores/counter";
import { storeToRefs } from "pinia";
const store = useCounterStore();
const showDetails = ref(false);
const options = ref([]);
options.value = store.depositProductsOptions;

const router = useRouter();

const toggleDetails = () => {
  showDetails.value = !showDetails.value;
};
const product = defineProps({
  item: Object,
});
// console.log('11', product.item.fin_prdt_cd);


const showDetails2 = ref(false)

showDetails2.value = Array.from(store.wantProducts).find((ele) => {
  return ele === product.item.fin_prdt_cd
})

const handleButtonClick =  () => {
  if (store.isLogin) {
    if (!showDetails2.value) {
      // 해지하기 버튼을 눌렀을 때의 동작
      // product에 해당 상품에 대한 정보를 넣어주고, 요청을 다시 보내고, 버튼을 '가입하기'로 변경하는 로직 추가
      store.updateFinancial(product.item.fin_prdt_cd);
      store.wantProducts.push(product.item.fin_prdt_cd);
      console.log("상품 추가 완");
      
      showDetails2.value = !showDetails2.value;
    } else {
      // 가입하기 버튼을 눌렀을 때의 동작
      // product에 해당 상품에 대한 정보를 넣어주고, 해당 함수가 작동하게 해주고, 버튼을 '해지하기'로 변경하는 로직 추가
      store.updateFinancial(product.item.fin_prdt_cd);
      const index = store.wantProducts.indexOf(product.item.fin_prdt_cd);
      // store.wantProducts.push(product.item.fin_prdt_cd)
      store.wantProducts.splice(index, 1);
      console.log("상품 제거 완");
      console.log(store.wantProducts);
      showDetails2.value = !showDetails2.value;
    }
  }
  else {
    alert("로그인이 필요합니다.")
    router.push('/login');
  }
};
</script>

<style scoped>
.table-container {
  max-width: 1000px;
  margin: auto;
}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.styled-table tr {
  border-bottom: 1px solid #ddd;
}

.styled-table td {
  padding: 12px;
  text-align: left;
}

.styled-table td.label {
  font-weight: bold;
  width: 10%;
}
.styled-table td.bank {
  width: 20%;
}

.styled-table td.product {
  font-weight: bold;
  width: 30%;
  white-space: nowrap; /* Prevent line breaks */
  overflow: hidden; /* Hide overflowing content */
  text-overflow: ellipsis; /* Display ellipsis (...) for overflow */
}

.styled-table td.option1,
.styled-table td.option2,
.styled-table td.option3,
.styled-table td.option4 {
  width: 10%; /* 조절된 값 */
}

.details-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.details-table td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  background-color: white;
}
.td1 {
  font-weight: bold;
  width: 25%;
}

.td2 {
}
.details-label {
  font-weight: bold;
  width: 30%;
}
</style>
